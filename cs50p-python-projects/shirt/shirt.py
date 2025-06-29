import sys, os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    valid_ext = [".jpeg",".jpg",".png"]

    if ext1 not in valid_ext or ext2 not in valid_ext:
        print("Invalid input")
        sys.exit(1)

    if ext1 != ext2:
        print("Input and output have different extensions")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print(f"'{sys.argv[1]}' not found")
        sys.exit(1)

    if not os.path.exists("shirt.png"):
        print("shirt.png not found")
        sys.exit(1)

    modify_input(sys.argv[1], sys.argv[2])

def modify_input(input_file, output_file):
    size = (600, 600)
    with Image.open(input_file) as person_img:
        person_img = ImageOps.fit(person_img, size)
        with Image.open("shirt.png") as shirt_img:
            shirt_img = shirt_img.resize(person_img.size)
            person_img.paste(shirt_img, (0, 0), shirt_img)
        person_img.save(output_file)

main()
