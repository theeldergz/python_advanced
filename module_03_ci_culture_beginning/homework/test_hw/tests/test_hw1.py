from unittest import TestCase
from datetime import datetime, timedelta
from freezegun import freeze_time
from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import GREETINGS, app


class TestModule3HomeWork(TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time('2024-02-06')
    def test_can_get_correct_weekday(self):
        username = 'username'
        datetime_now = datetime.now()

        for day_num in range(8):
            response = self.app.get(self.base_url + username)
            response_text = response.data.decode()

            delta = timedelta(days=day_num)
            datetime_then = datetime_now + delta
            weekday = datetime_then.today().weekday()
            greetings = GREETINGS[weekday]
            self.assertTrue(greetings in response_text)

    def test_can_get_correct_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_cannot_pass_weekday_in_username(self):
        username = 'хорошей среды'
        weekday = datetime.today().weekday()
        greetings = GREETINGS[weekday]
        self.assertNotIn(username, greetings)
