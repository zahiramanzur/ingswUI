import os
import unittest
from selenium import webdriver
import pages


current_dir = os.path.abspath(os.path.dirname(__name__))

class FlightTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.join(current_dir, 'chromedriver'))
        self.base_url = 'http://newtours.demoaut.com'

    def tearDown(self):
        self.driver.close()

def test_book_flight(self):
        self.driver.get(self.base_url)
        landing_page = pages.LandingPage(self.driver)
        credentials = {
            'username': 'tutorial',
            'password': 'tutorial'
        }
        landing_page.sign_in(credentials)
        flight_filters_page = pages.FlightFiltersPage(self.driver)
        flight_filtering_data = {
            'departing_from': 'London',
            'arriving_in': 'Paris',
            'first_class_service': True
        }
        flight_filters_page.fill_filtering_data(flight_filtering_data)
        flight_filters_page.FIND_FLIGHTS.click()
        flights_results_page = pages.FlightsResultsPage(self.driver)
        flights_results_page.RESERVE_FLIGHTS.click()
        purchase_flight_page = pages.PurchaseFlightPage(self.driver)
        purchasing_data = {
            'first_name': 'juan',
            'last_name': 'perez',
            'credit_number': '1111'
        }
        purchase_flight_page.fill_purchasing_data(purchasing_data)
        purchase_flight_page.BUY_FLIGHTS.click()

        sign_off = self.driver.find_element_by_css_selector('a[href="mercurysignoff.php"]')
        self.assertIsNotNone(sign_off)
        sign_off.click()

if __name__ == '__main__':
    unittest.main(verbosity=2)
