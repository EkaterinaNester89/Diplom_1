from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun - булочка"""

    def test_get_bun_name(self):
        """Проверка имя у булочки, такое какое задали"""
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_get_bun_price(self):
        """Проверка цена у булочки, такая какую задали"""
        bun = Bun("white bun", 200)
        assert bun.get_price() == 200
