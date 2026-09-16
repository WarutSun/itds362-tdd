from kitchen import Quantity, grams, ounces, Converter
from kitchen import Quantity, grams, ounces

def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)

def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)

def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)
    
def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)
    
def test_addition_of_different_units():
    total = grams(200).plus(ounces(1))
    converter = Converter()
    converter.add_rate("oz", "g", 28.35)
    assert converter.reduce(total, "g") == grams(228.35)