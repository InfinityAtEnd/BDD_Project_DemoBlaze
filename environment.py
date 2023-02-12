from browser_initialize import Browser
from pages.homepage import HomePage
from pages.cartpage import CartPage

# method executed before every test, it initialize the browser and everything else needed for the tests
def before_all(context):
	context.browser = Browser()
	context.homepage_object = HomePage()
	context.cartpage_object = CartPage()


# method executed after every test, it closes the browser to offer a clean startup for the following test
def after_all(context):
	context.browser.close()