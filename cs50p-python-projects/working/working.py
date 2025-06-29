import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)$"
    match = re.search(pattern, s.strip())

    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    time1 = convert_to_24hr(h1, m1, p1)
    time2 = convert_to_24hr(h2, m2, p2)

    return f"{time1} to {time2}"

    #time1 = datetime.strptime(f"{h1:02}:{m1:02} {p1}", "%I:%M %p")
    #time2 = datetime.strptime(f"{h2:02}:{m2:02} {p2}", "%I:%M %p")

    #return f'{time1.strftime("%H:%M %p")} to {time2.strftime("%H:%M %p")}'

def convert_to_24hr(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
