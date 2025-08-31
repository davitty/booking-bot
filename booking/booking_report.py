# This file is for including methods that will parse
# the specific data we need from each one of the deal boxes
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()


    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]').text.strip()
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]').text.strip()
            hotel_score_parent = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]')
            hotel_score_children = hotel_score_parent.find_elements(By.XPATH, "./*")
            hotel_score = hotel_score_children[1].text.strip()
            collection.append([hotel_name,hotel_price,hotel_score])

        return collection

