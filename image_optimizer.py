import os
import shutil
import sys

import tinify

import settings


SUPPORTED_FORMATS = ('jpg', 'jpeg', 'png')


def create_dirs(raw_images_dir=settings.USER_INPUT_PATH,
                save_dir=settings.USER_OUTPUT_PATH):
    """Creates the necessary directories if they do not exist.

    Args
        raw_images_dir (str): raw directory path
        save_dir (str): save directory path
    """

    # Checking raw-images directory
    if not os.path.isdir(raw_images_dir):
        os.makedirs(raw_images_dir)

    # Collect user directories in raw-images dir
    custom_dirs = []
    for root, directories, files in os.walk(raw_images_dir):
        for directory in directories:
            custom_path = os.path.join(save_dir, directory)
            custom_dirs.append(custom_path)

    # Creation of all necessary dirs in the dir with compressed images
    compress_dirs = (save_dir, (*custom_dirs))
    for dir_ in compress_dirs:
        if not os.path.isdir(dir_):
            os.makedirs(dir_)


def get_raw_images(raw_images_dir=settings.USER_INPUT_PATH):
    """Gets images path from the user directory.

    If supported images are found, return a list :raw_images:
    Else raises an exception

    Arg
        raw_images_dir (str): raw directory path
    """

    print('\n[*] Looking for images...\n')

    raw_images = []

    # Walk the tree
    for root, directories, files in os.walk(raw_images_dir):
        for filename in files:
            if not filename.startswith('.'):
                file_type = filename.split('.')[-1]
                if file_type in SUPPORTED_FORMATS:
                    filepath = os.path.join(root, filename)
                    raw_images.append(filepath)

    # If no images found → raise exception
    if not raw_images:
        try:
            raise OSError('No images found')
        except OSError:
            dir_name = os.path.basename(raw_images_dir)
            print(f'[!] Please add images to “{dir_name}” and try again...\n')
            sys.exit()

    return raw_images


def change_dir(abs_image_path,
               raw_images_dir=settings.USER_INPUT_PATH,
               save_dir=settings.USER_OUTPUT_PATH):
    """Changes the directory to the save location.

    Args
        abs_image_path (str): absolute image path
        raw_images_dir (str): raw directory path
        save_dir (str): save directory path
    """

    # If the original image is not saved in the custom direcory,
    # change the directory to the default save-directory
    if os.path.dirname(abs_image_path) == raw_images_dir:
        os.chdir(save_dir)

    else:  # Else change the directory to a custom
        custom_dir_path = os.path.dirname(abs_image_path)
        custom_dir_name = os.path.basename(custom_dir_path)
        compressed_custom_dir_path = os.path.join(save_dir, custom_dir_name)
        os.chdir(compressed_custom_dir_path)


def compress_and_save(abs_image_path,
                      metadata=settings.METADATA):
    """Compresses and saves result image.

    Args
        abs_image_path (str): absolute image path
        metadata (bool): user metadata flag
    """

    # Get image info
    only_image_path, image_info = os.path.split(abs_image_path)
    image_name, image_type = image_info.split('.')

    if metadata:  # Transfer the metadata (if this op. selected in the settings)
        meta_filename = f'{image_name}_optimized_copyright.{image_type}'
        if not os.path.isfile(meta_filename):
            print(f'[*] Compressing {image_name}')
            source = tinify.from_file(abs_image_path)
            copyrighted = source.preserve('copyright', 'creation')

            print(f'[*] Saving {meta_filename}\n')
            copyrighted.to_file(meta_filename)

    else:  # Just save image without metadata
        optimized_filename = f'{image_name}_optimized.{image_type}'
        if not os.path.isfile(optimized_filename):
            print(f'[*] Compressing {image_name}')
            source = tinify.from_file(abs_image_path)

            print(f'[*] Saving {optimized_filename}\n')
            source.to_file(optimized_filename)


def delete_after_compress(raw_images_dir=settings.USER_INPUT_PATH):
    """Deletes all uncompressed images.

    Creates an empty directory if the main directory is deleted

    Arg
        raw_images_dir (str): raw directory path
    """

    shutil.rmtree(raw_images_dir, ignore_errors=True)
    if not os.path.isdir(raw_images_dir):
        os.makedirs(raw_images_dir)


def main():
    try:
        # Prepare tinify
        tinify.key = settings.API_KEY
        tinify.validate()

        # Main logic
        create_dirs()
        raw_image_pull = get_raw_images()
        for image in raw_image_pull:
            change_dir(image)
            compress_and_save(image)
        print('[!] All optimized images have been saved')

        if settings.DELETE_RAW_AFTER_COMPRESS:
            delete_after_compress()
            print('\n[×] All the uncompressed images have been removed [×]\n')

    except tinify.AccountError:
        print('[AccountError]: Please verify your Tinify API key and account limit.')
    except tinify.ClientError:
        print('[ClientError]: Please check your source image.')
    except tinify.ServerError:
        print('[ServerError]: Temporary issue with the Tinify API.')
    except tinify.ConnectionError:
        print('[ConnectionError]: A network connection error occurred.')
    except Exception as e:
        print('[UnknownError]: Something went wrong. Please try again...\n', e)


if __name__ == "__main__":
    main()
