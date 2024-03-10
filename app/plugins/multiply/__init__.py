from app.commands.operation_command import OperationCommand
from calculator.operations import multiply
class MultiplyCommand(OperationCommand):
    def __init__(self):
        super().__init__(multiply)
