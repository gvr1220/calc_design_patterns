from app.commands.operation_command import OperationCommand
from calculator.operations import add


class AddCommand(OperationCommand):
    def __init__(self):
        super().__init__(add)