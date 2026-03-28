def main():
    while True:
        size = int(input("What's the square size? "))
        if size > 0:
            break

    print_square(size)


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print('* ' * width)


main()
