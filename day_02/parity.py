def main():
    x = int(input("What's x? "))

    print("Even" if is_even(x) else "Odd")


def is_even(x):
    return (x % 2 == 0)


main()
