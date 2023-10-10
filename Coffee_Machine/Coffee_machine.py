from Coffee_machine_data import MENU, logo, resources
import time
money = 0


def modify_report(input):
    """To modify the resources"""
    water = input['water']
    milk = input['milk']
    coffee = input['coffee']
    return f"🧴 water: {water}ml\n🧂 milk: {milk}ml\n☕ coffee: {coffee}g"


def resources_sufficient(drink):
    """To check whether the ingredient resources are Sufficient"""
    for item in drink:
        if resources[item] < drink[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """To calculate the payment"""
    print("Please make payment through Coins?")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(payment, drink):
    """Checking if the payment is successful"""
    global money
    if payment >= drink:
        money += drink
        change = round(payment - drink, 2)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(order, drink):
    """Calculating the resources remainder"""
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {order} ☕️. Enjoy!")


def coffee_machine():
    print("                                           Gabi_Coffee_Machine                                      ")
    print(logo)
    should_continue = True
    print("Type 'report' if you want to know how many resources remaining and 'off' to off the machine ")
    time.sleep(0.5)
    while should_continue:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == 'report':
            print(modify_report(resources))
            print(f"💰 money: ${money}")
        elif order == 'off':
            should_continue = False
        else:
            drink = MENU[order]
            if resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if transaction_successful(payment, drink["cost"]):
                    make_coffee(order, drink["ingredients"])
coffee_machine()