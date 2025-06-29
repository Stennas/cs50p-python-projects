def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        #first two characters must be letters
        if not s[:2].isalpha():
            return False
        
        #check length
        if not (2 <= len(s) <= 6):
            return False

        #only letters and numbers allowed
        if not s.isalnum():
            return False

        #numbers must be at the end and cannot start with 0
        number_started = False
        for char in s:
            if char.isdigit():
                if not number_started:
                    number_started = True
                    if char == "0":
                        return False
            elif number_started:
                return False

        return True

if __name__ == "__main__":
    main()
