from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_initialize import Browser


class BasePage(Browser):
	# function designed to wait for the page to fully load before trying to access element
	def wait_and_click_element_by_selector(self, by, selector):
		WebDriverWait(self.chrome, 5).until(ec.presence_of_element_located((by, selector)))
		self.chrome.find_element(by, selector).click()

	# used to change focus on the popup when we have to interact with it
	def change_focus(self):
		frame = self.chrome.window_handles[-1]
		self.chrome.switch_to.window(frame)
