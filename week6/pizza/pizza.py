import sys
import csv
from tabulate import tabulate

args = []
for _ in sys.argv:
    args.append(_)

if len(args) < 2:
    sys.exit("Too few command-line arguments")
elif len(args) > 2:
    sys.exit("Too many command-line arguments")
elif args[1].endswith(".csv") != True:
    sys.exit("Not a CSV file")
else:
    file_name = args[1]
    rows = []
    with open(f"{file_name}") as file:
        try:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
            print(tabulate(rows,headers ="keys",tablefmt = "grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")