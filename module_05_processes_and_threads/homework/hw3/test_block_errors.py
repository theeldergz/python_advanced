import unittest
from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):

    def test_ignore_exc(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                a = 1 / 0
        except:
            self.fail()

    def test_raise_exc(self):
        with self.assertRaises(TypeError):
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'

    def test_raise_outer_exc(self):
        with BlockErrors({TypeError}):
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'

    def test_ignore_sub_exc(self):
        with BlockErrors({Exception}):
            a = 1 / '0'

if __name__ == '__main__':
    unittest.main()
