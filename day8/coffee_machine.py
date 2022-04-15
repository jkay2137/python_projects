# Coffee Machine Program
import machine

con = True
change = 0
not_enough = ""

def show_raport():
    print(f"Water: {machine.resources['water']}")
    print(f"Milk: {machine.resources['milk']}")
    print(f"Coffee: {machine.resources['coffee']}")
    print(f"Coins: {machine.resources['coins']}")

def count_coins():
    quarters = int(input("How many quarters?: "))    
    dimes = int(input("How many dimes?: ")) 
    nickles = int(input("How many nickles?: ")) 
    pennies = int(input("How many pennies?: "))

    result = quarters * machine.COINS["quarter"] + dimes * machine.COINS["dime"] + nickles * machine.COINS["nickel"] + pennies * machine.COINS["penny"]
    return round(result, 2)


def check_coins(choice):
    global change
    coins = count_coins()
    
    if coins < machine.MENU[choice]["cost"]:
        add_resources(choice)
        return False
    else:
        change = coins - machine.MENU[choice]["cost"]
        machine.resources["coins"] += machine.MENU[choice]["cost"]
        return True
    

def check_resources(choice):
    global not_enough
    if machine.resources["water"] - machine.MENU[choice]["water"] < 0:
        not_enough = "water"
        return False
    elif machine.resources["milk"] - machine.MENU[choice]["milk"] < 0:
        not_enough = "milk"
        return False
    elif machine.resources["coffee"] - machine.MENU[choice]["coffee"] < 0:
        not_enough = "coffee"
        return False
    else:
        machine.resources["water"] -= machine.MENU[choice]["water"]
        machine.resources["milk"] -= machine.MENU[choice]["milk"]
        machine.resources["coffee"] -= machine.MENU[choice]["coffee"]
        return True

def add_resources(choice):
    machine.resources["coffee"] += machine.MENU[choice]["coffee"]
    machine.resources["milk"] += machine.MENU[choice]["milk"]
    machine.resources["water"] += machine.MENU[choice]["water"]

def make_coffee(choice):
    global change
    text = ""
    if check_resources(choice) == True:
        if check_coins(choice) == True:
            if change > 0:
                text += f"Here is ${change} dollars in change.\n"
            text += f"“Here is your {choice}. Enjoy!"
            return text
        else:
            return f"Sorry that's not enough money. Money refunded."
    else:
        return f"Sorry there is not enough {not_enough}."


while con:
    choice = input("What would you like? [espresso/latte/cappucino]: ").lower()
    if choice == "report":
        show_raport()
        continue
    elif choice == "off":
        con = False
    else:
        print(make_coffee(choice))