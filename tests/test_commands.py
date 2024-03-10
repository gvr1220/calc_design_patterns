"""
Module docstring: This module contains unit tests for the App class and its commands.
"""

from unittest.mock import patch
import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand


@patch('sys.exit')
def test_add_command(mock_exit, capsys):
    """Test the add command."""
    inputs = iter(['10', '20', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("add", AddCommand())
        app.command_handler.execute_command("add")
        captured = capsys.readouterr()
        assert "The result of add operation is 30" in captured.out
        assert not mock_exit.called  # Ensure sys.exit was not called

def test_subtract_command(capsys):
    """Test the subtract command."""
    inputs = iter(['20', '5', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("subtract", SubtractCommand())
        app.command_handler.execute_command("subtract")
        captured = capsys.readouterr()
        assert "The result of subtract operation is 15" in captured.out

def test_multiply_command(capsys):
    """Test the multiply command."""
    inputs = iter(['10', '3', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("multiply", MultiplyCommand())
        app.command_handler.execute_command("multiply")
        captured = capsys.readouterr()
        assert "The result of multiply operation is 30" in captured.out

def test_divide_command(capsys):
    """Test the divide command."""
    # Test division with non-zero divisor
    inputs = iter(['20', '4', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("divide", DivideCommand())
        app.command_handler.execute_command("divide")
        captured = capsys.readouterr()
        assert "The result of divide operation is 5" in captured.out

    # Test division with zero divisor
    inputs = iter(['20', '0', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("divide", DivideCommand())
        app.command_handler.execute_command("divide")
        captured = capsys.readouterr()
        assert "Please enter a non-zero divisor." in captured.out


def test_app_exit():
    """Test that the app exits properly."""
    inputs = iter(['exit'])  # Simulate user entering 'exit'
    with patch('builtins.input', lambda _: next(inputs)):
        app = App()
        with pytest.raises(SystemExit) as e:
            app.start()
        assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command():
    """Test that the app menu command works."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        with pytest.raises(SystemExit) as e:
            app.start()
        assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_invalid_command():
    """Test that the app handles invalid commands gracefully."""
    inputs = iter(['invalid', 'exit'])  # Input an invalid command
    with patch('builtins.input', lambda _: next(inputs)):
        app = App()
        with pytest.raises(SystemExit) as e:
            app.start()
        assert str(e.value) == "Exiting...", "No such command: invalid"
