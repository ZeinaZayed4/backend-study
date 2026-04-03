import csv

from sys import argv, exit

if len(argv) == 3:
    in_file = argv[1]
    out_file = argv[2]
    if not in_file.endswith(".csv"):
        exit("Not a CSV file")
    try:
        with open(in_file) as f1, open(out_file, "w") as f2:
            reader = csv.DictReader(f1)
            writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
    except FileNotFoundError:
        exit(f"Could not read {in_file}")
elif len(argv) > 3:
    exit("Too many command-line arguments")
else:
    exit("Too few command-line arguments")