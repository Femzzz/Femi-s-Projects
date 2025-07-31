import random
#Number Guessing Game

guess = ""
number = random.randint(1, 100)

while guess != number:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print("You got it!")
    except ValueError:
        print("Please enter a valid number.")