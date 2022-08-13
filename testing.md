# Contents

* [**Testing**](#testing)
    * [**Manual Testing**](#manual-testing)
    * [**Automated Testing**](#automated-testing)
    * [**Code Validation**](#code-validation)
    * [**Development Testing**](#development-testing)
    * [**Deployment Testing**](#deployment-testing)

<a name="Testing"></a>
# Testing
  [Go to the top](#contents)

<a name="Manual-Testing"></a>
## Manual Testing
  [Go to the top](#contents)

In the development and deployed versions of this site, one way of manual testing i carried out is to physically perform the tasks that were required of the site and show that they were successful,  and the proof of this is below:

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

This first image shows the validations for the css:

- Project level CSS validation

![project-css](documentation/testing_image_files/code_validation/project-level-css.jpg)

- Profile level CSS validation

![profile-css](documentation/testing_image_files/code_validation/profile-level-css.jpg)

- Checkout level CSS validation

![checkout-css](documentation/testing_image_files/code_validation/checkout-level-css.jpg)



