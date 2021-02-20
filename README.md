<p align="center">
  <img src="https://res.cloudinary.com/wark/image/upload/v1576923027/image_optimizer.png" width="665px">
  <h2 align="center" style="margin-top: -4px !important;">Optimize your images for web and local storage</h2>
  <p align="center">
    <a href="https://github.com/dt-wark/image-optimizer/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-green.svg">
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-v3.8-blue.svg">
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/status-stable-brightgreen.svg">
    </a>
  <a href="https://github.com/dt-wark/image-optimizer/pulls?utf8=%E2%9C%93&amp;q=is%3Apr%20author%3Aapp%2Fdependabot"><img src="https://camo.githubusercontent.com/6266857d1c53194119edf1d9aafae7a4b301fa16/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646570656e64656e636965732d7570253230746f253230646174652d627269676874677265656e2e737667" alt="Dependencies Status" data-canonical-src="https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg" style="max-width:100%;"></a>
    <a href="https://res.cloudinary.com/wark/image/upload/v1576597812/bit.png">
      <img src="https://img.shields.io/badge/btc-1AnYqP7mt7QxqYc6fmQk5m6YHN8Rqan4ze-informational.svg">
    </a>
  </p>
</p>

## What does optimizer do?

The script uses TinyPNG smart lossy compression techniques to reduce the file size of your JPG/PNG files. By selectively decreasing the number of colors in the image, fewer bytes are required to store the data. The effect is nearly invisible but it makes a very large difference in file size.

## Setup

1. Download and install the latest version of Python
2. Clone this repo
```
git clone https://github.com/kerogenesis/image-optimizer.git
```

3. Create and activate virtual environment
```
python3.9 -m venv venv
source venv/bin/activate
```

4. Install dependencies
```
pip install -r requirements.txt
```

## Initial setting

1. Open `settings.py` in any text editor.
2. Add a key from [tinypng.com/developers](https://tinypng.com/developers/) to the `API_KEY` field.
3. In the `USER_INPUT_PATH` field add a directory path with raw images.
4. In the `USER_OUTPUT_PATH` field add the directory path with compressed files.

You can also select the option to delete raw images after compression.


## Easy way to use

### Linux/macOS

Create `сompression.sh` file with:

```
#!/usr/bin/env bash
source path/to/venv/bin/activate && python3.9 path/to/image_optimizer.py
```

Give this file permission to execute:
```
chmod +x сompression.sh
```

Move it to any place (e.g. desktop) and run it.

### Windows

Create `compression.bat` file with:

```
@echo off
cmd /c "path\to\venv\Scripts\python.exe path\to\image_optimizer.py"
```

Move it to any place (e.g. desktop) and run it.

## Important note

**Remember the limit of 500 images per month on the free plan. You can change this at [tinypng.com/dashboard/api](https://tinypng.com/dashboard/api)**
