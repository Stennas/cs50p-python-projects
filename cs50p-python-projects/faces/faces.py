def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

def main():
    user_reply = input("How are you doing today? ")
    result = convert(user_reply)
    print(result)

main()


