#!/usr/bin/env python

import argparse
from ocr import ocr
from confluence import ConfluenceAPI

# load a picture, send it to ocr API and get response
def extract_text_from_image(image, type):
    ocr(image, type)

def create_confluence_page():
    api = ConfluenceAPI()
    page_content = file('ocr_result.txt', 'rb').read()
    api.create_page(page_content)

# Extract text from response and load it into Confluence


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract text from Image and load it into Confluence')
    parser.add_argument('--image-file', dest='image_file', action='store',
                        help='Specify the image location')
    parser.add_argument('--image-url', dest='image_url', action='store',
                        help='Specify the image url')

    args = parser.parse_args()

    if args.image_file is not None:
        extract_text_from_image(args.image_file, 'file')
    else:
        extract_text_from_image(args.image_url, 'url')

    create_confluence_page()
