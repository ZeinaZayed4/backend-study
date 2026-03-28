def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    
    digit = False
    for c in s[2:]:
        if c.isdigit():
            if not digit and c == '0':
                return False
            digit = True
        elif digit:
            return False
    
    return True


main()
