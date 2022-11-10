# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest
import requests

class TestResiFitWebsite(unittest.TestCase):

    base = 'https://jbddrexel.wixsite.com/resifit'

    def test_home_page(self):
        response = requests.get(self.base)
        # response.
        # print(f'Sending get request to {self.base}...')
        self.assertEqual(response.status_code, 200)
        # print(f'{self.base} returned a status code of 200. Success')

    # TODO rename this page from blank-1 to something else
    def test_about_page(self):
        response = requests.get(f'{self.base}/blank-1')
        self.assertEqual(response.status_code, 200)

    def test_news_page(self):
        response = requests.get(f'{self.base}/news')
        self.assertEqual(response.status_code, 200)

    def test_portfolio_page(self):
        response = requests.get(f'{self.base}/portfolio')
        self.assertEqual(response.status_code, 200)

    def test_jobs_page(self):
        response = requests.get(f'{self.base}/jobs')
        self.assertEqual(response.status_code, 200)

    # TODO rename this page from blank-3 to something else
    def test_resources_and_tips_page(self):
        response = requests.get(f'{self.base}/blank-3')
        self.assertEqual(response.status_code, 200)

    # TODO rename this page from blank-2 to something else
    def test_contact_page(self):
        response = requests.get(f'{self.base}/blank-2')
        self.assertEqual(response.status_code, 200)

    def test_bad_page(self):
        response = requests.get(f'{self.base}/thisdoesnotexist')
        self.assertEqual(response.status_code, 404)

    def test_another_bad_page(self):
        response = requests.get(f'{self.base}/thisalsodoesnotexist')
        self.assertEqual(response.status_code, 404)

    # TODO rename this page from general-clean to tools
    def test_tools_page(self):
        response = requests.get(f'{self.base}/general-clean')
        self.assertEqual(response.status_code, 200)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Running ResiFit Unit Tests...')
    print('Testing GET requests of main site pages...\n')
    unittest.main(verbosity=2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
