Feature: Manage pages module

  @done @pages @open_pages_page
  Scenario: Open pages page
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Pages link
    Then I want to see 'Manage Pages' page
    And I want to see table with all pages in it

  @done @pages @sorting @sorting_by_order @sorting_pages
  Scenario: Sort records by order ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on order sort
    Then i want to see sorted data by order and ascending
    When I click on order sort
    Then i want to see sorted data by order and descending

  @done @pages  @sorting  @sorting_by_name @sorting_pages
  Scenario: Sort records by name ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on name sort
    Then i want to see sorted data by name and ascending
    When I click on name sort
    Then i want to see sorted data by name and descending

  @done @pages  @sorting @sorting_by_createdby @sorting_pages
  Scenario: Sort records by createdby  ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on createdby sort
    Then i want to see sorted data by createdby and ascending
    When I click on createdby sort
    Then i want to see sorted data by createdby and descending

  @done @pages  @sorting @sorting_by_updatedby @sorting_pages
  Scenario: Sort records by updatedby time ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and ascending
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and descending
