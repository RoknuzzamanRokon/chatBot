with open("output.txt", "r") as file:
    count = file.read()

    words = count.split()

    number_of_word = len(words)

    print(number_of_word)