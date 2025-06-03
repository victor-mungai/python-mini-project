dictionary = {}
for i in range(1, 6):
    user_name = input("Enter the name: ")
    user_number = input("Enter the number: ")
    dictionary.update({user_name: user_number})
while True:
    user_name = input("Enter the name: ")
    number = dictionary[user_name]
    print(f"The number is {number}")
    option = input("Would you like to continue? (y/n): ")
    if option == "n":
        break
    else:
        continue