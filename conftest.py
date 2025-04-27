# conftest.py (updated precise_calculator fixture)
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

class PreciseCalculator(Calculator):
    def __init__(self, precision):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def subtract(self, a, b):
        result = super().subtract(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def multiply(self, a, b):
        result = super().multiply(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = super().divide(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def power(self, a, b):
        result = super().power(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

@pytest.fixture(params=[2, 3, 4])
def precise_calculator_parametrized(request):
    precision = request.param
    return PreciseCalculator(precision=precision)