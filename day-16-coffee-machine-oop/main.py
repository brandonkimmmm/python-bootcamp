from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_running = True


def get_report():
    coffee_maker.report()
    money_machine.report()


def stop_running():
    global is_running
    is_running = False


def complete_order(order):
    item = menu.find_drink(order)
    if (
        item is not None
        and coffee_maker.is_resource_sufficient(item)
        and money_machine.make_payment(item.cost)
    ):
        coffee_maker.make_coffee(item)


def run():
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "report":
        get_report()
    elif order == "off":
        stop_running()
    else:
        complete_order(order)


while is_running:
    run()
