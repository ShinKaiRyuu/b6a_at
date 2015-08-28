Feature: Manage partners module
  # Test all stuff connected with products(add,view,update,delete,sort,etc...)

  Scenario: Open partners page
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Partners link
    Then I want to see Manage Partners page
    And I want to see all partners