

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self):
        bun = Bun("Sesame Bun", 1.5)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize(("ingredient_type", "name", "price"), [
        ("Vegetable", "Lettuce", 0.5),
        ("Meat", "Beef", 1.5),
        ("Cheese", "Cheddar", 2.5)
    ])
    def test_add_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in list(burger.ingredients)

    def test_remove_ingredient(self):
        ingredient = Ingredient("Vegetable", "Lettuce", 0.5)
        ingredient2 = Ingredient("Meat", "Beef", 1.5)
        burger = Burger()
        burger.ingredients.append(ingredient)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert ingredient not in list(burger.ingredients)

    def test_move_ingredient(self):
        ingredient = Ingredient("Vegetable", "Lettuce", 0.5)
        ingredient2 = Ingredient("Meat", "Beef", 1.5)
        burger = Burger()
        burger.ingredients.append(ingredient)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients.index(ingredient) == 1
        assert burger.ingredients.index(ingredient2) == 0

    def test_get_price(self):
        bun = Bun("Sesame Bun", 1.5)
        lettuce = Ingredient("Lettuce", "Vegetable", 0.5)
        tomato = Ingredient("Tomato", "Vegetable", 0.7)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(lettuce)
        burger.add_ingredient(tomato)
        expected_price = bun.get_price() * 2 + lettuce.get_price() + tomato.get_price()
        assert expected_price == burger.get_price()

    def test_get_receipt(self):
        bun = Bun("Sesame Bun", 1.5)
        lettuce = Ingredient("Lettuce", "VEGETABLE", 0.5)
        tomato = Ingredient("Tomato", "VEGETABLE", 0.7)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(lettuce)
        burger.add_ingredient(tomato)
        receipt = burger.get_receipt()
        assert f'(==== {bun.get_name()} ====)' in receipt
        assert f'= {lettuce.get_type().lower()} {lettuce.get_name()} =' in receipt
        assert f'= {tomato.get_type().lower()} {tomato.get_name()} =' in receipt
        assert f'Price: {burger.get_price()}' in receipt
