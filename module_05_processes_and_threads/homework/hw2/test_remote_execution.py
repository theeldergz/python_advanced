import unittest
from remote_execution import app


class TestHomeworkTaskTwo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        cls.app = app.test_client()
        cls.base_url = '/run_code'

    def test_timeout_work_correct(self):
        test_data = {"code": "print('TEST')", "timeout": 0}
        response = self.app.post(self.base_url, data=test_data)
        self.assertEqual(400, response.status_code)

    def test_not_correct_form_data(self):
        test_data = {'code': 234234, 'timeout': 'fdsf'}
        response = self.app.post(self.base_url, data=test_data)
        self.assertEqual(400, response.status_code)

    def test_can_raise_BlockingIOError(self):
        test_data = {"code": "\nfrom subprocess import run\nrun(['./kill_the_system.sh'])", "timeout": 10}
        response = self.app.post(self.base_url, data=test_data)
        self.assertIn('BlockingIOError', response.data.decode())


if __name__ == '__main__':
    unittest.main()
