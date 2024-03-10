
from decimal import Decimal
from typing import Callable, List

class Calculation:
    def __init__(self, operands: List[Decimal], operation: Callable[[List[Decimal]], Decimal]):
        self.operands = operands
        self.operation = operation

    @staticmethod
    def create(operands: List[Decimal], operation: Callable[[List[Decimal]], Decimal]):
        return Calculation(operands, operation)

    def perform(self) -> Decimal:
        return self.operation(self.operands)

    def __repr__(self):
        operands_str = ', '.join(map(str, self.operands))
        return f"Calculation({operands_str}, {self.operation.__name__})"
