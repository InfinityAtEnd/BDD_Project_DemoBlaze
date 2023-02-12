Feature: Testing the DemoBlaze website functionality

  Background:
    Given Homepage: I am on DemoBlaze start page

  @ALL @timed
  Scenario: Check that the DemoBlaze website fully loads in less than 2 seconds
    Then Homepage: The time needed to fully load the DemoBlaze webpage is less then "1" seconds

  @All @categories
  Scenario Outline: Check if categories are shown
    Then Homepage: I have visibility on category "<category_name_01>"
    Then Homepage: I have visibility on category "<category_name_02>"
    Then Homepage: I have visibility on category "<category_name_03>"
    Examples:
      | category_name_01 | category_name_02 | category_name_03 |
      | Phones           | Laptops          | Monitors         |

  @All @bottom_page
  Scenario: Check if bottom page elements are show correctly
    Then Homepage: About Us section is shown correctly
    Then Homepage: Get In Touch section is shown correctly
    Then Homepage: Product Store logo is shown correctly

  @All @top_menu @home
  Scenario: Check top menu Home function
    When Homepage: I click on element "Home" on "top menu"
    Then Homepage: I am returned to DemoBlaze homepage

  @ALL @top_menu @contact
  Scenario: Check top menu Contact function with inputs and accept
    When Homepage: I click on element "Contact" on "top menu"
    When Homepage: I enter "marian_test@gmail.com" in the "Contact Email" field of "contact popup"
    When Homepage: I enter "Marian Laurentiu" in the "Contact Name" field of "contact popup"
    When Homepage: I enter "I wish to become a programmer..............scratch that............... I WILL BECOME A PROGRAMER" in the "Message" field of "contact popup"
    When Homepage: I click on element "Send message" on "contact popup"
    Then Homepage: I get the confirmation message "Thanks for the message!!" and choose ok

  @ALL @top_menu @contact
  Scenario: Check top menu Contact function without inputs and cancel
    When Homepage: I click on element "Contact" on "top menu"
    When Homepage: I click on element "Close" on "contact popup"
    Then Homepage: I am returned to DemoBlaze homepage

  @ALL @top_menu @about_us
  Scenario: Check top menu About us function and close it
    When Homepage: I click on element "About us" on "top menu"
    Then Homepage: I have access to the video
    When Homepage: I click on element "Close" on "about us popup"
    Then Homepage: I am returned to DemoBlaze homepage

  @ALL @top_menu @log_in
  Scenario: Check top menu Log in with inputs and accept
    When Homepage: I click on element "Log in" on "top menu"
    When Homepage: I enter "current_user" in the "Username" field of "log in popup"
    When Homepage: I enter "easy_password" in the "Password" field of "log in popup"
    When Homepage: I click on element "Log in" on "log in popup"
    Then Homepage: I get the confirmation message "User does not exist." and choose ok

  @ALL @top_menu @log_in
  Scenario: Check top menu Log in without inputs and accept
    When Homepage: I click on element "Log in" on "top menu"
    When Homepage: I click on element "Log in" on "log in popup"
    Then Homepage: I get the confirmation message "Please fill out Username and Password." and choose ok

  @ALL @top_menu @log_in
  Scenario: Check top menu Log in function by clicking close
    When Homepage: I click on element "Log in" on "top menu"
    When Homepage: I click on element "Close" on "log in popup"
    Then Homepage: I am returned to DemoBlaze homepage

  @ALL @top_menu @sign_up
  Scenario: Check top menu Sign up with inputs and accept
    When Homepage: I click on element "Sign up" on "top menu"
    When Homepage: I enter "active_user" in the "Username" field of "sign up popup"
    When Homepage: I enter "complicated_password" in the "Password" field of "sign up popup"
    When Homepage: I click on element "Sign up" on "sign up popup"
    Then Homepage: I get the confirmation message "This user already exist." and choose ok

  @ALL @top_menu @sign_up
  Scenario: Check top menu Sign up without inputs and accept
    When Homepage: I click on element "Sign up" on "top menu"
    When Homepage: I click on element "Sign up" on "sign up popup"
    Then Homepage: I get the confirmation message "Please fill out Username and Password." and choose ok

  @ALL @top_menu @sign_up
  Scenario: Check top menu Sign up function by clicking close
    When Homepage: I click on element "Sign up" on "top menu"
    When Homepage: I click on element "Close" on "sign up popup"
    Then Homepage: I am returned to DemoBlaze homepage

  @ALL @top_menu @cart
  Scenario: Check top menu Cart function by placing order without items or inputs
    When Homepage: I click on element "Cart" on "top menu"
    Then Cartpage: I have "0" items in the cart list
    When Cartpage: I click on element "Place Order" on "cart page"
    When Cartpage: I click on element "Purchase" on "place order popup"
    Then Cartpage: I get the confirmation message "Please fill out Name and Creditcard." and choose ok

  @ALL @top_menu @cart
  Scenario Outline: Check top menu Cart function by placing order with inputs but no items
    When Homepage: I click on element "Cart" on "top menu"
    Then Cartpage: I have "0" items in the cart list
    When Cartpage: I click on element "Place Order" on "cart page"
    When Cartpage: I enter "<Name>" in the "Name" field of "place order popup"
    When Cartpage: I enter "<Country>" in the "Country" field of "place order popup"
    When Cartpage: I enter "<City>" in the "City" field of "place order popup"
    When Cartpage: I enter "<Credit card>" in the "Credit card" field of "place order popup"
    When Cartpage: I enter "<Month>" in the "Month" field of "place order popup"
    When Cartpage: I enter "<Year>" in the "Year" field of "place order popup"
    When Cartpage: I click on element "Purchase" on "place order popup"
    Then Cartpage: I get the confirmation message with correct "<Credit card>" and "<Name>" information and choose ok
    Examples:
      | Name   | Country | City | Credit card | Month     | Year |
      | Marian | Romania | Iasi | MasterCard  | Octombrie | 1986 |

  @ALL @top_menu @cart @test
  Scenario Outline: Check top menu Cart function by placing order with inputs and item
    When Homepage: I click on element "<Product>" on "<Category>"
    When Homepage: I click on element "Add to cart" on "product page"
    Then Homepage: I get the confirmation message "Product added" and choose ok
    When Homepage: I click on element "Cart" on "top menu"
    Then Cartpage: I have "1" items in the cart list
    When Cartpage: I click on element "Place Order" on "cart page"
    When Cartpage: I enter "<Name>" in the "Name" field of "place order popup"
    When Cartpage: I enter "<Country>" in the "Country" field of "place order popup"
    When Cartpage: I enter "<City>" in the "City" field of "place order popup"
    When Cartpage: I enter "<Credit card>" in the "Credit card" field of "place order popup"
    When Cartpage: I enter "<Month>" in the "Month" field of "place order popup"
    When Cartpage: I enter "<Year>" in the "Year" field of "place order popup"
    When Cartpage: I click on element "Purchase" on "place order popup"
    Then Cartpage: I get the confirmation message with correct "<Credit card>" and "<Name>" information and choose ok
    Examples:
      | Product      | Category | Name   | Country | City | Credit card | Month     | Year |
      | Nexus 6      | Phones   | Marian | Romania | Iasi | MasterCard  | Octombrie | 1986 |
      | Dell i7 8gb  | Laptops  | Marian | Romania | Iasi | MasterCard  | Octombrie | 1986 |
      | ASUS Full HD | Monitors | Marian | Romania | Iasi | MasterCard  | Octombrie | 1986 |