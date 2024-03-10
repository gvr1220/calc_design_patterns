
"""
Module providing tests for various operations in the calculator.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_operation():
    """Testing various operations"""
    test_cases = [
        ([Decimal('0'), Decimal('0')], add, Decimal('0')),
        ([Decimal('1'), Decimal('1')], multiply, Decimal('1')),
        ([Decimal('2'), Decimal('2')], multiply, Decimal('4')),
        ([Decimal('3'), Decimal('3')], subtract, Decimal('0')),
        ([Decimal('4'), Decimal('4')], add, Decimal('8')),
    ]

    for operands, operation, expected in test_cases:
        calculation = Calculation.create(operands, operation)
        assert calculation.perform() == expected, f"{operation.__name__} operation failed"


def test_divide_by_zero():
    """Testing the divide by zero exception"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation.create([Decimal('10'), Decimal('0')], divide)
        calculation.perform()
