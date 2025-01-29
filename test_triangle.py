import pytest

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle sides"

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        right_triangle = True
    else:
        right_triangle = False

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
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles():
    assert classify_triangle(5, 5, 3) == "Isosceles"

def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene Right Triangle"

def test_invalid_triangle():
    assert classify_triangle(0, 4, 5) == "Invalid triangle sides"
    assert classify_triangle(-1, 4, 5) == "Invalid triangle sides"

def test_right_equilateral():
    assert classify_triangle(1, 1, 1) == "Equilateral"

