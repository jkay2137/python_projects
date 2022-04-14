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

    result = quarter * machine.COINS["quarter"] + dimes * machine.COINS["dime"] + nickles * machine.COINS["nickel"] + pennies * machine.COINS["penny"]
    return result


def check_coins(choice):
    global change
    coins = count_coins()
    
    if choice == "cappucino":
        if coins < machine.MENU["cappucino"]["cost"]:
            return False
        else:
            change = coins - machine.MENU["cappucino"]["cost"]
            machine.resources["coins"] += machine.MENU["cappucino"]["cost"]
            return True
    elif choice == "espresso":
        if coins < machine.MENU["espresso"]["cost"]:
            return False
        else:
            change = coins - machine.MENU["espresso"]["cost"]
            machine.resources["coins"] += machine.MENU["espresso"]["cost"]
            return True
    elif choice == "latte":
        if coins < machine.MENU["latte"]["cost"]:
            return False
        else:
            change = coins - machine.MENU["latte"]["cost"]
            machine.resources["coins"] = machine.MENU["latte"]["cost"]
            return True

        

while con:
    choice = input("What would you like? [espresso/latte/cappucino]: ").lower()
    if choice == "report":
        show_raport()
        continue