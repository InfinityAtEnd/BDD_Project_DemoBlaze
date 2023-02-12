from behave import *


@When('Cartpage: I click on element "{element}" on "{menu_choice}"')
def step_impl(context, element, menu_choice):
	context.cartpage_object.click_on_element(element, menu_choice)

@Then('Cartpage: I get the confirmation message "{message}" and choose ok')
def step_impl(context, message):
	context.cartpage_object.validate_confirmation_message(message)

@Then('Cartpage: I have "{number}" items in the cart list')
def step_impl(context, number):
	context.cartpage_object.verify_cart_nr_of_items(number)


@When('Cartpage: I enter "{input_text}" in the "{location}" field of "{menu}"')
def step_impl(context, input_text, location, menu):
	context.cartpage_object.add_input_to_location(input_text, location, menu)

@Then('Cartpage: I get the confirmation message with correct "{credit_card}" and "{name}" information and choose ok')
def step_impl(context, credit_card, name):
	context.cartpage_object.verify_purchase_message(credit_card, name)

