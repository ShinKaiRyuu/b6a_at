Feature: Products
  # Test all stuff connected with products(add,view,update,delete,sort,etc...)

  Scenario: Open products page
    Given I am logged in as Administrator
    When I click on Manage_Site link
    When I click on Manage_Products link
    Then I want to see Manage Products page

  Scenario: Create new product
    Given I am logged in as Administrator
    When I click on Manage_Site link
    When I click on Manage_Products link
    Then I want to see Manage Products page
    When I click on Create_new_product button
    Then I want to see Create Product page
    When I create new product with Title1, Slug1, Description, 1025, true
    Then I want to see View Product page
    And I want to see  product details with Title1, Slug1, Description, 1025, true
    When I click on Manage_products_menu link
    Then I want to see Manage Products page
    Then I want to see product with Title1 in list

#  Scenario: Sorting products
#   # TODO write products sorting scenario
#
  Scenario: View product
    Given I am logged in as Administrator
    When I click on Manage_Site link
    When I click on Manage_Products link
    Then I want to see Manage Products page
    When I click on view link
    Then I want to see View Product page
   #And I want to see selected product details

#
  Scenario: Update product
      Given I am logged in as Administrator
      When I click on Manage_Site link
      When I click on Manage_Products link
      Then I want to see Manage Products page
      When I click on update link
      Then I want to see Create Product page
#
#  Scenario: Delete product
#   #TODO write delete product scenario