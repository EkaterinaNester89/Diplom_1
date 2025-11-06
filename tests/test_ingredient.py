from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient"""

    def test_ingredient_get_type(self):
        """Проверка соответствия заданного типа нового ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test ingredient", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_ingredient_get_name(self):
        """Проверка соответствия заданного имени нового ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "test ingredient", 100)
        assert ingredient.get_name() == "test ingredient"

    def test_ingredient_get_price(self):
        """Проверка соответствия заданной цены нового ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test ingredient", 100)
        assert ingredient.get_price() == 100
