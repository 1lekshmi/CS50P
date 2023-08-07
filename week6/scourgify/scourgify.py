import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            new_entries = []
            for line in reader:
                lname,fname = line["name"].split(",")
                house = line["house"]
                new_entries.append({"first":fname.strip(), "last":lname, "house":house})

        with open(f"{sys.argv[2]}", "w") as new:
            writer = csv.DictWriter(new, fieldnames=["first","last","house"])
            writer.writeheader()
            for row in new_entries:
                writer.writerow(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")