from coffee_machine_menu import Menu, logo
from coffee_machine_maker import CoffeeMaker
from coffee_machine_money import MoneyMachine
import time


def coffee_machine():
    should_continue = True
    resources = CoffeeMaker()
    money = MoneyMachine()
    location = Menu()
    print("                                           Gabi_Coffee_Machine                                      ")
    print(logo)
    print("Type 'report' if you want to know how many resources remaining and 'off' to off the machine ")
    while should_continue:
        time.sleep(0.5)
        options = location.get_items()
        order = input(f"What would you like? {options}: ").lower()
        if order == 'report':
            resources.report()
            money.report()
        elif order == 'off':
            should_continue = False
        else:
            drink = location.find_drink(order)
            if resources.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                resources.make_coffee(drink)


coffee_machine()