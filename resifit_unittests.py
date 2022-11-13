# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest
import requests
from bs4 import BeautifulSoup

# we will use selenium later to
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from shutil import copyfile
from datetime import datetime, timedelta
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

class TestResiFitWebsite(unittest.TestCase):
    # setup for future Selenium use
    # options = Options()
    # options.headless = True
    # driver = webdriver.Chrome(options=options)

    base = 'https://jbddrexel.wixsite.com/resifit'

    def test_home_page(self):
        # self.driver.get('https://www.investopedia.com')

        response = requests.get(self.base)
        self.assertEqual(response.status_code, 200)

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

    def test_all_links_on_resources_page(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
        source = requests.get(f'{self.base}/blank-3').text
        soup = BeautifulSoup(source, 'html.parser')
        section = soup.find('section', {'id':'comp-la7mrnoo'})
        links = section.find_all('a', href=True)
        for link in links:
            url = link.get('href')

            # credit.com does not allow programmatic access, even when setting UserAgent in the headers to
            # mimic browser activity. For now, we will skip testing the link for this site.
            if url != 'https://www.credit.com':
                response = requests.get(url, headers=headers)
                self.assertEqual(response.status_code, 200)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Running ResiFit Unit Tests...')
    print('Testing GET requests of main site pages...\n')
    unittest.main(verbosity=2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
