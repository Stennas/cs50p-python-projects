from validator_collection import validators

def main():
    try:
        validators.email(input("What is your email? "))
        print("Valid")
    except ValueError:
        print("Invalid")


main()
