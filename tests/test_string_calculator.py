from string_calculator import StringCalculator

def test_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.calculate("") == 0
