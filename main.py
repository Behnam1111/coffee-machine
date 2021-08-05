MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}
cost = 0


def get_input_from_user(msg):
    """returns choice that user made"""
    choice = input(msg)
    if choice == "off":
        turn_off_the_machine()
    elif choice == "report":
        print_report()
    elif choice == "espresso" or "latte" or "cappuccino":
        make_coffee(choice)

    return choice


def print_report():
    """prints report of resources"""
    print(f"'water':{resources['water']}")
    print(f"'milk':{resources['milk']}")
    print(f"'coffee':{resources['coffee']}")


def turn_off_the_machine():
    """finish the process"""
    return 0


def if_resource_sufficient(coffee_resource):
    """returns true if resource is sufficient and false if resource is not."""
    for item in coffee_resource:
        if resources[item] < coffee_resource[item]:
            print("Sorry there is not enough water.")
            return False
        return True


def process_coin():
    """returns amount of money deducted from coins"""
    quarters_amount = input("how many quarters?")
    dimes_amount = input("how many dimes?")
    nickles_amount = input("how many nickles?")
    pennies_amount = input("how many pennies?")
    amount = int(quarters_amount) * 0.25 + int(dimes_amount) * 0.01 + int(nickles_amount) * 0.05 + int(
        pennies_amount) * 0.01
    return amount


def is_transaction_successful(amount, coffee_type):
    """return True if transaction is true and False if transaction has failed."""
    if amount < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if amount >= MENU[coffee_type]["cost"]:
        change = round(amount - MENU[coffee_type]["cost"], 2)
        global cost
        cost += change
        for item in MENU[coffee_type]["ingredients"]:
            resources[item] -= MENU[coffee_type]["ingredients"][item]
        print(f"Here is ${change} in charge.")
        return True


def make_coffee(choice):
    if if_resource_sufficient(MENU[choice]["ingredients"]):
        amount = process_coin()
        if is_transaction_successful(amount, choice):
            print("“Here is your {}. Enjoy!".format(choice))
            print_report()
    get_input_from_user("What would you like? (espresso/latte/cappuccino):")


get_input_from_user("What would you like? (espresso/latte/cappuccino):")
