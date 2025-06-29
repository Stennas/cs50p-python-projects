def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    while True:
        try:
            date = input("Date: ")
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            try:
                month_day, year = date.split(",")
                year = int(year.strip())
                month, day = month_day.strip().split(" ")
                month = months[month.capitalize()]
                day = int(day)
            except (KeyError, ValueError):
                continue
        if 1 <= month <= 12 and 1 <= day <= 31:
                break

    print(f"{year}-{month:02}-{day:02}")

main()
