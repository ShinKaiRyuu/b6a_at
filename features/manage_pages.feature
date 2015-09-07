Feature: Manage pages module

  @done @pages @open_pages_page
  Scenario: Open Manage pages page and view pages records
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Pages link
    Then I want to see 'Manage Pages' page
    And I want to see table with data

  @done @pages @sorting @sorting_by_order @sorting_pages
  Scenario: Sort pages records by order ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on order sort
    Then i want to see sorted data by order and ascending
    When I click on order sort
    Then i want to see sorted data by order and descending

  @done @pages  @sorting  @sorting_by_name @sorting_pages
  Scenario: Sort pages records by name ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on name sort
    Then i want to see sorted data by name and ascending
    When I click on name sort
    Then i want to see sorted data by name and descending

  @done @pages  @sorting @sorting_by_createdby @sorting_pages
  Scenario: Sort pages records by createdby ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on createdby sort
    Then i want to see sorted data by createdby and ascending
    When I click on createdby sort
    Then i want to see sorted data by createdby and descending

  @done @pages  @sorting @sorting_by_updatedby @sorting_pages
  Scenario: Sort pages records by updatedby ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and ascending
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and descending

  @wip
  Scenario: Create new parent page
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on Create Page button
    Then I want to see 'Create Page' page
    When I create new page
    Then I want to see 'Manage Pages' page
    And I want to see created page in list
    When I click on Public pages link
    Then I want to see created page in link list
    Then I want to see created page and it content
    When I click on logout link
    Then I want to see 'Main' page
    And I want to see create page in header

  @wip
  Scenario: Drag n drop
    Given created parent page
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I dragndrop created page to top position
    Then I want to see created page in top position
    When I click on Public pages link
    Then I want to see created page in top of list

