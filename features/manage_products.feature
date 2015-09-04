Feature: Manage products module

  @wip
  Scenario: View products
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Products link
    Then I want to see Manage Products page
    And I want to see all products

  @wip
  Scenario: Create new product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on Create new product button
    Then I want to see Create Product page
    When I create new product
    Then I want to see Manage Products page
    Then I want to see created product in list

  @wip
  Scenario: Delete product
    Given created product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I delete created product
    Then I want to see dialog box and click No
    Then I want to see product in list is not deleted
    When I delete created product
    Then I want to see dialog box and click Yes
    Then I want to see product is deleted

  @wip
  Scenario: View product
    Given created product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I view product
    Then I want to see Create Product page
    And I want to see product details

  @wip
  Scenario: Update product
    Given created product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I update product
    Then I want to see Create Product page
    And I want to see product details
    Then I want to change title description price enabled
    And I am on Manage Products page
    Then I want to see updated product in list

  Scenario: Filter products by order
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I write 1 in order Filter
    Then I want to see filtered products

  Scenario: Filter products by title
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I write New in title Filter
    Then I want to see filtered products

  Scenario: Filter products by price
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I write 1025 in price Filter
    Then I want to see filtered products

  Scenario: Filter products by created_by
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I write admin in created_by Filter
    Then I want to see filtered products

  Scenario: Filter products by updated_by
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I write admin in updated_by Filter
    Then I want to see filtered products

  Scenario: Filter products by enabled
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I select Enabled in enabled Filter
    Then I want to see filtered products

  Scenario: Filter products by disabled
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I select Disabled in enabled Filter
    Then I want to see filtered products


  @wip
#  Scenario: Sorting products
#   Given I am logged in as Administrator
#   Given I am on Manage Products page
#   When I click on ID link
#   Then I want to see nothing changed
#   When I click on ID link
#   Then I want to see sorted by *ID* *descent* products
#   When I click on ID link
#   Then I want to see sorted by *ID* *ascent* products