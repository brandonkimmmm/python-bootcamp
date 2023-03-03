from art import logo
from replit import clear


def calculate(x, y, op):
    """Perform math calcuation x op y and return value"""
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    else:
        return x / y


def get_input_and_calculate(x=None):
    """Recursive function that gets calculation inputs from user, performs calculation, and calls self with result"""

    first_number = x
    if first_number == None:
        first_number = float(input("What's the first number?: "))
        print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = calculate(first_number, second_number, operation)

    print(f"{first_number} {operation} {second_number} = {result}")

    use_prev_val = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
    )

    if use_prev_val == "y":
        get_input_and_calculate(result)
    else:
        clear()
        get_input_and_calculate()


print(logo)

get_input_and_calculate()
