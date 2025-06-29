def main():
    meal_time = input("What time is it? ")
    result = convert(meal_time)

    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = map(float, time.split(":"))
    final = hours + minutes / 60
    return final


if __name__ == "__main__":
    main()
    
