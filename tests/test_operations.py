import pytest
from app.operations import addition, division, subtraction, multiplication


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 2),      # Test adding two positive integers
        (2, 3, 5),      # Test adding two larger positive integers
        (-1, 1, 0),     # Test adding a negative and a positive integer
        (-2, -3, -5),   # Test adding negative integers
        (0, 5, 5),      # Test adding zero and positive integers
        (3.5, 2.5, 6.0), #Test adding two positive float
    ],
)
def test_addition(a, b, expected):
    assert addition(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 0),
        (5, 3, 2),
        (3, 5, -2),
        (-2, -3, 1),
        (0, 5, -5),
        (0, 0, 0),
    ],
)
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 1),
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (0, 5, 0),
        (0, 0, 0),
    ],
)
def test_multiplication(a, b, expected):
    assert multiplication(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 1),
        (6, 2, 3),
        (10, 2, 5),
        (-6, 2, -3),
        (-6, -2, 3),
    ],
)
def test_division(a, b, expected):
    assert division(a, b) == expected


@pytest.mark.parametrize(
    "a,b",
    [
        (1, 0),
        (10, 0),
        (-5, 0),
    ],
)
def test_division_by_zero(a, b):
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(a, b)