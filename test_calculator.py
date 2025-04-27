# test_calculator.py (updated with parameterized precise_calculator test)
import pytest
# from calculator import Calculator # No longer need this import

# ... (rest of your existing test functions) ...

def test_precise_calculator_addition(precise_calculator):
    assert precise_calculator.add(1.005, 2.003) == 3.01

def test_precise_calculator_division(precise_calculator):
    assert precise_calculator.divide(10, 3) == pytest.approx(3.33)

def test_precise_calculator_rounding_parametrized(precise_calculator_parametrized):
    if precise_calculator_parametrized.precision == 2:
        assert precise_calculator_parametrized.add(1.005, 2.003) == 3.01
    elif precise_calculator_parametrized.precision == 3:
        assert precise_calculator_parametrized.add(1.0005, 2.0003) == 3.001
    elif precise_calculator_parametrized.precision == 4:
        assert precise_calculator_parametrized.add(1.00005, 2.00003) == 3.0001