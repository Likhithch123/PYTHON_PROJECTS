# Calculator App
# Functions
# Add,Sub,Mult,Div

from art import logo
from os import system


def add_nums(n1, n2):
    return n1 + n2


def sub_nums(n1, n2):
    return n1 - n2


def mult_nums(n1, n2):
    return n1 * n2


def div_nums(n1, n2):
    return n1 / n2


operations_dict = {"+": add_nums, "-": sub_nums, "*": mult_nums, "/": div_nums}


def calculator():
    print(logo)
    num1 = float(input("Enter the first number?\n"))
    for symbol in operations_dict:
        print(symbol)
    operation = input(
        "What operation you need to perform (pick one from the above operations)?\n"
    )
    num2 = float(input("Enter the second number?\n"))
    calculation_function = operations_dict[operation]
    result = calculation_function(num1, num2)
    print(f"{operation} of {num1} and {num2} is {result}.")

    calculator_active = True
    while calculator_active:
        should_continue = input(
            f"Type 'yes' if you want to continue calculation with {result} else type 'no'.Type 'new' if you want to carry out a new calculation.\n"
        ).lower()
        if should_continue == 'yes':
            operation = input("Pick a operation from the above operations.\n")
            next_num = int(input("What's the next number?\n"))
            calculation_function = operations_dict[operation]
            answer = calculation_function(result, next_num)
            print(f"{operation} of {result} and {next_num} is {answer}")
        elif should_continue == 'new':
            calculator_active = False
            system('cls')
            calculator()
        else:
            calculator_active = False


calculator()
