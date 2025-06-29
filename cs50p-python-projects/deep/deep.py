def main():
    answer = input("What is the answer to The Great Question of Life, The Universe and Everything? ").lower()

    match answer:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

main()
