import unittest
from serde.json import from_json, to_json

# Project modules
from entities import Configurations


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tmp = {"x": 10}
        assert to_json(Configurations(10)) == 'str'


if __name__ == '__main__':
    unittest.main()
