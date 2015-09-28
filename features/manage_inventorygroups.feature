Feature: Manage inventorygroups module

  @done @pages @open_pages_page
  Scenario: Open Manage inventory group page and view pages records
    Given I am logged in as Administrator
    And I am on Main page
    When I click on Manage Site link
    When I click on Manage Scoreboard link
    Then I want to see 'Inventory Group' page
    And I want to see table with data

  @slug
  Scenario: Create inventorygroup
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I click on create button
    And fill form with inventory group data
    And I am on Inventory Group page
    And I want to see new inventory group in list

  @done @partners @view_partner
  Scenario: View inventory group
    Given created inventorygroup
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I view inventory group
    Then I want to see 'Update Inventory Group' page
    And I want to see inventory group details

  @done @partners @update_partner @slug
  Scenario: Update inventory group
    Given created inventorygroup
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I view inventory group
    Then I want to see 'Update Inventory Group' page
    And I want to see inventory group details
    Then I want to change name content
    And I am on Inventory Group page
    Then I want to see updated inventory group in list

  @done @partners @delete_partner
  Scenario: Delete inventory group
    Given created inventorygroup
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I delete created inventory group
    Then I want to see dialog box and click No
    And I want to see inventory group in list
    When I delete created inventory group
    Then I want to see dialog box and click Yes
    Then I want to see inventory group is deleted

  Scenario: Create new item and opportunity
    Given created inventorygroup
    Given I am logged in as Administrator
    And I am on Inventory Group page
    When I view inventory group
    Then I want to see 'Update Inventory Group' page
    Then I add a new item
    Then I want to see item in list
    When I view item
    Then I want to see 'Update item' page
    Then I add a new opportunity
    Then I want to see opportunity in list
    When I click on Scoreboard link
    Then I want to see 'Scoreboard' page
#    And I want to see inventory group data
    Then I open items page
    Then I want to see 'Items' page
    Then I want to see items details

#  @wip @sorting @sorting_by_id @sorting_inventorygroups
#  Scenario: Sort inventorygroup records by id ascending/descending
#    Given I am logged in as Administrator
#    And I am on Inventory Group page
#    When I click on id sort
#    Then i want to see sorted data by id and ascending
#    When I click on id sort
#    Then i want to see sorted data by id and descending
#
#  @wip @sorting @sorting_by_name @sorting_inventorygroups
#  Scenario: Sort inventorygroup records by name ascending/descending
#    Given I am logged in as Administrator
#    And I am on Inventory Group page
#    When I click on name sort
#    Then i want to see sorted data by name and ascending
#    When I click on name sort
#    Then i want to see sorted data by name and descending
#
#  @wip @sorting @sorting_by_partner @sorting_inventorygroups
#  Scenario: Sort inventorygroup records by partner ascending/descending
#    Given I am logged in as Administrator
#    And I am on Inventory Group page
#    When I click on partner sort
#    Then i want to see sorted data by partner and ascending
#    When I click on partner sort
#    Then i want to see sorted data by partner and descending
#
#  @wip @sorting @sorting_by_createdby @sorting_inventorygroups
#  Scenario: Sort inventorygroup records by partner ascending/descending
#    Given I am logged in as Administrator
#    And I am on Inventory Group page
#    When I click on createdby sort
#    Then i want to see sorted data by createdby and ascending
#    When I click on createdby sort
#    Then i want to see sorted data by createdby and descending
#
#  @wip @sorting @sorting_by_updatedby @sorting_inventorygroups
#  Scenario: Sort inventorygroup records by partner ascending/descending
#    Given I am logged in as Administrator
#    And I am on Inventory Group page
#    When I click on updatedby sort
#    Then i want to see sorted data by updatedby and ascending
#    When I click on updatedby sort
#    Then i want to see sorted data by updatedby and descending