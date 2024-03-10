from decimal import Decimal

def get_user_input():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = user_input.split()
    decimals = [Decimal(number) for number in numbers]
    return decimals
