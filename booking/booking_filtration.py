# After the results, this file will include a class and apply filters
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        stars_parent_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "filter_group_class_")]'))
        )
        star_child_elements = stars_parent_element.find_elements(By.CSS_SELECTOR, '*')

        # star values, so we can select multiple star options
        for star_value in star_values:
            for element in star_child_elements:
                if str(element.get_attribute('innerHTML')).strip() == f"{star_value} stars":
                    element.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        element.click()
        price_element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="price"]'))
        )
        price_element.click()