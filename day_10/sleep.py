def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(1, n + 1):
        yield "🐏" * i


if __name__ == "__main__":
    main()
