import pytest

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on the lengths of its sides.

    Args:
        a (int or float): Length of the first side.
        b (int or float): Length of the second side.
        c (int or float): Length of the third side.

    Returns:
        str: The type of the triangle ("Equilateral", "Isosceles", "Scalene")
             and whether it is a "Right Triangle" or not.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle sides"

    right_triangle = (a**2 + b**2 == c**2 or
                     a**2 + c**2 == b**2 or
                     b**2 + c**2 == a**2)

    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    if right_triangle:
        return f"{triangle_type} Right Triangle"
    else:
        return triangle_type

def test_equilateral():
    """Test for equilateral triangle."""
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles():
    """Test for isosceles triangle."""
    assert classify_triangle(5, 5, 3) == "Isosceles"

def test_scalene():
    """Test for scalene triangle."""
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_right_triangle():
    """Test for right triangle."""
    assert classify_triangle(3, 4, 5) == "Scalene Right Triangle"

def test_invalid_triangle():
    """Test for invalid triangle sides."""
    assert classify_triangle(0, 4, 5) == "Invalid triangle sides"
    assert classify_triangle(-1, 4, 5) == "Invalid triangle sides"

def test_degenerate_triangle():
    """Test for degenerate triangle where the sides form a line."""
    assert classify_triangle(1, 2, 3) == "Invalid triangle sides"

def test_zero_side():
    """Test for invalid triangle with a zero side length."""
    assert classify_triangle(0, 4, 5) == "Invalid triangle sides"

def test_non_numeric_input():
    """Test for invalid triangle with non-numeric input."""
    assert classify_triangle("a", 4, 5) == "Invalid triangle sides"
    assert classify_triangle(3, "b", 5) == "Invalid triangle sides"
    assert classify_triangle(3, 4, "c") == "Invalid triangle sides"

