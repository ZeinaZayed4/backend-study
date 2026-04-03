import os

from PIL import Image, ImageOps
from sys import argv, exit

if len(argv) == 3:
    in_file, out_file = argv[1], argv[2]
    ext_in = os.path.splitext(in_file)[1].lower()
    ext_out = os.path.splitext(out_file)[1].lower()
    
    supported_ext = [".jpg", ".jpeg", ".png"]
    if not ext_in in supported_ext or not ext_out in supported_ext:
        exit("Invalid input")
    elif ext_in != ext_out:
        exit("Input and output have different extensions")

    try:
        with Image.open(in_file) as in_image, Image.open("shirt.png") as mask_image:
            size = mask_image.size
            out_image = ImageOps.fit(in_image, size)
            out_image.paste(mask_image, mask_image)
            out_image.save(out_file)
    except FileNotFoundError:
        exit("Input does not exist")

elif len(argv) > 3:
    exit("Too many command-line arguments")
else:
    exit("Too few command-line arguments")
