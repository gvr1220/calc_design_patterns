'''

This Python code defines a Calculator class that provides a simple interface for performing arithmetic operations (addition, subtraction, multiplication, division) on Decimal numbers. The class uses static methods, demonstrating a functional approach within an object-oriented context.

'''

from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def _perform_operation(operation: Callable[..., Decimal], *operands: Decimal) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(*operands, operation=operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(*operands: Decimal) -> Decimal:
        return Calculator._perform_operation(add, *operands)

    @staticmethod
    def subtract(*operands: Decimal) -> Decimal:
        return Calculator._perform_operation(subtract, *operands)

    @staticmethod
    def multiply(*operands: Decimal) -> Decimal:
        return Calculator._perform_operation(multiply, *operands)

    @staticmethod
    def divide(*operands: Decimal) -> Decimal:
        return Calculator._perform_operation(divide, *operands)
