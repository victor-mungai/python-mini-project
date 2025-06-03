numbers = []
odds = 0
evens = 0
for i in range(1,11):
    user = input(f"enter number no {i}: ")
    numbers.append(int(user))
for number in numbers:
    if number % 2 == 0:
        evens += 1
    else:
        odds += 1
print(f"The number of odds is: {odds}")
print(f"The number of evens is: {evens}")
