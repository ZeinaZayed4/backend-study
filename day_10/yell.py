def main():
    yell("This", "is", "CS50")


def yell(*words):
    lowercased = map(str.lower, words)
    print(*lowercased)
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
