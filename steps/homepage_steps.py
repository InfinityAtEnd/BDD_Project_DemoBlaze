from behave import *


@Given("Homepage: I am on DemoBlaze start page")
def step_impl(context):
	context.homepage_object.navigate_to_start_page()


@When("Homepage: I start the timer for reloading the DemoBlaze website")
def step_impl(context):
	context.homepage_object.wait_for_homepage()


@Then('Homepage: The time needed to fully load the DemoBlaze webpage is less then "{time}" seconds')
def step_impl(context, time):
	context.homepage_object.get_elapsed_time(time)


@Then('Homepage: I have visibility on category "{category_name}"')
def step_impl(context, category_name):
	context.homepage_object.check_visibility_of(category_name)


@Then("Homepage: About Us section is shown correctly")
def step_impl(context):
	context.homepage_object.about_us()


@Then("Homepage: Get In Touch section is shown correctly")
def step_impl(context):
	context.homepage_object.get_in_touch()


@Then("Homepage: Product Store logo is shown correctly")
def step_impl(context):
	context.homepage_object.logo()


@When('Homepage: I click on element "{element}" on "{menu_choice}"')
def step_impl(context, element, menu_choice):
	context.homepage_object.click_on_element(element, menu_choice)


@Then("Homepage: I am returned to DemoBlaze homepage")
def step_impl(context):
	context.homepage_object.check_current_url()


@When('Homepage: I enter "{input_text}" in the "{location}" field of "{menu}"')
def step_impl(context, input_text, location, menu):
	context.homepage_object.add_input_to_location(input_text, location, menu)


@Then('Homepage: I get the confirmation message "{message}" and choose ok')
def step_impl(context, message):
	context.homepage_object.validate_confirmation_message(message)


@Then("Homepage: I have access to the video")
def step_impl(context):
	context.homepage_object.validate_link()

