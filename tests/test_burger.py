from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    """Тесты для класса Burger"""

    def test_new_burger_zero_buns(self):
        """Проверка у бургера 0 булочек при создании"""
        burger = Burger()
        assert burger.bun is None


    def test_set_buns(self):
        """Проверка у бургера именно та булочка, что назначили"""

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 100.0

        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_new_burger_zero_ingredients(self):
        """Проверка у бургера 0 ингредиентов при создании"""
        burger = Burger()
        assert burger.ingredients == []

    def test_add_ingredient_quantity_match(self):
        """Проверка у бургера именно 1 ингредиент после назначения"""

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "test ingredient"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_add_ingredient_obj_match(self):
        """Проверка у бургера именно тот ингредиент, что мы назначили"""

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "test ingredient"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient


    def test_remove_ingredient_exists_zero(self):
        """Проверка при удалении добавленного ингредиента их 0"""
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "test ingredient"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_change_position_ingredient(self):
        """Проверка изменения позиции ингредиента"""
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_1.get_name.return_value = "test ingredient"

        mock_ingredient_2 = Mock(spec=Ingredient)
        mock_ingredient_2.get_name.return_value = "test ingredient2"

        burger = Burger()

        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient_1

    def test_get_price(self):
        """Проверка расчета цены бургера с ингредиентами"""

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 100.0

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "test ingredient"
        mock_ingredient.get_price.return_value = 30.0


        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)


        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    def test_get_receipt(self):
        """Проверка формирования чека"""

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 100.0

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "test ingredient"
        mock_ingredient.get_price.return_value = 30.0
        mock_ingredient.get_type.return_value = "sauce"

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert receipt == ("(==== test bun ====)\n"
                           "= sauce test ingredient =\n"
                           "(==== test bun ====)\n\n"
                           "Price: 230.0")