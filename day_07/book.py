def main():
    with open("alice.txt") as file:
        contents = file.readlines()
    
    chapter1 = contents[52:271]
    with open("chapter1.txt", "w") as file:
        file.writelines(chapter1)


main()
