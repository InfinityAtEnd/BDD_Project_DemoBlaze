from time import perf_counter

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):
	# Elements mapping
	WEBPAGE = "https://www.demoblaze.com/index.html"
	BOTTOM_ABOUT_US = (By.XPATH, '//b[contains(text(),"About Us")]/parent::h4/following-sibling::p')
	BOTTOM_ABOUT_US_INFO = "We believe performance needs to be validated at every stage of the software development cycle and our open source compatible, massively scalable platform makes that a reality."
	ABOUT_US_VIDEO = (By.ID, "example-video")
	BOTTOM_GET_IN_TOUCH = (By.XPATH, '//b[contains(text(),"Get in Touch")]/parent::h4')
	BOTTOM_GET_IN_TOUCH_INFO = {
		"Address": "2390 El Camino Real",
		"Phone": "+440 123456",
		"Email": "demo@blazemeter.com"
	}
	BOTTOM_LOGO = (By.XPATH, "//h4/img")
	BOTTOM_LOGO_PARAMETERS = {
		"width": 50,
		"height": 50,
		"image": "https://www.demoblaze.com/bm.png"
	}
	# mapping page elements as dictionary in dictionary
	MAPPING = {
		"top menu": { # mapping buttons of the top right menu
			"Home": (By.XPATH, '//a[contains(text(),"Home")]'),
			"Contact": (By.XPATH, '//a[contains(text(),"Contact")]'),
			"About us": (By.XPATH, '//a[contains(text(),"About us")]'),
			"Log in": (By.XPATH, '//a[contains(text(),"Log in")]'),
			"Sign up": (By.ID, 'signin2'),
			"Cart": (By.ID, 'cartur')
		},
		"contact popup": { # mapping elements on the popup from Contact menu
			"Contact Email": (By.ID, "recipient-email"),
			"Contact Name": (By.ID, "recipient-name"),
			"Message": (By.ID, "message-text"),
			"Close": (By.XPATH, '//div[@id="exampleModal"]//button[contains(text(),"Close")]'),
			"Send message": (By.XPATH, '//div[@id="exampleModal"]//button[contains(text(),"Send message")]')
		},
		"about us popup": { # mapping elements on the popup from About us menu
			"Close": (By.XPATH, '//div[@id="videoModal"]//button[contains(text(),"Close")]')
		},
		"log in popup": { # mapping elements on the popup from Log in menu
			"Username": (By.ID, "loginusername"),
			"Password": (By.ID, "loginpassword"),
			"Close": (By.XPATH, '//div[@id="logInModal"]//button[contains(text(),"Close")]'),
			"Log in": (By.XPATH, '//div[@id="logInModal"]//button[contains(text(),"Log in")]')
		},
		"sign up popup": { # mapping elements on the popup from Sign up menu
			"Username": (By.ID, "sign-username"),
			"Password": (By.ID, "sign-password"),
			"Close": (By.XPATH, '//div[@id="signInModal"]//button[contains(text(),"Close")]'),
			"Sign up": (By.XPATH, '//div[@id="signInModal"]//button[contains(text(),"Sign up")]')
		},
		"product page": { # mapping elements on the product page description on accessing a product
			"Add to cart": (By.XPATH, '//a[contains(text(),"Add to cart")]')
		},
		"search": { # mapping categories to be used as a defined search option since the website doesn't have one
			"Phones": (By.XPATH, '//a[contains(text(),"Phones")]'),
			"Laptops": (By.XPATH, '//a[contains(text(),"Laptops")]'),
			"Monitors": (By.XPATH, '//a[contains(text(),"Monitors")]')
		}
	}

	def navigate_to_start_page(self):
		self.chrome.get(self.WEBPAGE)  # DemoBlaze Homepage

	def get_elapsed_time(self, time):
		start_time = perf_counter()
		self.navigate_to_start_page()  # I access the page again for the timed testing purpose
		WebDriverWait(self.chrome, 5).until(lambda driver: self.chrome.execute_script("return document.readyState") == 'complete')
		end_time = perf_counter()
		elapsed_time = end_time - start_time
		assert elapsed_time <= float(time), f'it took too long, expected: less than {time} seconds but instead it took: {elapsed_time} seconds'

	def check_visibility_of(self, category_name):
		element = self.chrome.find_element(By.XPATH, f'//a[contains(text(),"{category_name}")]')
		assert element, f'Element {category_name} is not visible or does not exists!'

	def about_us(self): # function to check the text shown in the bottom About us section
		element = self.chrome.find_element(*self.BOTTOM_ABOUT_US).text
		assert len(element) == len(self.BOTTOM_ABOUT_US_INFO), f"Fields does not match, expected: {len(self.BOTTOM_ABOUT_US_INFO)} but got {len(element)}"
		assert element == self.BOTTOM_ABOUT_US_INFO, f"Field does not match, expected: {self.BOTTOM_ABOUT_US_INFO}, but we got {element}"

	def get_in_touch(self): # function to check the text shown in the bottom Get in Touch section
		get_in_touch_element = self.chrome.find_element(*self.BOTTOM_GET_IN_TOUCH)
		get_in_touch_data = get_in_touch_element.find_elements(By.TAG_NAME, "p")
		for el in get_in_touch_data:
			assert el.text in self.BOTTOM_GET_IN_TOUCH_INFO.values(), f'The field: {el.text} is not found!'

	def logo(self): # function to check the logo shown on the bottom right section
		logo_element = self.chrome.find_element(*self.BOTTOM_LOGO)
		logo_width = int(logo_element.get_attribute("width"))
		logo_height = int(logo_element.get_attribute("height"))
		logo_image_path = logo_element.get_attribute("src")
		assert logo_height == self.BOTTOM_LOGO_PARAMETERS["height"], f'Field does not match, expected height: {self.BOTTOM_LOGO_PARAMETERS["height"]}, but we got {logo_height}'
		assert logo_width == self.BOTTOM_LOGO_PARAMETERS["width"], f'Field does not match, expected width: {self.BOTTOM_LOGO_PARAMETERS["width"]}, but we got {logo_width}'
		assert logo_image_path == self.BOTTOM_LOGO_PARAMETERS["image"], f'Field does not match, expected image path: {self.BOTTOM_LOGO_PARAMETERS["image"]}, but we got {logo_image_path}'

	def click_on_element(self, element, menu_choice):
		if menu_choice not in self.MAPPING["search"]: # we check if category is specified, if not...we access de element by mapping ... location and name
			element_selector = self.MAPPING[menu_choice][element]
		else: # if category is specified, it's a form of search so we access the desired category and the desired product
			self.wait_and_click_element_by_selector(*self.MAPPING["search"][menu_choice]) # we access the category
			element_selector = (By.XPATH, f'//a[contains(text(),"{element}")]')
		self.wait_and_click_element_by_selector(*element_selector) # we access the element

	def check_current_url(self):
		current_url = self.chrome.current_url
		assert current_url == self.WEBPAGE, f'Field does not match, expected url: {self.WEBPAGE}, but we got {current_url}'

	# fuction to add text in a specified location from a specified menu
	def add_input_to_location(self, input_text, location, menu):
		element_selector = self.MAPPING[menu][location]
		self.chrome.find_element(*element_selector).send_keys(input_text)

	# function to treat alerts that shows on message confirmations
	def validate_confirmation_message(self, message):
		alert = WebDriverWait(self.chrome, 2).until(ec.alert_is_present())
		assert alert.text == message, f'Message confirmation error, expected: {message}, but we got: {alert.text}'
		alert.accept()

	# function to validate the video on About us top menu
	def validate_link(self):
		video_id = self.ABOUT_US_VIDEO[0]
		video_selector = self.ABOUT_US_VIDEO[1]
		presence = WebDriverWait(self.chrome, 2).until(ec.presence_of_element_located((video_id, video_selector)))
		assert presence, "Error, the about us video is not visible"
