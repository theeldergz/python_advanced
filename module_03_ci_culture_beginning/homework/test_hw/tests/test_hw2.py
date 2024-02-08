import unittest
from module_02_linux.homework.hw3.decrypt import decrypt


class TestDecrypt(unittest.TestCase):

    def test_if_one_dot(self):
        self.assertEqual('абра-кадабра', decrypt('абра-кадабра.'))
        self.assertEqual('', decrypt('.'))

    def test_if_two_dot(self):
        self.assertEqual('абра-кадабра', decrypt('абраа..-кадабра'))
        self.assertEqual('абра-кадабра', decrypt('абра--..кадабра'))

    def test_if_three_dot(self):
        self.assertEqual('абра-кадабра', decrypt('абраа..-.кадабра'))
        self.assertEqual('абра-кадабра', decrypt('абрау...-кадабра'))
        self.assertEqual('23', decrypt('1..2.3'))

    def test_if_four_and_more_dots(self):
        self.assertEqual('', decrypt('абра........'))
        self.assertEqual('a', decrypt('абр......a.'))
        self.assertEqual('', decrypt('1.......................'))