from selenium import webdriver
import os
import time
import booking.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path

        # Code below is designed to make the Selenium bot less detectable by websites that try to block automated traffic
        options = Options()
        options.add_argument("--incognito")

        # Makes the browser identify as a regular Chrome browser
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )

        # To hide automation flags
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)
        super().__init__(options=options)
        self.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
        )
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self,currency):
        advert_btn = self.find_elements(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
        if advert_btn:
            advert_btn[0].click()

        try:
            currency_btn = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'))
            )
            currency_btn.click()
        except:
            print("Couldn't click the header currency picker trigger")
        try:
            change_currency_btn = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[@data-testid='selection-item' and .//div[text()='{currency}']]"))
            )
            change_currency_btn.click()
        except:
            print("Couldn't change the currency at the last step")

    def select_place_to_go(self, place):
        search_field = WebDriverWait(self,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="ss"]'))
        )
        search_field.clear()
        search_field.send_keys(place)

        first_result = WebDriverWait(self,5).until(
            EC.element_to_be_clickable((By.ID, "autocomplete-result-0"))
        )
        time.sleep(1)
        first_result.click()

    def select_dates(self,check_in, check_out):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out}"]'
        )
        check_out_element.click()

    def select_adults(self,count=1):
        selection_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        selection_element.click()
        WebDriverWait(self,3)

        while True:
            decrease_btn = WebDriverWait(self,5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='de576f5064 b46cd7aad7 e26a59bb37 c295306d66 c7a901b0e7 aaf9b6e287 c857f39cb2']"))
            )
            decrease_btn.click()
            value_adults = self.find_elements(By.CLASS_NAME, 'e32aa465fd')[0]
            int_adults = int(value_adults.text)
            # if the value of adult reaches 1, we should break the loop
            if int_adults == 1:
                break

        increase_btn = self.find_element(By.XPATH,'//button[@class="de576f5064 b46cd7aad7 e26a59bb37 c295306d66 c7a901b0e7 aaf9b6e287 dc8366caa6"]')

        for i in range(count - 1):
            increase_btn.click()



    def click_search(self):
        search_btn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_btn.click()


    def apply_filters(self):
        filters = BookingFiltration(driver=self)
        filters.apply_star_rating(3,4,5)
        filters.sort_price_lowest_first()


    def report_results(self):
        # when at least 1 element is rendered, we try to find all
        WebDriverWait(self, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="title"]'))
        )
        cards = self.find_element(By.CSS_SELECTOR, 'div[role="list"]')

        report = BookingReport(cards)
        table = PrettyTable(
            ["Hotel Name", "Price", "Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)