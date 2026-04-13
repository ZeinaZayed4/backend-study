def minion_game(string):
    string = string.upper()
    vowels = "AEIOU"
    kevin, stuart = 0, 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)