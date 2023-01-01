"""
CardVisionPy

A reimplementation of bergquester/CardVision in Python
using OpenCV and Tesseract.

"""
import argparse
import os

from cardvisionpy import cardvisionpy


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--input-path",
        default="images/",
        help="The directory to read image files from. Defaults to ./images/",
    )
    argparser.add_argument(
        "--output-file",
        default="transactions.csv",
        help="The CSV file to write transactions to. Defaults to ./transactions.csv",
    )

    args = argparser.parse_args()
    input_path = os.path.abspath(args.input_path)
    output_file = os.path.abspath(args.output_file)

    transactions = cardvisionpy.get_processed_transactions(input_path)
    cardvisionpy.write_to_csv(transactions, output_file)


if __name__ == "__main__":
    main()
