from app.commands.operation_command import OperationCommand
from calculator.operations import divide

class DivideCommand(OperationCommand):
    def __init__(self):
        super().__init__(divide)
