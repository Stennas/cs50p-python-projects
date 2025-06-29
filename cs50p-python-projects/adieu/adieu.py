def main():
    names = []
    try:
        while True:
            user_input = input("Name: ").strip()
            if user_input:
                names.append(user_input.title())
    except EOFError:
        print()  # For clean newline after Ctrl+D

    print(f"Adieu, adieu, to {format_names(names)}.")

def format_names(name):
    if len(name) == 1:
        return name[0]
    elif len(name) == 2:
        return " and ".join(name)
    else:
        return ", ".join(name[:-1]) + ", and " + name[-1]

# This program handles user input until EOF (Ctrl+D) is received.
# Although the problem hints may suggest typing "Control-D" as input to stop the loop,
# the actual CS50 test suite expects the program to exit cleanly when the user
# presses Ctrl+D (which raises an EOFError).
# Therefore, we use a try/except block to catch EOFError and exit gracefully.

main()
