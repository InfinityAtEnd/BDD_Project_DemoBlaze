# BDD_Project_DemoBlaze
# BDD Project developed on the DemoBlaze website

Objective: Testing different features on the [DemoBlaze](https://www.demoblaze.com/index.html) website. 

Browser used: Only Chrome.

Packages installed:
    - Selenium
    - webdriver_manager
    - behave
    - behave-html-formatter

Imports:
    - from time: perf_counter -> used for timed tests

Scenarios Details:
1)  Scenario: Check that the DemoBlaze website fully loads in less than 2 seconds
    - verify that the webpage will fully load in less then "n" seconds time
    - "n" can pe specified in the feature file
2)  Scenario Outline: Check if categories are shown
    - verify if all categories are visible to prevent one to not be shown or be shown with the wrong name
3)  Scenario: Check if bottom page elements are show correctly
    - verify if About Us section shows the desired information
    - verify if Get In Touch section shows the desired information
    - verify if Product Store logo is shown at correct size
4)  Scenario: Check top menu Home function
    - verify if clicking on top menu Home button will get us back to the homepage
5)  Scenario: Check top menu Contact function with inputs and accept
    - I open the contact form
    - I enter inputs in all the fields -> webpage doesn't have input validation so we will offer any input to verify if something can pe written in the input fields
    - I get the confirmation that the message has been send
6)  Scenario: Check top menu Contact function without inputs and cancel
    - I open the contact form
    - I leave all the input fields empty
    - I am returned to homepage after I click the Close button
7)  Scenario: Check top menu About us function and close it
    - I click on About us top menu
    - I check if the video is visible
    - I close the popup and check if I'm back to the homepage
8)  Scenario: Check top menu Log in with inputs and accept
    - I click on Log in in top menu
    - I enter inputs in all fields -> webpage doesn't have input validation so we will offer any input to verify if something can pe written in the input fields
    - I click Log in and verify the message shown
9)  Scenario: Check top menu Log in without inputs and accept
    - I click on Log in in top menu
    - I click close without entering any input data
    - I verify the message requesting for input data to be filled in
10) Scenario: Check top menu Log in function by clicking close
    - I click on Log in in top menu
    - I click close without doing any other actions
    - I check that I'm returned to the home page
11) Scenario: Check top menu Sign up with inputs and accept
    - I click on Sign up in top menu
    - I enter inputs in all fields
    - I click Sign up button and verify the message shown
12) Scenario: Check top menu Sign up without inputs and accept
    - I click on Sign up in top menu
    - I click close without entering any input data
    - I verify the message requesting for input data to be filled in
13) Scenario: Check top menu Sign up function by clicking close
    - I click on Sign up in top menu
    - I click close without doing any other actions
    - I check that I'm returned to the home page
14) Scenario: Check top menu Cart function by placing order without items or inputs
    - I click on Cart in top menu
    - I click on Place Order and then click Purchase
    - I get the message to fill name and credit card input fields
15) Scenario Outline: Check top menu Cart function by placing order with inputs but no items
    - I click on Cart in top menu
    - I check that I have no items in the cart
    - I click Place Order, fill out all the input field then click Purchase
    - I get the confirmation message with correct name and credit card information
16) Scenario Outline: Check top menu Cart function by placing order with inputs and item
    - I look for the specified item on the specified category and add it to the cart
    - I click on Cart in top menu
    - I check that I have an item to the cart list
    - I click Place Order, fill out all the input field then click Purchase
    - I get the confirmation message with correct name and credit card information

