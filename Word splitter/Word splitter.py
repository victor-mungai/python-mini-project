while True:
    sentence = input("Please enter a sentence: ")
    words = sentence.split()
    largestWord = ""
    shortestWord = ""
    for word in words:
        if len(word) > len(largestWord):
            largestWord = word
        elif len(word) < len(largestWord):
            shortestWord = word
    print(f"The largest word is: {largestWord}")
    print(f"The shortest word is: {shortestWord}")
    print(f"The total number of words is: {len(words)}")
    print("##############################################")
    option = input("Would you like to continue? (y/n): ")
    print()
    if option == "n":
        break
    else:
        continue