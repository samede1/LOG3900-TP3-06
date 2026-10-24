"""

Tests unitaires du module app (fonction calculate).

Ces tests couvrent les résultats d'expressions simples ("a opérande b") et traitent les cas d'erreurs.

"""

import pytest
from server.app import calculate

""" Tests de la méthode calculate """

def test_calculate_add():
    " Expression simple avec '+' "
    result = calculate("10+30")
    assert(result == 40)

def test_calculate_add_with_spaces():
    " Expression simple avec '+' qui doit ignorer les espaces "
    result = calculate(" 10 + 30 ")
    assert(result == 40)

def test_calculate_substract(): 
    " Expression simple avec '-' "
    result = calculate("25-15")
    assert(result == 10)

def test_calculate_multiply(): 
    " Expression simple avec '*' "
    result = calculate("5*5")
    assert(result == 25)

def test_calculate_divide(): 
    " Expression simple avec '/' "
    result = calculate("25/5")
    assert(result == pytest.approx(5.0))

def test_calculate_float(): 
    " Expression simple avec '/' qui n'est pas une division entière "
    result = calculate("26/5")
    assert(result == pytest.approx(5.2))

def test_calculate_division_by_zero():
    " Expression simple avec '/' où le dénumérateur est 0, qui doit relever ZeroDivisionError "
    with pytest.raises(ZeroDivisionError):
        calculate("5/0")

def test_calculate_empty():
    " Expression vide qui doit relever un ValueError "
    with pytest.raises(ValueError):
        calculate("")

def test_invalid_format():
    " Expression mal formatée qui doit relever un ValueError "
    with pytest.raises(ValueError):
        calculate("5+")
    with pytest.raises(ValueError):
        calculate("+5")
    with pytest.raises(ValueError):
            calculate("+")

def test_calculate_non_numeric_operands():
    " Expression qui comporte un caractère non-numérique qui doit relever un ValueError "
    with pytest.raises(ValueError):
        calculate("a+b")
    with pytest.raises(ValueError):
        calculate("1-b")
    with pytest.raises(ValueError):
        calculate("a/1")

def test_calculate_multiple_operands():
    " Expression qui comporte plus qu'une operande qui doit relever un ValueError "
    with pytest.raises(ValueError):
        calculate("3-2-1")





    