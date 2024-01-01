import unittest

from src.your_python_module1 import add_numbers


class TestYourModule1(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8, "Addition result is incorrect")


if __name__ == '__main__':
    unittest.main()
