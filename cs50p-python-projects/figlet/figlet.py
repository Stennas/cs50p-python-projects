import sys
import pyfiglet

def main():
    if len(sys.argv) == 1:
        font = None
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        font = sys.argv[2]
    else:
        print("Usage: python figlet.py [-f FONT]")
        sys.exit(1)

    text = input("Input: ")
    try:
        if font:
            ascii_art = pyfiglet.figlet_format(text, font=font)
        else:
            ascii_art = pyfiglet.figlet_format(text)

    except pyfiglet.FontNotFound:
        print(f"Font '{font}' not found.")
        sys.exit(1)
    print(ascii_art)

    
main()
