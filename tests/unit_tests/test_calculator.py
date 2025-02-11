from src.calculator import Calculator


def test_addition():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0

def test_subtraction():
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(3, 5) == -2
    assert Calculator.subtract(0, 0) == 0

def test_multiplication():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-1, 5) == -5
    assert Calculator.multiply(0, 100) == 0
