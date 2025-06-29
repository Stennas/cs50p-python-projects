import random

def main():

    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except (ValueError, NameError):
            continue

    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            elif guess == number:
                print("Just right!")
                return
        except (ValueError, NameError):
            continue

main()
