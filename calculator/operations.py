from decimal import Decimal

def add(*operands: Decimal) -> Decimal:
    return sum(operands, Decimal(0))

def subtract(*operands: Decimal) -> Decimal:
    result = operands[0]
    for operand in operands[1:]:
        result -= operand
    return result

def multiply(*operands: Decimal) -> Decimal:
    result = operands[0]
    for operand in operands[1:]:
        result *= operand
    return result

def divide(*operands: Decimal) -> Decimal:
    result = operands[0]
    for operand in operands[1:]:
        if operand == 0:
            raise ValueError("Cannot divide by zero")
        result /= operand
    return result


