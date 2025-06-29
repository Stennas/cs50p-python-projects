def main():
    camelCase = input("camelCase: ")
    snake_case = convert(camelCase)
    print(f"snake_case: {snake_case}")

def convert(texts):
    result = ""
    for text in texts:
        if text.isupper():
            if result:
                result += "_"
            result += text.lower()
        else:
            result += text
    return result

main()
