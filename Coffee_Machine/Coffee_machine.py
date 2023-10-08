from Coffee_machine_data import logo, resources, MENU
import time


money = 0
def modify_report(input):
    water = input['water']
    milk = input['milk']
    coffee = input['coffee']
    return f"\n🚰 water: {water}ml \n🥛 milk: {milk}ml \n☕ coffee: {coffee}g"


def resource_sufficient(drink):
    """To check if there are enough resources for the drink we want to purchase"""
    for item in drink:
        if resources[item] < drink[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coin():
    """Payment through Coins"""
    print("Please pay through coins: ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(payment, drink):
    """To check for cost transaction"""
    for item in drink:
        if payment < drink["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            break
        elif payment > drink["cost"]:
            change = round(payment - drink["cost"], 2)
            if change > 0:
                global money
                money += drink["cost"]
                print(f"Here is ${change} dollars in change.")
            else:
                print("No change is needed.")
            payment = drink["cost"]


def make_coffee(order, drink):
    """To deduct the drink item from the resources item so it could be deducted
    to calculate the next drink"""
    for item in drink:
            resources[item] -= drink[item]
    print(f"Here is your {order} ☕️. Enjoy!")


def coffee_machine():
    should_continue = True
    print("                                         Gabi Coffee Machine                                 ")
    print(logo)
    print("To get the report of the remains, you could type Report likewise to off the machine is off")
    time.sleep(1)
    print(" ")
    while should_continue:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == 'report':
            print(modify_report(resources))
            print(f"💰 money: ${money}")
        elif order == 'off':
            should_continue = False
        else:
            drink = MENU[order]
            if resource_sufficient(drink["ingredients"]):
                payment = process_coin()
                transaction_successful(payment, drink)
                make_coffee(order, drink["ingredients"])
coffee_machine()