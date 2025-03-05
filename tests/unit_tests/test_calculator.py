from src.calculator import add, multiply, subtract


def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0


def test_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
