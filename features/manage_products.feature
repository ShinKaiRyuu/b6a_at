Feature: Manage products module

  @done @products @view_products
  Scenario: Open Manage products page and view products
    Given I am logged in as Administrator
    And I am on Main page
    When I click on Manage Site link
    When I click on Manage Products link
    Then I want to see 'Manage Products' page
    And I want to see table with data

  @done @products @creating_new @create_new_product @slug
  Scenario: Create new product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on Create new product button
    Then I want to see 'Create Product' page
    When I create new product
    When I click on Manage Products link
    Then I want to see 'Manage Products' page
    Then I want to see created product in list

  @done @products @deleting @delete_product #TODO fix
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

  @done @products @viewing @view_new_product
  Scenario: View product
    Given created product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I view product
    Then I want to see 'Create Product' page
    And I want to see product details

  @done @products @viewing @view_new_product @slug
  Scenario: Open product page
    Given created product
    And I am on Partnership Portal page
    When I open product
    Then I want to see 'Product' page
    And I want to see product elements

  @done @products @updating @update_product #TODO fix
  Scenario: Update product
    Given created product
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I update product
    Then I want to see 'Create Product' page
    And I want to see product details
    Then I want to change title description price enabled
    When I click on Manage Products link
    Then I want to see 'Manage Products' page
    Then I want to see updated product in list

  @done @products @filtering @filtering_by_title
  Scenario: Filter products records by title
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I write New in title Filter
    Then I want to see filtered data

#  @done @products @filtering @filtering_by_created_by @filtering_products
#  Scenario: Filter products records by created by
#    Given I am logged in as Administrator
#    And I am on Manage Products page
#    Then I write admin in createdby Filter
#    Then I want to see filtered data

  @done @products @filtering @filtering_by_updated_by @filtering_products #TODO fix
  Scenario: Filter products records by updated by
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I write admin in updatedby Filter
    Then I want to see filtered data

  @done @products @filtering @filtering_by_enabled @filtering_products
  Scenario: Filter products records by enabled
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I select Enabled in enabled Filter
    Then I want to see filtered data

  @done @products @filtering @filtering_by_disabled @filtering_products
  Scenario: Filter products records by disabled
    Given I am logged in as Administrator
    And I am on Manage Products page
    Then I select Disabled in enabled Filter
    Then I want to see filtered data

#  @done @products @sorting @sorting_by_order @sorting_products
#  Scenario: Sort products records by order ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Products page
#    When I click on order sort
#    Then i want to see sorted data by order and descending
#    When I click on order sort
#    Then i want to see sorted data by order and ascending

  @done @products @sorting @sorting_by_order @sorting_products #TODO fix
  Scenario: Sort products records by title ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on title sort
    Then i want to see sorted data by title and ascending
    When I click on title sort
    Then i want to see sorted data by title and descending

  @done @products @sorting @sorting_by_order @sorting_products
  Scenario: Sort products records by price ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on price sort
    Then i want to see sorted data by price and ascending
    When I click on price sort
    Then i want to see sorted data by price and descending

#  @done @products @sorting @sorting_by_order @sorting_products
#  Scenario: Sort products records by createdby  ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Products page
#    When I click on createdby sort
#    Then i want to see sorted data by createdby and ascending
#    When I click on createdby sort
#    Then i want to see sorted data by createdby and descending

  @done @products @sorting @sorting_by_order @sorting_products #TODO fix
  Scenario: Sort products records by updatedby time ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Products page
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and ascending
    When I click on updatedby sort
    Then i want to see sorted data by updatedby and descending