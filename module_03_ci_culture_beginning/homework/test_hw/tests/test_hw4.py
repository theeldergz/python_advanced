import datetime
from unittest import TestCase
from module_03_ci_culture_beginning.homework.hw4.person import Person


class TestPerson(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.person = Person(name='Name', year_of_birth=1998, address='some street')

    def test_can_get_age_correct(self):
        expected_res = 26
        func_res = self.person.get_age()
        self.assertEqual(expected_res, func_res)

    def test_can_get_name_correct(self):
        expected_res = 'Name'
        func_res = self.person.get_name()
        self.assertEqual(expected_res, func_res)

    def test_can_set_name_correct(self):
        expected_res = 'TestName'
        self.person.set_name('TestName')
        self.assertEqual(expected_res, self.person.name)

    def test_can_set_address_correct(self):
        expected_res = 'some street number 2'
        self.person.set_address(expected_res)
        self.assertEqual(expected_res, self.person.address)

    def test_can_get_address_correct(self):
        expected_res = 'some street'
        func_res = self.person.get_address()
        self.assertEqual(expected_res, func_res)

    def test_is_homeless_work_correct(self):
        func_res = self.person.is_homeless()
        self.assertTrue(func_res)

        self.person.set_address('')
        func_res = self.person.is_homeless()
        self.assertFalse(func_res)