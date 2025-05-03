This is a simple Python-based tool for hiding messages in images using steganography. The tool provides two main functionalities:

1. **Encoding** - Hide a secret message within an image.
2. **Decoding** - Extract the hidden message from an image.

## Features

- The tool works with PNG and JPEG images.
- Automatically converts JPEG images to PNG for lossless encoding.
- Hidden messages are stored in the least significant bit of pixel color values.
- Supports both encoding and decoding operations.

## Requirements

- Python 3.x
- Pillow library (for image handling)

Install the required library using the following command:

    pip install pillow

## Usage

### Encoding a Message

To hide a message in an image, run the encode.py script. This will embed the message into the image and save the new image with the hidden message.

    python encode.py

You can modify the script to change the input image, secret message, and output file. The default example hides the message the secret key is 1034 in the image input.jpg and saves the result as output.png.

Decoding a Message

To extract the hidden message from an image, run the decode.py script. This will retrieve and display the secret message.

    python decode.py

You can modify the script to change the input image. The default example retrieves the message from the image output.png.

Example

    Start with an image (e.g., input.jpg).

    Use encode.py to embed a secret message.

    Use decode.py to reveal the hidden message.

Notes

    Make sure your input image is in a supported format (PNG or JPEG).

    JPEG images are automatically converted to PNG to ensure lossless encoding.

    The message is hidden using the least significant bit method in the pixel values of the image.

    The script is meant for educational purposes and demonstration of steganography.
