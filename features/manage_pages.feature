Feature: Manage pages module

  @done @partner @partner_open_partners_page
  Scenario: Open pages page
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Pages link
    Then I want to see 'Manage Pages' page
    And I want to see table with all pages in it
######
  Scenario: View pages. Sort records by order ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on order sort
    Then i want to see sorted pages by order and ascending
    When I click on order sort
    Then i want to see sorted pages by order and descending

  Scenario: View users. Sort records by name ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on name sort
    Then i want to see sorted pages by name and ascending
    When I click on name sort
    Then i want to see sorted pages by name and descending

  Scenario: View users. Sort records by createdby  ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on createdby sort
    Then i want to see sorted pages by createdby and ascending
    When I click on createdby sort
    Then i want to see sorted pages by createdby and descending

  Scenario: View users. Sort records by updatedby time ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on updatedby sort
    Then i want to see sorted pages by updatedby and ascending
    When I click on updatedby sort
    Then i want to see sorted pages by updatedby and descending
######