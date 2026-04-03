import csv

from tabulate import tabulate
from sys import argv, exit

if len(argv) == 2:
    filename = argv[1]
    if not filename.endswith(".csv"):
        exit("Not a CSV file")
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            print(reader)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
            

    except FileNotFoundError:
        exit("File does not exist")
elif len(argv) > 2:
    exit("Too many command-line arguments")
else:
    exit("Too few command-line arguments")