def calc(user_input):
    user_input = user_input.split(" ")
    x = int(user_input[0])
    y = user_input[1]
    z = int(user_input[2])

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "/":
        return x / z
    elif y == "*":
        return x * z

def main():
    expression = input("Expression: ")
    result = calc(expression)
    print(f"{result:.1f}")

main()
