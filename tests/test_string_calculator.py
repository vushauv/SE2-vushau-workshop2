import pytest
from string_calculator import StringCalculator

def test_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.calculate("") == 0


@pytest.mark.parametrize("value", [
    "-20",
    "-1"
    "0",
    "1",
    "5",
    "123",
    "9999",
])
def test_single_number_returns_value(value: str) -> None:
    calc = StringCalculator()
    assert calc.calculate(value) == int(value)


@pytest.mark.parametrize("num1,num2", [
    (0, 0),
    (-4, -2),
    (10, 0),
    (123, 456),
])
def test_two_numbers_comma_delimited_return_sum(num1: int, num2: int) -> None:
    calc = StringCalculator()
    assert calc.calculate(f"{num1},{num2}") == num1 + num2