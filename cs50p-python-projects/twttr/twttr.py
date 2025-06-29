def main():
    texts = input("Input: ")
    print(f"Output: {shorten(texts)}")

def shorten(word):
    result = ""
    for new_word in word:
        if new_word.upper() not in  ["A", "E", "I", "O", "U"]:
            result += new_word
    return result

if __name__ == "__main__":
    main()
