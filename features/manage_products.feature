Feature: Manage products module
  # Test all stuff connected with products(add,view,update,delete,sort,etc...)

  Scenario: Open products page
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Products link
    Then I want to see Manage Products page
    And I want to see all products

  Scenario: Create new product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on Create new product button
    Then I want to see Create Product page
    When I create new product with UnicTitle, UnicSlug, UnicDescription, 1025.00, true
    Then I want to see View Product page
    And I want to see  product details with new data
    When I click on Manage products menu link
    Then I want to see Manage Products page
    Then I want to see created product in list

#  Scenario: Sorting products
#   Given I am logged in as Administrator
#   Given I am on Manage Products page
#   When I click on ID link
#   Then I want to see nothing changed
#   When I click on ID link
#   Then I want to see sorted by *ID* *descent* products
#   When I click on ID link
#   Then I want to see sorted by *ID* *ascent* products

  @wip
  Scenario: View product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on view link
    Then I want to see View Product page
   #And I want to see selected product details

  @wip
  Scenario: Update product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on update link
    Then I want to see Create Product page

  @wip
  Scenario: Delete product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on delete link
    Then I want to see dialog box
#    Given created product
#   When I click no
#   Then nothing changed
#   When I click on delete button for this product
#   Then I want to see dialog box
#   When I click yes
#   Then I want to see this product was deleted