import random
number = random.randint(1, 10)
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")