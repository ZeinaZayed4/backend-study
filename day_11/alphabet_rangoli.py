def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3

    for i in range(size - 1, -1, -1):
        left = alphabet[size-1:i:-1]
        right = alphabet[i:size]
        row = left + right
        print("-".join(row).center(width, "-"))

    for i in range(1, size):
        left = alphabet[size-1:i:-1]
        right = alphabet[i:size]
        row = left + right
        print("-".join(row).center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
