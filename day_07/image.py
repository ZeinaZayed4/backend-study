from PIL import Image, ImageFilter


def main():
    with Image.open("in.jpeg") as image:
        image = image.rotate(180)
        image = image.filter(ImageFilter.FIND_EDGES)
        image.save(f"out.jpeg")


main()
