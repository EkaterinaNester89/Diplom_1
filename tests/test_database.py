from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database базы данных"""

    def test_database_initialization_buns_quantity(self):
        """Проверка запуска базы данных с правильным
         количеством булочек """

        database = Database()
        assert len(database.buns) == 3

    def test_database_initialization_buns_ingredients(self):
        """Проверка запуска базы данных с правильным
         количеством ингредиентов """

        database = Database()
        assert len(database.ingredients) == 6

    @pytest.mark.parametrize("index,name,price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_buns_parametrized(self, index, name, price):
        """Параметризованный тест всех булочек"""

        database = Database()
        buns = database.available_buns()
        bun = buns[index]

        assert bun.name == name

    @pytest.mark.parametrize("index,ingredient_type,name,price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_ingredients_parametrized(self, index, ingredient_type, name, price):
        """Параметризованный тест всех ингредиентов"""
        database = Database()

        ingredients = database.available_ingredients()
        ingredient = ingredients[index]

        assert ingredient.name == name
