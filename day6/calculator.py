import os
from art import logo

clear = lambda: os.system("clear")

def count(first_number, next_number, operation):
    if operation == "+":
        return first_number + next_number
    elif operation == "-":
        return first_number - next_number
    elif operation == "*":
        return first_number * next_number
    elif operation == "/":
        return first_number / next_number
    else:
        return 0

to_continue = True

print(logo)

while to_continue:
    first_number = float(input("What's the first number?: "))
    while True:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        
        if operation == "/" and first_number == 0:
            print("Do not divide by zero!!!")
        else:
            result = count(first_number, next_number, operation)
            print(f"{first_number} {operation} {next_number} = {result}")

        choice = input(f"Type \"y\" to continue calculationg with {result}, type \"n\" to start a new calculation, or type \"exit\" to exit: ").lower()

        if choice == "y":
            first_number = result
            continue
        elif choice == "n":
            clear() 
            break
        elif choice == "exit":
            print("Goodbye!")
            to_continue = False
            break
        else:
            print("Wrong option.\nApplication exit.")
            to_continue = False
            break

            