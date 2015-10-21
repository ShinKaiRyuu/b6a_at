Feature: Manage partners module

  @done @partners @open_partners_page
  Scenario: Open partners page
    Given created partner
    Given I am logged in as Administrator
    And I am on Main page
    When I click on Manage Site link
    When I click on Manage Partners link
    Then I want to see 'Manage Partners' page
    And I want to see table with data

  @done @partners @create_partner
  Scenario: Create partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I want to see 'Manage Partners' page
    When I click on Create Partner button
    Then I want to see 'Create Partner' page
    When I create new partner
    And I click on Manage Partners link
    Then I want to see 'Manage Partners' page
    And I want to see created partner in list

  @done @partners @delete_partner
  Scenario: Delete partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    When I delete created partner
    Then I want to see dialog box and click No
    Then I want to see partner in list is not deleted
    When I delete created partner
    Then I want to see dialog box and click Yes
    Then I want to see partner is deleted

  @done @partners @view_partner
  Scenario: View partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    When I view partner
    Then I want to see 'Create Partner' page
    And I want to see partner details

  @done @partners @update_partner
  Scenario: Update partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    When I update partner
    Then I want to see 'Create Partner' page
    And I want to see partner details
    Then I want to change name starname staremail status
    When I click on Manage Partners link
    Then I want to see 'Manage Partners' page
    Then I want to see updated partner in list

#  @done @partners @sorting @sorting_by_order @sorting_partners
#  Scenario: Sort partners records by order ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Partners page
#    When I click on order sort
#    Then i want to see sorted data by order and ascending
#    When I click on order sort
#    Then i want to see sorted data by order and descending

  @done @partners @sorting @sorting_by_name @sorting_partners
  Scenario: Sort partners records by name ascending/descending
    Given created partner
    Given created partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    When I click on name sort
    Then i want to see sorted data by name and ascending
    When I click on name sort
    Then i want to see sorted data by name and descending

#  @done @partners @sorting @sorting_by_createdby @sorting_partners
#  Scenario: Sort partners records by createdby  ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Partners page
#    When I click on createdby sort
#    Then i want to see sorted data by createdby and ascending
#    When I click on createdby sort
#    Then i want to see sorted data by createdby and descending

  @done @partners @sorting @sorting_by_updatedby @sorting_partners #TODO fixed
  Scenario: Sort partners records by updatedby time ascending/descending
    Given created partner
    Given created partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and ascending
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and descending

  @done @partners @filtering @filtering_partner_by_name @filtering_partners
  Scenario: Filter partners records by name
    Given created partner
    Given created partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I write partner_name in name Filter
    Then I want to see filtered data

#  @done @partners @filtering @filtering_partner_by_createdby @filtering_partners
#  Scenario: Filter partners records by created_by
#    Given I am logged in as Administrator
#    And I am on Manage Partners page
#    Then I write admin in createdby Filter
#    Then I want to see filtered data

  @done @partners @filtering @filtering_partner_by_updatedby @filtering_partners #TODO fixed
  Scenario: Filter partners records by updated_by
    Given created partner
    Given created partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I write admin in updatedby Filter
    Then I want to see filtered data

  @done @partners @filtering @filtering_partner_by_enabled @filtering_partners
  Scenario: Filter partners records by enabled
    Given created partner
    Given created partner
    Given created disabled partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I select Enabled in status Filter
    Then I want to see filtered data

  @done @partners @filtering @filtering_partner_by_disabled @filtering_partners
  Scenario: Filter partners records by disabled
    Given created partner
    Given created partner
    Given created disabled partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I select Disabled in status Filter
    Then I want to see filtered data