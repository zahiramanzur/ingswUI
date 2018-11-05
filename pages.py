from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.USERNAME = self.driver.find_element_by_name('userName')
        self.PASSWORD = self.driver.find_element_by_name('password')
        self.SIGN_IN = self.driver.find_element_by_name('login')

    def sign_in(self, credentials):
        self.USERNAME.clear()
        self.USERNAME.send_keys(credentials['username'])
        self.PASSWORD.clear()
        self.PASSWORD.send_keys(credentials['password'])
        self.SIGN_IN.click()


class FlightFiltersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.DEPARTING_FROM = self.driver.find_element_by_name('fromPort')
        self.ARRIVING_IN = self.driver.find_element_by_name('toPort')
        self.FIRST_CLASS_SERVICE = self.driver.find_element_by_css_selector('input[value="First"]')
        self.FIND_FLIGHTS = self.driver.find_element_by_name('findFlights')

    def fill_filtering_data(self, filtering_data):
        Select(self.DEPARTING_FROM).select_by_value(filtering_data['departing_from'])
        Select(self.ARRIVING_IN).select_by_value(filtering_data['arriving_in'])
        if 'first_class_service' in filtering_data:
            self.FIRST_CLASS_SERVICE.click()


class FlightsResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.RESERVE_FLIGHTS = self.driver.find_element_by_name('reserveFlights')


class PurchaseFlightPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.FIRST_NAME = self.driver.find_element_by_name('passFirst0')
        self.LAST_NAME = self.driver.find_element_by_name('passLast0')
        self.CREDIT_NUMBER = self.driver.find_element_by_name('creditnumber')
        self.BUY_FLIGHTS = self.driver.find_element_by_name('buyFlights')

    def fill_purchasing_data(self, purchasing_data):
        self.FIRST_NAME.send_keys(purchasing_data['first_name'])
        self.LAST_NAME.send_keys(purchasing_data['last_name'])
        self.CREDIT_NUMBER.send_keys(purchasing_data['credit_number'])
