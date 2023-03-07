MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}

is_running = True


def format_money(amount):
    return "{:.2f}".format(amount)


def calculate_total_money(quarters, dimes, nickles, pennies):
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)


def receive_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return calculate_total_money(quarters, dimes, nickles, pennies)


def has_enough_money(order, money):
    menu_item_cost = MENU[order]["cost"]
    return money >= menu_item_cost


def give_change(order, money):
    menu_item_cost = MENU[order]["cost"]
    resources["money"] += menu_item_cost
    change = money - menu_item_cost
    if float(format_money(change)) > 0:
        print(f"Here is ${format_money(change)} in change.")


def get_insufficient_resource(order):
    menu_item_ingredients = MENU[order]["ingredients"]
    insufficient_resource = None

    if resources["water"] < menu_item_ingredients["water"]:
        insufficient_resource = "water"
    elif resources["coffee"] < menu_item_ingredients["coffee"]:
        insufficient_resource = "coffee"
    elif resources["milk"] < menu_item_ingredients["milk"]:
        insufficient_resource = "milk"

    return insufficient_resource


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${format_money(resources['money'])}")


def get_order():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    while order not in ["espresso", "latte", "cappuccino", "report", "off"]:
        order = input(
            "Invalid order given! What would you like? (espresso/latte/cappuccino): "
        )
    return order


def remove_resources(order):
    global resources
    menu_item_ingredients = MENU[order]["ingredients"]
    resources["water"] -= menu_item_ingredients["water"]
    resources["coffee"] -= menu_item_ingredients["coffee"]
    resources["milk"] -= menu_item_ingredients["milk"]


def complete_order(order):
    insufficient_resource = get_insufficient_resource(order)
    if insufficient_resource != None:
        print(f"Sorry, there is not enough {insufficient_resource}.")
    else:
        given_money = receive_money()
        enough_money_given = has_enough_money(order, given_money)
        if not enough_money_given:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            remove_resources(order)
            give_change(order, given_money)
            print(f"Here is your {order} ☕ Enjoy!")


def run():
    order = get_order()
    global is_running
    if order in ["espresso", "latte", "cappuccino"]:
        complete_order(order)
    elif order == "report":
        print_report()
    elif order == "off":
        is_running = False


while is_running:
    run()
