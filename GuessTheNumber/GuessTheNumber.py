import random

scope = range(1, 11)
randomNumber = random.choice(scope)

attempts = 0
while True:
    user = int(input("Enter your guess: "))
    if user == randomNumber:
        print(f"you have guessed the correct number {randomNumber}")
        print(f"you have had {attempts} attempts")
        break
    else:
        print("you have guessed the wrong number Try again")
        attempts += 1
