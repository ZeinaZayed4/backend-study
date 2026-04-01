def main():
    text = input("Plate: ")
    print("Valid" if is_valid(text) else "Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s.isalnum():
        return False
    
    digit = False
    for c in s[2:]:
        if c.isdigit():
            if not digit and c == "0":
                return False
            digit = True
        elif digit:
            return False
    return True


if __name__ == "__main__":
    main()
