from datetime import date
import sys
import inflect


def main():
    print(convert_to_minutes(input("Date of Birth: ")))


def convert_to_minutes(dob):
    try:
        dob = date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid format")

    today = date.today()
    difference = today - dob
    minutes = difference.days * 24 * 60
    return convert_to_words(minutes)


def convert_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"

if __name__ == "__main__":
    main()
