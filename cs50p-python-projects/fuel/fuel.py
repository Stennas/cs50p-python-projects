def convert(fraction):
    try:
        x, y = fraction.split("/")
        z = round(int(x) / int(y) * 100)
        if z > 100:
            raise ValueError("Percentage exceeds 100%")
        return z
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()
