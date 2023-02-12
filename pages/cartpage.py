from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class CartPage(BasePage):
	# Elements mapping
	CART_LIST = (By.ID, 'tbodyid')
	PURCHASE_SUCCESSFUL_MESSAGE = "Thank you for your purchase!"
	# mapping elements by zone and name
	MAPPING = {
		"cart page": { # mapping elements on the cart page
			"Place Order": (By.XPATH, '//button[contains(text(),"Place Order")]')
		},
		"place order popup": { # mapping elements on the popup after you click Place Order button
			"Purchase": (By.XPATH, '//button[contains(text(),"Purchase")]'),
			"Name": (By.ID, 'name'),
			"Country": (By.ID, 'country'),
			"City": (By.ID, 'city'),
			"Credit card": (By.ID, 'card'),
			"Month": (By.ID, 'month'),
			"Year": (By.ID, 'year'),

		},
		"purchase popup": { # mapping elements on the popup after you click Purchase button on Place Order popup
			"message": (By.XPATH, '//div[@class="sweet-alert  showSweetAlert visible"]/h2'),
			"info block": (By.XPATH, '//div[@class="sweet-alert  showSweetAlert visible"]/p')
		}
	}

	def click_on_element(self, element, menu_choice):
		element_selector = self.MAPPING[menu_choice][element]
		self.wait_and_click_element_by_selector(*element_selector)

	def validate_confirmation_message(self, message):
		alert = WebDriverWait(self.chrome, 2).until(ec.alert_is_present())
		assert alert.text == message, f'Message confirmation error, expected: {message}, but we got: {alert.text}'
		alert.accept()

	# function to verify number of items in the cart list
	def verify_cart_nr_of_items(self, number):
		cart_list = self.chrome.find_element(*self.CART_LIST) # we get the webelement that contains the cart list of added products
		items = cart_list.find_elements(By.CLASS_NAME, "success") # we get a list of all the products in the cart list
		assert len(items) == int(number), f'Error, number of items in the cart does not match, expected: {number}, but got: {len(items)}'

	def add_input_to_location(self, input_text, location, menu):
		element_selector = self.MAPPING[menu][location]
		self.chrome.find_element(*element_selector).send_keys(input_text)

	# function to verify purchase message
	def verify_purchase_message(self, credit_card, name):
		message_shown = self.chrome.find_element(*self.MAPPING["purchase popup"]["message"]).text # we get the shown message
		assert message_shown == self.PURCHASE_SUCCESSFUL_MESSAGE, f'Message error, expected: {self.PURCHASE_SUCCESSFUL_MESSAGE}, but got: {message_shown}'
		info_block = self.chrome.find_element(*self.MAPPING["purchase popup"]["info block"]).get_attribute("innerHTML") # we got all the information block on the popup as a HTML since we can't isolate a part of it using selectors
		info_list = [text for text in info_block.split("<br>")] # since the info is split by HTML code <br>, we split it
		# id_shown = info_list[0] currently not used in test
		# amount_shown = info_list[1] currently not used in test
		card_shown = info_list[2]
		name_shown = info_list[3]
		# date_shown = info_list[4] currently not used in test
		assert credit_card in card_shown, f'Error, credit card information does not match, expected: {credit_card}, but got {card_shown}'
		assert name in name_shown, f'Error, mane information does not match, expected: {name}, but got {name_shown}'

