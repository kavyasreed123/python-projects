import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 45,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 40,
    },
    "horlicks": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "horlicks":22,
        },
        "cost": 25,
    },
    "boost": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "horlicks":22,
        },
        "cost": 25,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "horlicks": 50,
    "boost": 50
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many ₹2 coins?: ")) * 5
    total += int(input("how many ₹5 coins?: ")) * 3
    total += int(input("how many ₹5 coins?: ")) * 4
    total += int(input("how many ₹10 coins?: ")) * 5
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources and inform the user about the preparation."""
   # preparation_time = 0
    print("Order accepted...")
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
       # preparation_time += order_ingredients[item]
    print(f"Making your {drink_name}...")
   # time.sleep()
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso(₹50)/latte(₹45)/cappuccino(₹60)/horlicks(₹25)/boost(₹25)): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Horlicks:{resources['horlicks']}g")
        print(f"Boost:{resources['boost']}g")
        print(f"Money: ₹{profit}")
    elif choice not in MENU:
        print("Sorry, that drink is not available. Please choose from the available options like...(espresso/latte/cappuccino/horlicks/boost).")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])