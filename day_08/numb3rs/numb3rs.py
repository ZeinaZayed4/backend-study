import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^([1-9]\d*|0)\.([1-9]\d*|0)\.([1-9]\d*|0)\.([1-9]\d*|0)$", ip):
        return all(0 <= int(n) <= 255 for n in match.groups())
    return False


if __name__ == "__main__":
    main()
