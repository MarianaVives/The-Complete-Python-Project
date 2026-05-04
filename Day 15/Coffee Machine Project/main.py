import art

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def print_intro():
    print(art.logo)
    print("Welcome to the coffee machine app ☕🥧🧸💭🥐🥛🍵. Please make your order. ")

def are_there_enough_resources(ingredients):
    """Returns True if there are enough ingredients for the coffee"""
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def get_report():
    """Print report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {profit}$")

def process_payment(total_to_pay):
    """Returns the total of the sum of the coins inserted to the machine"""
    print(f"The total of your order is : {total_to_pay}")
    print(f"Please insert your coins.")
    total_payed = 0
    total_payed += int(input("How many quarters ?")) * 0.5
    total_payed += int(input("How many dimes ?")) *0.1
    total_payed += int(input("How many nickles ?")) * 0.05
    total_payed += int(input("How many pennies ?")) * 0.01
    return total_payed

def is_payment_complete(total_payed, beverage_price):
    """Returns true if payment is completed and gives back change. If payment was not completed returns false"""
    if total_payed >= beverage_price:
        change = total_payed - beverage_price
        change_two_dec = "{:.2f}".format(change)
        global profit
        profit += beverage_price
        print(f"Take your change: {change_two_dec}")
        return True
    elif total_payed < beverage_price:
        print("You have not inserted enough coins to complete the payment. Transaction cancelled")
        return False
    else:
        print("Invalid input")
        return None

def select_your_options():
    """Selects an option. Options: 'off' to turn off the machine, 'report' to print a report, and 'espresso/latte/cappuccino'."""
    beverage_choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    drink = MENU[beverage_choice]
    if beverage_choice == "off":
        return beverage_choice
    if beverage_choice == "report":
        return get_report()
    if are_there_enough_resources(drink["ingredients"]):
        beverage_price = float(drink["cost"])
        process_payment(beverage_price)
    else:
        print(f"Sorry, cannot prepare you {beverage_choice}. Choose a different beverage.")
    return None

def deduct_resources(drink_ingredients):
    """Removes consumed resources from the resources list and returns updated resources"""
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]

def prepare_coffee(drink, drink_ingredients):
    """Prepares the coffee and calls the deduct_resources function"""
    print("Preparing your coffee... ")
    deduct_resources(drink_ingredients)
    print(f"Here is your {drink} ☕")
    print(art.coffee)

def order_a_coffee():
    """Allows the user to order a coffee, chose how to pay. If the coffee resources are not enough allows the user to repeat the process."""
    turn_off = False
    while not turn_off:
        print_intro()
        beverage_choice = input("What would you like? (espresso/latte/cappuccino)").lower()
        if beverage_choice == "off":
            turn_off = True
            return turn_off
        if beverage_choice == "report":
            return get_report()
        drink = MENU[beverage_choice]
        if are_there_enough_resources(drink["ingredients"]):
            beverage_price = float(drink["cost"])
            total_payed = process_payment(beverage_price)
            if is_payment_complete(total_payed, beverage_price):
                prepare_coffee(beverage_choice, drink["ingredients"])
        else:
            print(f"Sorry, there are not enough resources to prepare you {beverage_choice}. Choose a different beverage.")

order_a_coffee()