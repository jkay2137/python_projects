print("Welcome to the tip calculator.")

bill = float(input("What is your bill? $"))

tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

result = round((bill + (bill * tip / 100)) / people, 2)

print(f"Each person should pay: ${result}")
