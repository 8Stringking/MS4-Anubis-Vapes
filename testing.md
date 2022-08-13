# Contents

* [**Testing**](#testing)
    * [**Manual Testing**](#manual-testing)
    * [**Development Testing**](#development-testing)
    * [**Deployment Testing**](#deployment-testing)
    * [**Automated Testing**](#automated-testing)
    * [**Code Validation**](#code-validation)

<a name="Testing"></a>
# Testing
  [Go to the top](#contents)

<a name="Manual-Testing"></a>
## Manual Testing
  [Go to the top](#contents)

In the development AND deployed versions of this site, one way of manual testing i carried out is to physically perform the tasks that were required of the site and show that they were successful,  and the proof of this is below:

![login-test](documentation/testing_image_files/manual_testing/login-test.jpg)

This first image shows a successful login and that it has been tested

![sign-out](documentation/testing_image_files/manual_testing/sign-out-confirmed.jpg)

This image shows a successful sign out of an account and that the site notifies the user

![wishlist](documentation/testing_image_files/manual_testing/add-to-wishlist-test.jpg)

This image shows a product successfully being added to the users wishlist

![remove-wishlist](documentation/testing_image_files/manual_testing/remove-wishlist-item-test.jpg)

This image shows a product successfully being removed from the wishlist

![add-to-cart](documentation/testing_image_files/manual_testing/add-to-cart-test.jpg)

This image shows a product successfully being added to the cart 

![update-cart](documentation/testing_image_files/manual_testing/update-cart-test.jpg)

This shows the cart successfully updating the quantity of products 

![remove-cart](documentation/testing_image_files/manual_testing/remove-cart-test.jpg)

This image shows a product successfully being removed from the cart

![add-product](documentation/testing_image_files/manual_testing/add-product-test.jpg)

This image shows a product has successfully been added to the site

![edit-product](documentation/testing_image_files/manual_testing/edit-product-test.jpg)

This image shows a product has successfully been edited on the site

![product-delete](documentation/testing_image_files/manual_testing/product-delete-test.jpg)

This image shows a product successfully being deleted from the site

![price-error](documentation/testing_image_files/manual_testing/price-error-reminder-add-product.jpg)

This image shows that when adding a product the admin user must enter the correct amount of numbers

![checkout-success](documentation/testing_image_files/manual_testing/checkout-success.jpg)

This image shows a successfull payment being made to the site and that the user is given a confirmation of their order and a order number.

<a name="development-testing"></a>
## Development Testing
  [Go to the top](#contents)

Test            | Outcome                          | Result
--------------- | -------------------------------- | ------------
Navigation Bar  | Does the nav bar navigate to each page?| Pass 
Buttons | Does all buttons function as intended consistantly?| Pass
User Story 1a | View a list of products to select which ones to buy | Pass
User story 2a | View a specific category to find what a user wants easily | Pass
User Story 3a | View specifc product details, eg. price, description | Pass
User story 4a | Sort a list of items. By price, alphabetically, rating, and category | Pass
User story 5a | To be able to search for an item | Pass
User story 6a | Select a quantity of an item to buy | Pass
User story 7a | To view items in my bag including the total of products and price | Pass
User story 8a | To be able to enter payment details to purchase items | Pass
User story 9a | To see my order confirmation including what the user has bought | Pass
User story 1b | Be able to register the users account | Pass
User story 2b | To be able to log in/out of the users account | Pass
User story 3b | To recover a lost Password | Pass
User story 4b | Get a confirmation email to aid in registering the users account | Pass
User story 5b | Have a personal user profile | Pass
User story 6b | To save delivery information to profile to speed up the checkout process | Pass
User story 7b | To be able to place items in their designated wishlist | Pass
User story 8b | To be able to view their wishlist | Pass
User story 1c | To be able to add a product with its information to the website | Pass
User story 2b | To be able to edit a product and its information | Pass
User story 3c | To delete a product and its information | Pass
Responsiveness | Is the application responsive across all devices? | Pass
Accessibility | Is the application accessible to all users? | Pass (see accessibility section)
Error Handling | In the applications development is the error handlers to handle internal server errors and 404 errors? | Pass (404.html, 500.html)

<a name="deployment-testing"></a>
## Deployment Testing
  [Go to the top](#contents)

Test            | Outcome                          | Result
--------------- | -------------------------------- | ------------
Checked against development version | Has the development testing criteria been applied to the deployed version? Any issues? | Pass, No issues
Visual Checks | Has visual checks been carried out in full on deployment version? | Yes, Pass
Code checked | Has the code been checked for errors? | Yes, Pass (errors have been noted that i have been unable to change, see code validation section)
Console errors | Is there any errors in the console? | No, Pass
Stability | Does using the forward and backward keys break the site? | No, Pass
Stability | Does the site work as intended? | Yes, Pass
Security | Can only logged in users access the pages on the application (minus the registration page) such as wishlist app and profile pages | Yes, Pass
Error Handling | Does the application gracefully handle errors that the user may cause in the application and redirect the user back to the site without the use of the browsers navigation buttons? | Yes, Pass 
Error Handling | Can a user break the site using URL manipulation? | No, this will be handled by 404 and internal server error handlers, Pass
Links | are any of the links (on login page/register page/error page) broken and work as intended? | None broken, and work as intended, Pass


<a name="Automated-Testing"></a>
## Automated Testing
  [Go to the top](#contents)

In this project their are 3 instances of automated testing. I would like to note that if given more time i would have liked to have expanded on this, however the deadline was extremely tight.

The apps that i have tested are:
  - Home app
  - Bag app
  - Products app

What these tests tested:
  - That the app being tested renders the correct template

These tests are all in a separate file called test_views.py within the relevant app folders, and have been written using Python.

The evidence of the terminal results are below:

![home-app-test](documentation/testing_image_files/automated_testing/home-app-index-test-python-results.jpg)

- This image shows the results of the home app being tested on the terminal in gitpod

![bag-app-test](documentation/testing_image_files/automated_testing/bag-app-view-bag-test-python-results.jpg)

- This image shows the results of the bag app being tested on the terminal in gitpod

![products-app-test](documentation/testing_image_files/automated_testing/products-app-all-products-test-python-results.jpg)

- This image shows the results of the product app being tested on the terminal in gitpod

<a name="code-validation"></a>
## Code Validation
  [Go to the top](#contents)

### CSS Validation

The following images shows the validations for the css:

- Project level CSS validation

![project-css](documentation/testing_image_files/code_validation/project-level-css.jpg)

- Profile level CSS validation

![profile-css](documentation/testing_image_files/code_validation/profile-level-css.jpg)

- Checkout level CSS validation

![checkout-css](documentation/testing_image_files/code_validation/checkout-level-css.jpg)


### HTML Validation

As stated in the bugs section in the html validation across the site, there is warnings for the javascript in the page. Where i have been able to, i have moved as much javascript out of my html pages as possible using a update_and_remove file. However in every page of the site i have had to leave some of the javascript where it is. In attempting to remove this javascript and separating it, it broke the toasts function that gives messages to the users on their actions, and other functions as well. After extensive research and attempts i was unable to fix this issue. This also causes the javascript not to pass through jslint without errors. So i have made the decision to leave this, as the site functions in its current state and again i havent found a way to fix this issue.

![checkout-page](documentation/testing_image_files/code_validation/html_validation/checkout-page.jpg)

- This image is for the checkout page. As stated in the Bugs section. This page throws up an error involving placeholder content on select element at this time. I have left this in place mainly as this particular piece of code has come from the Django/bootstrap documentation and is also present in the boutique ado project. I have tried to remedy this issue but again due to a fix breaking the country select box i have left this as it is. I can only determine that this is a limitation of Django and bootstrap code as i am unable to fix this issue even with extensive research and many attempted fixes.

The checkout page also throws a warning for an empty heading however this is in place for the loading spinner that displays on screen when making a payment. I have tried to remedy this issue but again every fix i have attempted has broken this function.

![home-page](documentation/testing_image_files/code_validation/html_validation/home-page.jpg)

- This image is for the home page html validation

![login-page](documentation/testing_image_files/code_validation/html_validation/login-page.jpg)

- This image is for the login page html validation

![logout-page](documentation/testing_image_files/code_validation/html_validation/logout-page.jpg)

- This image is for the logout page html validation

![register-page](documentation/testing_image_files/code_validation/html_validation/register-page.jpg)

- This image is for the registration page html validation

![password-reset](documentation/testing_image_files/code_validation/html_validation/password-reset-page.jpg)

- This image is for the password reset page html validation

![account-profile](documentation/testing_image_files/code_validation/html_validation/account-profile.jpg)

- This image is for the account profile page html validation

![all-products](documentation/testing_image_files/code_validation/html_validation/all-products.jpg)

- This image is for the all products page html validation

![product-detail](documentation/testing_image_files/code_validation/html_validation/product-detail-page.jpg)

- This image is for the products detail page html validation

![add-product](documentation/testing_image_files/code_validation/html_validation/add-product.jpg)

- This image is for the add products page html validation

![edit-product](documentation/testing_image_files/code_validation/html_validation/edit-product-page.jpg)

- This image is for the edit product page html validation

![cart](documentation/testing_image_files/code_validation/html_validation/cart.jpg)

- This image is for the cart page html validation

![checkout-success](documentation/testing_image_files/code_validation/html_validation/checkout-success.jpg)

- This image is for the checkout success page html validation

![wishlist](documentation/testing_image_files/code_validation/html_validation/wishlist-page.jpg)

- This image is for the wishlist page html validation

### Pep8 Validation

Th efollowing images show the evidence for the pep8 validation across the site:

![home-views](documentation/testing_image_files/pep8_validation/home-views.jpg)

- This image is for the home app views

![product-models](documentation/testing_image_files/pep8_validation/product-models.jpg)

- This image is the for product app models

![product-views](documentation/testing_image_files/pep8_validation/product-views.jpg)

- This image is for the product app views

![profile-models](documentation/testing_image_files/pep8_validation/product-models.jpg)

- This image is for the profile apps models

![profile-views](documentation/testing_image_files/pep8_validation/profile-views.jpg)

- This image is for the profile app views

![wishlist-models](documentation/testing_image_files/pep8_validation/wishlist-models.jpg)

- This image is for the wishlist apps models

![wishlist-views](documentation/testing_image_files/pep8_validation/wishlist-views.jpg)

- This image is for the wishlist apps views

![bag-views](documentation/testing_image_files/pep8_validation/bag-view.jpg)

- This image is for the bag views

![checkout-models](documentation/testing_image_files/pep8_validation/checkout-models.jpg)

- This image is for the checkout apps models

![checkout-views](documentation/testing_image_files/pep8_validation/checkout-view-issue-1.jpg)

- This image is for the checkout apps views page. As you can see pep8 has identified a long line on line 75. I have attempted many times to remedy this issue, and even after extensive research i was unable to find a fix that wouldnt break the checkout app. All previous attempts to fix this resulted in the checkout app not working properly and was unable to process any payments, so ive had to leave it in and document the error.