from sys import argv, exit

if len(argv) == 2:
    filename = argv[1]
    if not filename.endswith(".py"):
        exit("Not a Python file")
    try:
        no_of_lines = 0
        with open(filename) as file:
            for line in file:
               if not (line.strip() == "" or line.lstrip().startswith("#")):
                   no_of_lines += 1 
    except FileNotFoundError:
        exit("File does not exist")
    print(no_of_lines)
elif len(argv) < 3:
    exit("Too few command-line arguments")
else:
    exit("Too many command-line arguments")
