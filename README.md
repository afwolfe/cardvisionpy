# cardvisionpy

A Python reimplementation of [BergQuester's CardVision](https://github.com/BergQuester/CardVision) to process Apple Card transaction screenshots using Tesseract.

It can be imported and used as a module in other Python scripts or as a standalone CLI.

## Requirements

* Python 3.9+
* [Tesseract](https://github.com/tesseract-ocr/tesseract)

## Usage

### Installation

`pip install git+https://github.com/afwolfe/cardvisionpy`

### Importing

You can install and import cardvisionpy as a module in your own projects.

For an example of this, see [AppleCardToYnab](https://github.com/afwolfe/AppleCardToYnab/)

### Standalone CLI

You can also use cardvisionpy as a CLI to process and export a folder of image screenshots as a CSV file.

```bash
$ python -m cardvisionpy --help
usage: __main__.py [-h] [--input-path INPUT_PATH] [--output-file OUTPUT_FILE]

options:
  -h, --help            show this help message and exit
  --input-path INPUT_PATH
                        The directory to read image files from. Defaults to ./images/
  --output-file OUTPUT_FILE
                        The CSV file to write transactions to. Defaults to ./transactions.csv
```

## Acknowledgements

* The cardvisionpy module would not be possible without the work originally done by [BergQuester's CardVision](https://github.com/BergQuester/CardVision) project to handle a lot of the "weirdness" of parsing Apple Card screenshots. While OpenCV/Tesseract handle them slightly differently than Apple's VisionKit, it provided a good starting point.
