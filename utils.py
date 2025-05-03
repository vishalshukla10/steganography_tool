from PIL import Image
import os

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    if img.format in ['JPEG', 'JPG']:
        print("[!] JPEG detected. Converting to PNG...")
        image_path = os.path.splitext(image_path)[0] + '.png'
        img.save(image_path)
        img = Image.open(image_path)

    binary_msg = ''.join([format(ord(char), '08b') for char in message]) + '1111111111111110'
    pixels = img.load()
    idx = 0
    for y in range(img.height):
        for x in range(img.width):
            if idx < len(binary_msg):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_msg[idx])
                pixels[x, y] = (r, g, b)
                idx += 1
            else:
                break
    img.save(output_path)
    print(f"[+] Message embedded in {output_path}")

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    binary_msg = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_msg += str(r & 1)

    bytes_ = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ""
    for byte in bytes_:
        if byte == '11111110':
            break
        message += chr(int(byte, 2))
    print("[+] Hidden message:", message)
