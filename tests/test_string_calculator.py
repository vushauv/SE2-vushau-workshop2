import pytest
from string_calculator import StringCalculator

def test_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.calculate("") == 0


@pytest.mark.parametrize("value", [
    "0",
    "1",
    "5",
    "123",
    "004",
    " 42 ",
    " 42",
    "42 ",
    "1000"
])
def test_single_number_returns_value(value: str) -> None:
    calc = StringCalculator()
    assert calc.calculate(value) == int(value)


@pytest.mark.parametrize("num1,num2", [
    (0, 0),
    (10, 0),
    (123, 456),
])
def test_two_numbers_comma_delimited_return_sum(num1: int, num2: int) -> None:
    calc = StringCalculator()
    assert calc.calculate(f"{num1},{num2}") == num1 + num2


@pytest.mark.parametrize("num1,num2", [
    (0, 0),
    (10, 0),
    (123, 456),
])
def test_two_numbers_newline_delimited_return_sum(num1: int, num2: int) -> None:
    calc = StringCalculator()
    assert calc.calculate(f"{num1}\n{num2}") == num1 + num2


@pytest.mark.parametrize("numbers,expected", [
    ("1,2,3", 6),
    ("1\n2\n3", 6),
    ("1,2\n3", 6),
    ("1\n2,3", 6),
    ("0,0,0", 0),
    ("10,20\n30", 60),
    (" 123 \n  456,789  ", 1368),
])
def test_three_numbers_delimited_either_way_return_sum(numbers: str, expected: int) -> None:
    calc = StringCalculator()
    assert calc.calculate(numbers) == expected


@pytest.mark.parametrize("numbers", [
   "-1",
    "-1,2",
    "1,-2",
    "1,-2,3",
    "   -1   \n  -2,-3",
    "1\n -2 , 3 ",
])
def test_negative_numbers_throw_exception(numbers: str) -> None:
    calc = StringCalculator()

    with pytest.raises(ValueError):
        calc.calculate(numbers)


@pytest.mark.parametrize("numbers,expected", [
    ("2,1001", 2),
    ("1001,2", 2),
    ("2,1000", 1002),
    ("1000,2", 1002),
    ("1001,1002", 0),
    ("1,2,1001", 3),
    ("1,1000,2", 1003),
    ("1001\n2", 2),
    ("2\n1001", 2),
    ("1\n1001,2", 3),
    ("999,1", 1000),
    ("1000", 1000),
    ("1001", 0),
])
def test_numbers_greater_than_1000_are_ignored(numbers: str, expected: int) -> None:
    calc = StringCalculator()
    assert calc.calculate(numbers) == expected