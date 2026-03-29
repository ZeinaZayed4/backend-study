def main():
    height = int(input('Height: '))
    pyramid(height)


def pyramid(h):
    for i in range(1, h + 1):
        print('#' * i)


main()
