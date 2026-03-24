def main():
    house = area(20, 40)
    yard = area(20, 80)
    total = house + yard
    print(f'{total} total square feet.')


def area(length, width):
    print(f'{length * width} square feet.')
    return length * width


main()