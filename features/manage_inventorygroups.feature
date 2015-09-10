Feature: Manage inventorygroups module

    @done @pages @open_pages_page
  Scenario: Open Manage pages page and view pages records
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Inventory Group link
    Then I want to see 'Inventory Group' page
    And I want to see table with data

   @wip @sorting @sorting_by_id @sorting_inventorygroups
  Scenario: Sort inventorygroup records by id ascending/descending
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I click on id sort
    Then i want to see sorted data by id and ascending
    When I click on id sort
    Then i want to see sorted data by id and descending

  @wip @sorting @sorting_by_name @sorting_inventorygroups
  Scenario: Sort inventorygroup records by name ascending/descending
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I click on name sort
    Then i want to see sorted data by name and ascending
    When I click on name sort
    Then i want to see sorted data by name and descending

  @wip @sorting @sorting_by_partner @sorting_inventorygroups
  Scenario: Sort inventorygroup records by partner ascending/descending
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I click on partner sort
    Then i want to see sorted data by partner and ascending
    When I click on partner sort
    Then i want to see sorted data by partner and descending

  @wip @sorting @sorting_by_createdby @sorting_inventorygroups
  Scenario: Sort inventorygroup records by partner ascending/descending
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I click on createdby sort
    Then i want to see sorted data by createdby and ascending
    When I click on createdby sort
    Then i want to see sorted data by createdby and descending

      @wip @sorting @sorting_by_updatedby @sorting_inventorygroups
  Scenario: Sort inventorygroup records by partner ascending/descending
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and ascending
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and descending