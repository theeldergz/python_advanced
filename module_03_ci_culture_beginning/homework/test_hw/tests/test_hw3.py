import unittest

from module_02_linux.homework.hw7.accounting import app, storage, add


class TestAccounting(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['PORT'] = 2024
        cls.app = app.test_client()
        storage.update({
            "2024": {
                "01": {
                    "01": 1000,
                    "02": 2000,
                    "month_total": 3000
                },
                "02": {
                    "02": 4000,
                    "month_total": 4000
                },
                "year_total": 7000
            },
            "2025": {
                "01": {
                    "01": 10000,
                    "month_total": 10000
                },
                "year_total": 10000
            }
        }
        )

    def test_can_endpoint_add_work(self):
        response = self.app.get('/add/20240101/2024')
        response_text = response.status_code
        self.assertEqual(200, response_text)

    def test_can_calculate_endpoints_work(self):
        calculate_year_ep = '/calculate/'
        calculate_year_month_ep = '/calculate/'

        response_calculate_year = self.app.get(calculate_year_ep + '2024')
        response_calculate_year_month = self.app.get(calculate_year_month_ep + '2025' + '/01')

        response_calculate_year_text = response_calculate_year.data.decode()
        response_calculate_year_month_text = response_calculate_year_month.data.decode()

        self.assertIn(response_calculate_year_text, str(storage['2024']['year_total']))
        self.assertIn(response_calculate_year_month_text, str(storage['2025']['01']['month_total']))

    def test_cannot_put_incorrect_datetime_format_in_add_ep(self):
        with self.assertRaises(TypeError):
            add('dfdfs', 'dfsdf')
