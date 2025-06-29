import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line argument")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)

    print(read_and_tabulate(sys.argv[1]))

def read_and_tabulate(file_path):
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)
        return tabulate(data[1:], headers=data[0], tablefmt="grid")

main()
