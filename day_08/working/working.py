import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)
    if not match:
        raise ValueError("Invalid format")
    
    h1, m1, p1, h2, m2, p2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
        raise ValueError("Invalid minutes")
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError("Invalid hours")
    
    h1 = convert_hour(h1, p1)
    h2 = convert_hour(h2, p2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def convert_hour(h, p):
    if p == "AM":
        return 0 if h == 12 else h
    else:
        return 12 if h == 12 else h + 12


if __name__ == "__main__":
    main()
