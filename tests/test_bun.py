from unittest.mock import Mock

from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun("test", 10)
        assert bun.get_name() == "test"

    def test_get_price(self):
        bun = Bun("test", 10)
        assert bun.get_price() == 10

    def test_mock_bun_get_name(self):
        bun = Mock()
        bun.get_name.return_value = "bulka"
        assert bun.get_name() == "bulka"

    def test_mock_bun_get_price(self):
        bun = Mock()
        bun.get_price.return_value = 10
        assert bun.get_price() == 10

