import art
import os

print(art.logo)
print("Welcome to the secet auction program.")

clear = lambda: os.system("clear") # Clearing function?

bidders = {}
highest = 0
winner = ""

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    choice = input("Are there any other bidders? [Y/n]\n").lower()

    bidders[name] = bid

    if choice != "y" and choice != "":
        break
    clear()

clear()

for key in bidders:
    if bidders[key] > highest:
        highest = bidders[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest}.")