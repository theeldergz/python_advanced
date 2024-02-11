"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app, RegistrationForm
from flask import request


class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        cls.app = app.test_client()
        cls.base_url = '/registration'

        # словарь test_data изначально с верными данными
        cls.test_data = {'email': 'test@mail.ru',
                         'phone': 8999999999,
                         'name': 'Denis',
                         'address': 'Test Adress Street',
                         'index': 404,
                         'comment': 'TEST COMMENT'
                         }

    def test_all_fields_correct(self):
        """
        Тест проверяет, работает ли форма регистрации при идеальных условиях
        (правильно заполнены все поля в RegistrationForm)
        """

        response = self.app.post(self.base_url, data=self.test_data)
        self.assertEqual(200, response.status_code)

    def test_field_email_no_correct(self):
        self.test_data['email'] = 'bezsobaki.ru'
        response = self.app.post(self.base_url, data=self.test_data)
        self.assertEqual(400, response.status_code)

    def test_field_phone_no_correct(self):
        self.test_data['phone'] = '790000000ffff'
        response = self.app.post(self.base_url, data=self.test_data)
        self.assertEqual(400, response.status_code)

    def test_field_name_no_correct(self):
        self.test_data['name'] = ''
        response = self.app.post(self.base_url, data=self.test_data)
        self.assertEqual(400, response.status_code)

    def test_field_address_no_correct(self):
        self.test_data['address'] = ''
        response = self.app.post(self.base_url, data=self.test_data)
        self.assertEqual(400, response.status_code)

    def test_field_index_no_correct(self):
        self.test_data['index'] = '404f'
        response = self.app.post(self.base_url, data=self.test_data)
        self.assertEqual(400, response.status_code)

    def test_field_comment_no_correct(self):
        """Тест поля comment не может быть неуспешным, т.к. не подключены валидаторы"""
        self.test_data['comment'] = ''
        response = self.app.post(self.base_url, data=self.test_data)
        self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    unittest.main()
