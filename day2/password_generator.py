# PASSWORD GENERATOR
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total = nr_letters + nr_numbers + nr_symbols

password = ""

print(total)

i = 0

while i < total:
    r = random.randint(1, 3)

    if r == 1:
        if nr_letters != 0:
            password += random.choice(letters)
            nr_letters -= 1
        else:
            total += 1
    elif r == 2:
        if nr_numbers != 0:
            password += random.choice(numbers)
            nr_numbers -= 1
        else:
            total += 1
    elif r == 3:
        if nr_symbols != 0:
            password += random.choice(symbols)
            nr_symbols -= 1
        else:
            total += 1
   
    i += 1

print(password)

