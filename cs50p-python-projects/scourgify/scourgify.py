import sys
import os
import csv

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    if not sys.argv[1].endswith(".csv"):
        print(f"{sys.argv[1]} not a csv file")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    output = convert_input(sys.argv[1], sys.argv[2])
    return output

def convert_input(source_file, destination_file):
    with open(source_file, "r", newline="") as infile, open(destination_file, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(" ", 1)
            writer.writerow({
                "first":first,
                "last": " "  + last.strip(",") ,
                "house": " " + row["house"]
            })

main()
