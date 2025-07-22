import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize('ingredient_type, name, price', [
    (INGREDIENT_TYPE_FILLING, 'big naggets', 250.20),
    (INGREDIENT_TYPE_SAUCE, 'garlic sauce', 95.00)
])
def test_ingredient_get_type(ingredient_type, name, price):
    ing = Ingredient(ingredient_type, name, price)
    assert ing.get_type() == ingredient_type

@pytest.mark.parametrize('ingredient_type, name, price', [
    (INGREDIENT_TYPE_FILLING, 'big naggets', 250.20),
    (INGREDIENT_TYPE_SAUCE, 'garlic sauce', 95.00)
])
def test_ingredient_get_name(ingredient_type, name, price):
    ing = Ingredient(ingredient_type, name, price)
    assert ing.get_name() == name

@pytest.mark.parametrize('ingredient_type, name, price', [
    (INGREDIENT_TYPE_FILLING, 'big naggets', 250.20),
    (INGREDIENT_TYPE_SAUCE, 'garlic sauce', 95.00)
])
def test_ingredient_get_price(ingredient_type, name, price):
    ing = Ingredient(ingredient_type, name, price)
    assert ing.get_price() == price