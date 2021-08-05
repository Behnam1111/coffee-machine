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
    choice = input(msg)
    if choice == "off":
        turn_off_the_machine()
    elif choice == "report":
        print_report()
    elif choice == "espresso" or "latte" or "cappuccino":
        make_coffee(choice)

    return choice


def print_report():
    print("'water': {}, 'milk': {}, 'coffee': {}, 'Money':{}".format(resources["water"], resources["milk"],
                                                                     resources["coffee"], cost))
    get_input_from_user("What would you like? (espresso/latte/cappuccino):")


def turn_off_the_machine():
    return 0


def check_resource_sufficient(coffee_type):
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        return True


def process_coin(quarters, dimes, nickles, pennies):
    amount = quarters * 0.25 + dimes * 0.01 + nickles * 0.05 + pennies * 0.01
    return amount


def check_transaction_successful(amount, coffee_type):
    if amount < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    if amount > MENU[coffee_type]["cost"]:
        change = amount - MENU[coffee_type]["cost"]
        print("Here is ${} in charge.".format(change))
        return True
    if amount == MENU[coffee_type]["cost"]:
        return True


def make_coffee(choice):
    coffee_type = choice
    if check_resource_sufficient(coffee_type):
        quarters_amount = input("how many quarters?")
        dimes_amount = input("how many dimes?")
        nickles_amount = input("how many nickles?")
        pennies_amount = input("how many pennies?")
        amount = process_coin(quarters_amount, dimes_amount, nickles_amount, pennies_amount)
        if check_transaction_successful(amount, coffee_type):
            print("“Here is your {}. Enjoy!".format(coffee_type))


def start():
    get_input_from_user("What would you like? (espresso/latte/cappuccino):")


start()
