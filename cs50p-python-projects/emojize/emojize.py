from emoji import emojize

def main():
    user_input = input("Input: ").strip()
    output = emojize(user_input, language='alias')
    print("Output:", output)

main()
