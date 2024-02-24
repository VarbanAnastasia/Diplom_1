from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient("sauce", "Томатный", 1)
        assert ingredient.get_price() == 1

    def test_get_name(self):
        ingredient = Ingredient("sauce", "Томатный", 1)
        assert ingredient.get_name() == "Томатный"

    def test_get_type(self):
        ingredient = Ingredient("sauce", "Томатный", 1)
        assert ingredient.get_type() == "sauce"


