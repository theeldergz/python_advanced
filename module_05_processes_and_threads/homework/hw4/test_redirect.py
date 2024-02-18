import os
import sys
import traceback
import unittest
from redirect import Redirect


class TestRedirect(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_stdout_file = open('test_stdout.txt', 'w')
        cls.test_stderr_file = open('test_stderr.txt', 'w')

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove('test_stdout.txt')
        os.remove('test_stderr.txt')

    def test_redirect_stdout(self):
        with Redirect(stdout=self.test_stdout_file):
            print('Hello stdout.txt')

        with open('test_stdout.txt', 'r', encoding='utf-8') as file:
            self.assertIn('Hello stdout.txt', file.read())

    def test_redirect_stderr(self):
        with Redirect(stderr=self.test_stderr_file):
            raise Exception('Hello stderr.txt')

        with open('test_stderr.txt', 'r', encoding='utf-8') as file:
            self.assertIn('Exception: Hello stderr.txt', file.read())


if __name__ == '__main__':
    unittest.main()
    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
