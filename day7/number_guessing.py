# Guessing Number Game
import random

guessing_number = random.randint(1, 100)
hard_mode = 5
easy_mode = 10
i = 0

def compare():
    if guess > guessing_number:
        return "Too high."
    elif guess < guessing_number:
        return "Too low."
    else:
        return f"You got it! The guessing number was {guessing_number}."

print("I'm thinking about the number between 1 and 100.")
choice = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()

if choice == "hard":
    guess = 0
    while guess != guessing_number and i < hard_mode:
        print(f"You have {hard_mode - i} attempts remaining.")
        guess = int(input("Make a guess: "))
        print(compare())
        i += 1
elif choice == "easy":
    guess = 0
    while guess != guessing_number and i < easy_mode: 
        print(f"You have {easy_mode - i} attempts remaining.")
        guess = int(input("Make a guess: "))
        print(compare())
        i += 1

if guess != guessing_number:
    print("You run out of guesses. You lose!")