userList = []
while True:
    user = input("Enter an item: ")
    if user != "done":
        userList.append(user)
    else:
        for item in sorted(userList):
            print(item)
        break
