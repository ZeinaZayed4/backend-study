import re


def main():
    code = input("Hexadecimal color code: ")
    
    pattern = r"^#[a-fA-F0-9]{6}$"
    if match := re.search(pattern, code):
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")


main()
