from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while True:
    choice = input("What would you like? [espresso/latte/cappucino]: ")
    if choice == "report":
        coffee_maker.report()
        continue
    else:
        menu_item = menu.find_drink(choice)
    break