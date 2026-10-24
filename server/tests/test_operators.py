"""

Tests unitaires du module operators.

Ces tests valident les opérations et les comportements attendus de la calculatrice.

"""

import pytest
from server.operators import add, subtract, multiply, divide

""" Tests de la méthode add : add(a, b) retourne a + b. """

def test_add_two_positive_ints():
    result = add(2,2)
    assert(result == 4)

def test_add_double_int():
    result = add(2.54,2)
    assert(result == pytest.approx(4.54))

def test_add_two_positive_doubles():
    result = add(0.57, 1.34)
    assert(result == pytest.approx(1.91))

def test_add_two_negatives():
    result = add(-2, -1.34)
    assert(result == pytest.approx(-3.34))

def test_add_one_negative():
    result = add(2, -1.34)
    assert(result == pytest.approx(0.66))

def test_add_zero():
    result = add(5,0)
    assert(result == 5)

""" Tests de la méthode subtract : subtract(a, b) retourne a - b. """

def test_subtract_two_positive_ints():
    result = subtract(2,2)
    assert(result == 0)

def test_subtract_double_int():
    result = subtract(2.54,2)
    assert(result == pytest.approx(0.54))

def test_subtract_two_positive_doubles():
    result = subtract(0.57, 1.34)
    assert(result == pytest.approx(-0.77))

def test_subtract_two_negatives():
    result = subtract(-2, -1.34)
    assert(result == pytest.approx(-0.66))

def test_subtract_one_negative():
    result = subtract(2, -1.34)
    assert(result == 3.34)

def test_subtract_zero():
    result = subtract(5,0)
    assert(result == 5)

""" Tests de la méthode multiply : multiply(a, b) retourne a * b. """

def test_multiply_two_int():
    result = multiply(2,3)
    assert(result == 6)

def test_multiply_double_int():
    result = multiply(0.54,2)
    assert(result == 1.08)

def test_multiply_zero():
    result = multiply(0,2)
    assert(result == 0)

def test_multiply_negatives():
    result = multiply(-12, -6)
    assert(result == 72)

def test_multiply_one_negative():
    result = multiply(12, -6)
    assert(result == -72)

""" Tests de la méthode divide : divide(a, b) retourne a / b. """

def test_divide_two_ints():
    result = divide(165, 5)
    assert(result == 33)

def test_divide_double_int():
    result = divide(0.33, 2)
    assert(result == 0.165)

def test_divide_negatives():
    result = divide(-12, -6)
    assert(result == 2)

def test_divide_one_negative():
    result = divide(12, -6)
    assert(result == -2)

def test_divide_num_zero():
    result = divide(0,2)
    assert(result == 0)

def test_divide_denom_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)

