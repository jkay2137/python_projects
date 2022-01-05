import art
import os

print(art.logo)
print("Welcome to the secet auction program.")

clear = lambda: os.system("clear") # Clearing function?

while True:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bidders = input("Are there any other bidders? [Y/n]\n").lower()

    if bidders != "y" or bidders != "":
        break

clear()
       