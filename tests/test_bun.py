from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun("test", 10)
        assert bun.get_name() == "test"

    def test_get_price(self):
        bun = Bun("test", 10)
        assert bun.get_price() == 10

