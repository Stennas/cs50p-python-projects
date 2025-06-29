def main():
    groceries = []
    try:
        while True:
            #collect user input, and add to a list, until CONTROL-D is pressed
            item = input("").upper()
            groceries.append(item)
    except EOFError:
        #count unique items
        counts = {}
        for grocery in groceries:
            if grocery in counts:
                counts[grocery] += 1
            else:
                counts[grocery] = 1

        #sort items alphabetically and print with count(s)
        for item in sorted(counts):
            print(f"{counts[item]} {item}")


main()
