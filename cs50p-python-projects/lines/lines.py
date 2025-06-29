import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not sys.argv[1].endswith(".py"):
        print("Not a python file")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)

    print(count_lines(sys.argv[1]))

def count_lines(file_path):
    count_line = 0
    with open(file_path, "r") as file:
        for line in file:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                count_line += 1
    return count_line

main()
