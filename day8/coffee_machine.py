# Coffee Machine Program
import machine


con = True
change = 0


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
    return result


def check_coins(choice):
    global change
    coins = count_coins()
    
    if choice == "cappucino":
        if coins < machine.MENU["cappucino"]["cost"]:
            add_resources(choice)
            return False
        else:
            change = coins - machine.MENU["cappucino"]["cost"]
            machine.resources["coins"] += machine.MENU["cappucino"]["cost"]
            return True
    elif choice == "espresso":
        if coins < machine.MENU["espresso"]["cost"]:
            add_resources(choice)
            return False
        else:
            change = coins - machine.MENU["espresso"]["cost"]
            machine.resources["coins"] += machine.MENU["espresso"]["cost"]
            return True
    elif choice == "latte":
        if coins < machine.MENU["latte"]["cost"]:
            add_resources(choice)
            return False
        else:
            change = coins - machine.MENU["latte"]["cost"]
            machine.resources["coins"] += machine.MENU["latte"]["cost"]
            return True

def check_resources(choice):
    if choice == "cappucino":
        if ((machine.resources["water"] - machine.MENU["cappucino"]["water"] < 0) 
        and (machine.resources["milk"] - machine.MENU["cappucino"]["milk"] < 0)
        and (machine.resources["coffee"] - machine.MENU["cappucino"]["coffee"] < 0)):
            return False
        else:
            machine.resources["water"] -= machine.MENU["cappucino"]["water"]
            machine.resources["milk"] -= machine.MENU["cappucino"]["milk"]
            machine.resources["coffee"] -= machine.MENU["cappucino"]["coffee"]
            return True
    elif choice == "espresso":
        if ((machine.resources["water"] - machine.MENU["espresso"]["water"] < 0) 
        and (machine.resources["milk"] - machine.MENU["espresso"]["milk"] < 0)
        and (machine.resources["coffee"] - machine.MENU["espresso"]["coffee"] < 0)):
            return False
        else:
            machine.resources["water"] -= machine.MENU["espresso"]["water"]
            machine.resources["milk"] -= machine.MENU["espresso"]["milk"]
            machine.resources["coffee"] -= machine.MENU["espresso"]["coffee"]
            return True
    elif choice == "latte":
        if ((machine.resources["water"] - machine.MENU["latte"]["water"] < 0) 
        and (machine.resources["milk"] - machine.MENU["latte"]["milk"] < 0)
        and (machine.resources["coffee"] - machine.MENU["latte"]["coffee"] < 0)):
            return False
        else:
            machine.resources["water"] -= machine.MENU["latte"]["water"]
            machine.resources["milk"] -= machine.MENU["latte"]["milk"]
            machine.resources["coffee"] -= machine.MENU["latte"]["coffee"]
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
        return f"Sorry there is not enough resources."


while con:
    choice = input("What would you like? [espresso/latte/cappucino]: ").lower()
    if choice == "report":
        show_raport()
        continue
    elif choice == "off":
        con = False
    else:
        print(make_coffee(choice))