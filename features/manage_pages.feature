Feature: Manage pages module

  @done @pages @open_pages_page
  Scenario: Open Manage pages page and view pages records
    Given I am logged in as Administrator
    And I am on Main page
    When I click on Manage Site link
    When I click on Manage Pages link
    Then I want to see 'Manage Pages' page
    And I want to see table with data

  @wip @pages @creating @slug
  Scenario: Create new parent page
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I click on Create Page button
    Then I want to see 'Create Page' page
    When I create new page
    Then I want to see 'Updated successfully.' message
    And I am on Manage Pages page
    And I want to see created page in list

  @wip @pages @drag_n_drop
  Scenario: Drag n drop created parent page from bottom to top
    Given created parent page
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I dragndrop created page to top position
    Then I want to see created page in top position
    And I am on Manage Pages page
    When I click on Public pages link
    Then I want to see created page in top of list
    When I click on logout link
    Then I want to see 'Main' page
    And I want to see created page in header

  @wip @pages @opening @open_parent_and_additional_page
  Scenario: Open parent and additional pages
    Given created parent page with additional page
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I open parent
    Then I want to see 'Parent Page' page
    And  I want to see additional link
    When I open additional
    Then I want to see 'Additional Page' page

  @wip @pages @opening
  Scenario: open draft pages
    Given created draft parent page
    Given I am logged in as Administrator
    And I am on Manage Pages page
    Then I want to see no link to draft parent page
    When I open page from parent context_data
    Then I must see 'The requested page does not exist.' text
    Given created parent page with draft additional page
    And I am on Manage Pages page
    Then I want to see no link to draft additional page
    When I open page from additional context_data
    Then I must see 'The requested page does not exist.' text

  @wip @pages @updating @slug
  Scenario: update parent page
    Given created parent page
    Given I am logged in as Administrator
    And I am on Manage Pages page
    When I update page
    Then I want to see 'Create Page' page
    And I want to see page details
    Then I want to change page details
    And I am on Manage Pages page
    And I want to see created page in list

#  @done @pages @filtering @filtering_by_name @filtering_pages
#  Scenario: Filter pages records by name
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    Then I write partnership in name Filter
#    Then I want to see filtered data
#
#  @done @pages @filtering @filtering_by_createdby @filtering_pages
#  Scenario: Filter pages records by created_by
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    Then I write admin in createdby Filter
#    Then I want to see filtered data
#
#  @done @pages @filtering @filtering_by_updatedby @filtering_pages
#  Scenario: Filter pages records by updated_by
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    Then I write admin in updatedby Filter
#    Then I want to see filtered data
#
#  @done @pages @filtering @filtering_by_enabled @filtering_pages
#  Scenario: Filter pages records by enabled
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    Then I select Published in status Filter
#    Then I want to see filtered data
#
#  @done @pages @filtering @filtering_by_disabled @filtering_pages
#  Scenario: Filter pages records by disabled
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    Then I select Draft in status Filter
#    Then I want to see filtered data
#
#  @done @pages @sorting @sorting_by_order @sorting_pages
#  Scenario: Sort pages records by order ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    When I click on order sort
#    Then i want to see sorted data by order and ascending
#    When I click on order sort
#    Then i want to see sorted data by order and descending
#
#  @done @pages  @sorting  @sorting_by_name @sorting_pages
#  Scenario: Sort pages records by name ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    When I click on name sort
#    Then i want to see sorted data by name and ascending
#    When I click on name sort
#    Then i want to see sorted data by name and descending
#
#  @done @pages  @sorting @sorting_by_createdby @sorting_pages
#  Scenario: Sort pages records by createdby ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    When I click on createdby sort
#    Then i want to see sorted data by createdby and ascending
#    When I click on createdby sort
#    Then i want to see sorted data by createdby and descending
#
#  @done @pages  @sorting @sorting_by_updatedby @sorting_pages
#  Scenario: Sort pages records by updatedby ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Pages page
#    When I click on updatedby sort
#    Then i want to see sorted data by updatedby and ascending
#    When I click on updatedby sort
#    Then i want to see sorted data by updatedby and descending
