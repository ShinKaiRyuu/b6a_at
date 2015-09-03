Feature: Manage partners module
  # Test all stuff connected with products(add,view,update,delete,sort,etc...)

  Scenario: Open partners page
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Partners link
    Then I want to see Manage Partners page
    And I want to see all partners

  Scenario: Create partner
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Partners link
    Then I want to see Manage Partners page
    When I click on Create Partner button
    Then I want to see Create Partner page
    When I create new partner
    Then I want to see Manage Partners page
    And I want to see created partner in list

  Scenario: Delete user
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I delete created user
    Then I want to see dialog box and click No
    Then I want to see user in list is not deleted
    When I delete created user
    Then I want to see dialog box and click Yes
    Then I want to see user is deleted