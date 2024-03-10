from app.commands import Command
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal
from calculator.input_handler import get_user_input
import logging

class OperationCommand(Command):
    def __init__(self, operation_function):
        self.operation_function = operation_function
        self.logger = logging.getLogger(__name__)

    def execute(self):
        try:
            operands = get_user_input()
            result = self.operation_function(*operands)
            calculation = Calculation.create(operands, self.operation_function)
            Calculations.add_calculation(calculation)
            self.logger.info("Performed operation: {}({}) = {}".format(
                self.operation_function.__name__, operands, result))
            print("The result of {} operation is {}".format(self.operation_function.__name__, result))
        except ValueError as e:
            self.logger.error(str(e))
            print(e)
            print("Please enter a non-zero divisor.")