# Image to WebP

A simple Python script that converts a batch of images of various formats into WebP format.

## Formats

Current list of image formats:

- .png
- .jpg

## Setup

_Note: I recommend virtual environments (venv) unless you know what you're doing of course_

_See the folks here for a very good primer on venvs and how to create your own: [RealPython - Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/#how-can-you-work-with-a-python-virtual-environment)_

---

### Clone and Install

First, clone this repo (or download the file itself: `main.py`)

Afterwards, install the necessary library (Pillow for image manipulation) with your package manager (ie. pip).

```
$ pip install -r requirements.txt
```

### Creating an input folder

This relies on reading all images within an `input` folder within the same directory as the script.

> If you do not have an input folder, the script will throw an exception to remind you to create an input folder.

Place all images that requires converting into the `input` folder. Your working directory should look something like this:

```
py-image-to-webp/
├── input/
  ├── image1.png
  ├── image2.png
  ├── ...
  ├── imageX.jpg
├── requirements.txt
├── main.py         <--- main script!
├── ...
```

### Running the script

Once you have loaded the `input` folder with your images, run the script. I use **[wsl](https://learn.microsoft.com/en-us/windows/wsl/about)** to run my python script so your method / operating system will vary:

```
$ python3 main.py
$
$ Converting image1.jpg
$ Converting image2.jpg
$ ...
$ Converting imageX.png
```

The script will generator an `output` folder within the same directory as the script so you should see that folder. Within the `output` folder, you should see your batch of **.webp** files and that should be it!
