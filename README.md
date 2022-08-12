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

### User Stories For A Shopper 

Number | User Stories                               
-------| ----------------------------------------------
1 | View a list of products to select which ones to buy |
2 | View a specific category to find what a user wants easily |
3 | View specifc product details, eg. price, description |
4 | Sort a list of items. By price, alphabetically, rating, and category |
5 | To be able to search for an item |
6 | Select a quantity of an item to buy |
7 | To view items in my bag including the total of products and price |
8 | To be able to enter payment details to purchase items |
9 | To see my order confirmation including what the user has bought |


### User Stories 




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




<a name="methods-for-creating-the-site"></a>
# Methods For Creating The Site
  [Go to the top](#contents)



<a name="Testing"></a>
# Testing
  [Go to the top](#contents)

 Please refer to [**Testing **](testing.md) for more information on testing.