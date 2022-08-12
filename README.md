![am-i-responsive](documentation/readme_image_files/am-i-responsive.jpg)

# Introduction

Welcome to the online e-commerce store Anubis Vapes! This is an online store using the Django framework alongside a postgresql database. In this shop not only can the user select as many items to purchase and use the secure checkout to pay for their items. The user can also register an account with Anubis Vapes to be able to pick items and place them in their own wishlist which will save on their account, and also have the ability to pre-save their delivery information to make purchases even easier!


Live site can be viewed here: https://anubis-vapes.herokuapp.com/

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [**Purpose**](#purpose)
    * [**User Stories**](#user-stories)
    * [**Wireframes**](#wireframes)
    * [**Web Design**](#web-design)
    * [**Data-Schema**](#data-schema)
    * [**Accessibility**](#accessibility)
* [**Website Walkthrough**](#website-walkthrough)
* [**Methods For Creating The Site**](#methods-for-creating-the-site)
* [**Testing**](#testing)
    * [**Development Testing**](#development-testing)
    * [**Deployment Testing**](#deployment-testing)
    * [**Code Validation**](#code-validation)
* [**Bugs**](#bugs)
* [**Deployment**](#deployment)

<a name="user-experience-ux"></a>
# User Experience (UX) design
<a name="purpose"></a>
## Purpose
  [Go to the top](#contents)

The main purpose of this app is an e-commerce store, but also a site that allows users to shop for vape items to stop them smoking. I used to smoke 50g tobacco a week and since vaping my health has improved drastically, so to provide a completely accessible site, that delivers some great products that everyone can see and use is very important to me. 

The target audience is people that already vape, or people that want to stop smoking themselves, but also people who suffer medical conditions who may need to stop smoking. These can be people from all ages.

This is also a vape shop that has been designed with security in mind. From the secure checkout, and to pages that have restricted access for the users to keep their information safe, such as the wishlist and user profile (including delivery information)

<a name="user-stories"></a>
## User Stories
  [Go to the top](#contents)

### User Stories For A Shopper and Anonymous Users

Number | User Stories                               
-------| ----------------------------------------------
1a | View a list of products to select which ones to buy |
2a | View a specific category to find what a user wants easily |
3a | View specifc product details, eg. price, description |
4a | Sort a list of items. By price, alphabetically, rating, and category |
5a | To be able to search for an item |
6a | Select a quantity of an item to buy |
7a | To view items in my bag including the total of products and price |
8a | To be able to enter payment details to purchase items |
9a | To see my order confirmation including what the user has bought |


### User Stories For Registered Users

Number | User Stories                               
-------| ----------------------------------------------
1b | Be able to register the users account |
2b | To be able to log in/out of the users account |
3b | To recover a lost Password |
4b | Get a confirmation email to aid in registering the users account |
5b | Have a personal user profile |
6b | To save delivery information to profile to speed up the checkout process |
7b | To be able to place items in their designated wishlist |
8b | To be able to view their wishlist |

### User Stories For Site Administration

Number | User Stories                               
-------| ----------------------------------------------
1c | To be able to add a product with its information to the website |
2c | To be able to edit a product and its information |
3c | To delete a product and its information |


<a name="wireframes"></a>
## WireFrames
  [Go to the top](#contents)

![home-screen](documentation/readme_image_files/wireframes/home-screen.jpg)

![products-page](documentation/readme_image_files/wireframes/products-page.jpg)

![product-detail](documentation/readme_image_files/wireframes/product-detail.jpg)

![card-design](documentation/readme_image_files/wireframes/card-design.jpg)

![sign-in](documentation/readme_image_files/wireframes/sign-in.jpg)

![register](documentation/readme_image_files/wireframes/register.jpg)

![account-profile](documentation/readme_image_files/wireframes/account-profile.jpg)

![add-product](documentation/readme_image_files/wireframes/add-a-product.jpg)

![wishlist](documentation/readme_image_files/wireframes/wishlist.jpg)

![cart](documentation/readme_image_files/wireframes/cart.jpg)

![checkout](documentation/readme_image_files/wireframes/checkout.jpg)

![checkout-success](documentation/readme_image_files/wireframes/checkout-success.jpg)

<a name="web-design"></a>
## Web Design
  [Go to the top](#contents)

This application has been designed with the following main principles:
- Simple and easy to navigate
- Completely responsive across all devices
- A very accessible site for everyone to use and read
- To demonstrate great vape products for everyone
- To be secure

The design of this website has been very simple. The main cause of this has been the deadline to which i have been working to being incredibly tight, so what i focused on was the site being fully functional, easy to read and to be as accessible as i could make it. In the future i will look to improve on the aesthetics of the site.

I have chosen to make the product cards quite large, this has been done to mainly have the users main focus be on the products themselves, and for the vape juice, to really drive home to the user the flavours of which they are looking at. If  had more funds i would like to have had designed a vape bottle to use in its place, however i do feel having a representation of the flavours does provide the user with a more apitising view of what flavours are on offer.

With accessibility in mind and having the ability for this site to be read by screen readers as much as possible, this is the reason for the text of the website being black and quite basic.

<a name="data-schema"></a>
## Data-Schema
  [Go to the top](#contents)

![entity-relationship-diagram](documentation/readme_image_files/schema/entity-relationship-diagram.jpg)

Above is the data schema for the relational database in the Anubis Vapes application.

I have not added a key to this Entity Relationship Diagram as i have labelled each variable next to the name as to what each individual variable is.

What this diagram describes is that the relationship between the profile and wishlist is a 1 to 1 relationship meaning for each profile you can create 1 wishlist. This is also the case for the relationship between the profile and user model.

For the the relationship between the products and the wishlist, this is a one to many relationship meaning many products can go into 1 wishlist. This is also the same between the products and categories, as many products can go into one category.

This diagram also shows that per order only 1 order number is assigned showing a 1 to 1 relationship.

Also this shows that the checkout is updated by using the orderLineitem model as a 1 to 1 relationship. 

<a name="accessibility"></a>
## Accessibility
  [Go to the top](#contents)

![home-page](documentation/readme_image_files/accessibility/home-page.jpg)

![product-detail-page](documentation/readme_image_files/accessibility/product-detail.jpg)

![wishlist](documentation/readme_image_files/accessibility/wishlist-page.jpg)

Above you can see that across the site i was successful in making this site accessible in the development stage which has carried over into the deployed stage.

However below are the only 2 pages in the site that isnt a 100% accessible. In the products page, i was unable to give the link a decernable name without causing errors in the HTML validation, even after extensive research and many attempts, however this page still reads at 97%. In the checkout page the only issue i was not able to fix was the picture of the product in the checkout. Again after many attempts and much research i was unable to find this solution, this page however still reads at 98%.

![products-page](documentation/readme_image_files/accessibility/products-page.jpg)

![checkout-page](documentation/readme_image_files/accessibility/checkout-page.jpg)


<a name="website-walkthrough"></a>
# Website Walkthrough
  [Go to the top](#contents)

![home-page](documentation/readme_image_files/walkthrough/home-page.jpg)

![products-page](documentation/readme_image_files/walkthrough/logged-in-products-page.jpg)

This is the products page (while logged in as admin) this satisfies user stories 1a (for this user story obviously without the user logged in they would not see the edit/delete bvuttons),3c,2c, 5a and 7b

![products-detail](documentation/readme_image_files/walkthrough/logged-in-product-detail.jpg)

This is the products detail page (while logged in as admin) this satisfies user stories 3a,6a(for this user story obviously without the user logged in they would not see the edit/delete bvuttons) , 2c and 3c

![sign-in](documentation/readme_image_files/walkthrough/sign-in.jpg)

This is the sign in page for the website and this satisfies user stories 2b, with access to 3b

![register](documentation/readme_image_files/walkthrough/register.jpg)

This is the registration page and this satisfies user stories 1b, which upon completion would recieve a confirmation which satisfies user story 4b

![profile](documentation/readme_image_files/walkthrough/profile.jpg)






<a name="methods-for-creating-the-site"></a>
# Methods For Creating The Site
  [Go to the top](#contents)

* [HTML5](https://en.wikipedia.org/wiki/HTML) (was used for structuring and presenting content of the website)
* [CSS](https://en.wikipedia.org/wiki/CSS) (used for the styling of the content)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript) (used for the initialisation of features such as quantity buttons)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) (used for programming the application through Django)
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) (used as the framework for this project)
* [Google Fonts](https://fonts.google.com/) (used for all the font styling within the project)
* [Chrome](https://www.google.com/intl/en_uk/chrome/) (used to debug and test the source code and to test site responsiveness)
* [GitHub](https://github.com/) (used to create the repository and store the projects code after pushed from Git)
* [Heroku](https://id.heroku.com/login) (Used for deployment of the application alongisde Github)
* [Gitpod](https://www.gitpod.io/) (used for the editing of code within the project for the site)
* [W3C Markup](https://validator.w3.org/) (used for validating the html5 code)
* [CSS Validator](https://www.cssportal.com/css-validator/) (used for validating the CSS code)
* [JSHint](https://jshint.com/) (this was also used for validating javascript code and double checking results from JSLint)
* [Am I Responsive](http://ami.responsivedesign.is/#) (used to generate the live site images, and also used to test responsiveness)
* [Balsamiq](https://balsamiq.com/) (This was used to generate the wireframes)
* [Dropbox](https://www.dropbox.com) (This was used to host the product images before being pushed to Amazon Web Services)
* [PeP8 online](http://pep8online.com/) (Used to check and prove pep8 compliance for models,routes.py files)
* [Miro](https://miro.com) (This was used to create the entity relationship diagram)
* [Amazon Web Services](https://aws.amazon.com/?nc2=h_lg) (This was used, specifically the S3 bucket to host all images on the site and all static files such as js and css files)

<a name="Testing"></a>
# Testing
  [Go to the top](#contents)

 Please refer to [**Testing **](testing.md) for more information on testing.