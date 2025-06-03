while True:
    word = input("Enter the word: ")
    if word == (word[::-1]):
        print(f"The word  {word} is palindrome with {(word[::-1])}")
        option = input("Would you like to continue? (y/n): ")

    else:
        print(f"The word  {word} is not palindrome with {(word[::-1])}")
        option = input("Would you like to continue? (y/n): ")

    if option == "n":
        break
    else:
        continue