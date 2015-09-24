Feature: Manage users module

  @done @view_users
  Scenario: Open manage users page and view all users
    Given I am logged in as Administrator
    And I am on Main page
    When I click on Manage Site link
    When I click on Manage Users link
    Then I want to see 'Manage Users' page
    And I want to see table with data

  @wip @create_user
  Scenario: Create new user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I click on Create link
    And I click on Create User link
    Then I want to see 'Create User' page
    When I create new user
    Then I want to see 'Update User Account Details' page
    And I am on Manage Users page
    Then I want to see created user in list
    When I click on Logout link
    Then I want to be able to login created user

  @wip @update_users @update_user_account_details
  Scenario: Update user account details
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I update created user
    Then I want to see 'Update User Account Details' page
    Then I want to change my username  & email & password
    And I am on Manage Users page
    Then I want to see updated user in list
    When I click on Logout link
    Then I want to be able to login with new data
    Then I want to login with old data
    And  I want to see error message "Invalid login or password"

  @wip @update_users @update_user_profile_details
  Scenario: Update user profile details
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I update created user
    Then I want to see 'Update User Account Details' page
    When I click on Profile details link
    Then I want to see 'Update User Profile Details' page
    And I want to see user profile details
    Then I want to change my name public email bio location partner
    And I want to see user profile details

  @wip @update_users @update_user_view_information
  Scenario: View user information
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I want to see created user in list
    When I view created user information
    Then I want to see 'Update User Account Details' page
    When I click on Information link
    Then I want to see 'User Information' page
    And i want to see user information details

  @wip @update_users @update_user_assignments
  Scenario: Update user assignments
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I want to see created user in list
    When I view created user information
    Then I want to see 'Update User Account Details' page
    When I click on Assignments link
    Then I want to see 'User Assignments' page
    Then I want to see not empty user assignmnets
    When I click on Logout link
    Then I want to login with these user
    When I open Manage Users page
    Then I must see 'Access denied' text
    When I click on Logout link
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I want to see created user in list
    When I view created user information
    Then I want to see 'Update User Account Details' page
    When I click on Assignments link
    Then I want to see 'User Assignments' page
    Then I want to remove editor assignmnet
    Then I want to see empty user assignmnets
    When I click on Logout link
    Then I want to login with these user
    When I open Manage Users page
    Then I must see 'Access denied' text

  @wip @delete_user_2
  Scenario: Delete user
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I view created user information
    Then I want to see 'Update User Account Details' page
    When I click on delete link
    Then I want to see dialog box and click No
    Then I want to see 'Update User Account Details' page
    When I click on delete link
    Then I want to see dialog box and click Yes
    Then I want to see 'Manage Users' page
    Then I want to see user is deleted
    #  Scenario: Update user. Block user

  @wip @testing_form
  Scenario Outline: Testing creating form
    Given I am logged in as Administrator
    And I am on Create User page
    When I fill create user form with <username>,<email>,<password>
    Then I want to get result - <result>
    Examples:
      | username            | email               | password | result                                                                        |
      | empty               | faker.email         | 123456   | I want to see error message "Username cannot be blank."                       |
      | faker.user_name     | empty               | 123456   | I want to see error message "Email cannot be blank."                          |
      | admin               | faker.email         | 123456   | I want to see error message "Username "admin" has already been taken."        |
      | faker.user_name     | root@nomail.com     | 123456   | I want to see error message "Email "root@nomail.com" has already been taken." |
      | faker.user_name     | faker.email         | 1234     | I want to see error message "Password should contain at least 6 characters."  |
      | script alert('aaa') | faker.email         | 123456   | I want to see error message "Username is invalid."                            |
      | faker.user_name     | script alert('aaa') | 123456   | I want to see error message "Email is not a valid email address."             |

  @wip @delete_user
  Scenario: Delete user
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I delete created user
    Then I want to see dialog box and click No
    Then I want to see user in list is not deleted
    When I delete created user
    Then I want to see dialog box and click Yes
    Then I want to see user is deleted

  @wip @block_unblock_user
  Scenario: Block\unblock user
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I block created user
    Then I want to see dialog box and click No
    Then I want to see user in list is not blocked
    When I block created user
    Then I want to see dialog box and click Yes
    Then I want to see user is blocked
    When I click on Logout link
    Then I want to login with these user
    And  I want to see error message "Your account has been blocked"
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I unblock created user
    Then I want to see dialog box and click No
    Then I want to see user in list is blocked
    When I unblock created user
    Then I want to see dialog box and click Yes
    Then I want to see user is unblocked
    When I click on Logout link
    Then I want to login with these user
    Then I want to see 'Main' page

#  @wip @filtering @filtering_users @filtering_users_by_username
#  Scenario: Filter user records by Username
#    Given I am logged in as Administrator
#    And I am on Manage Users page
#    Then I write admin in username Filter
#    Then I want to see filtered data
#
#  @wip @filtering @filtering_users @filtering_users_by_email
#  Scenario: Filter user records by email
#    Given I am logged in as Administrator
#    And I am on Manage Users page
#    Then I write admin@nomail.com in email Filter
#    Then I want to see filtered data
#
#  @wip @filtering @filtering_users @filtering_users_by_registration_date
#  Scenario: Filter user records by registration date
#    Given I am logged in as Administrator
#    And I am on Manage Users page
#    Then I write 2015-08-07 in registrationtime Filter
#    Then I want to see filtered data
#
#  @wip @sorting @sorting_by_username @sorting_users
#  Scenario: Sort user records by username ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Users page
#    When I click on username link
#    Then i want to see sorted data by username and ascending
#    When I click on username link
#    Then i want to see sorted data by username and descending
#
#  @wip @sorting @sorting_by_email @sorting_users
#  Scenario: Sort user records by email ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Users page
#    When I click on email link
#    Then i want to see sorted data by email and ascending
#    When I click on email link
#    Then i want to see sorted data by email and descending
#
#  @wip @sorting @sorting_by_registrationtime @sorting_users
#  Scenario: Sort user records by registration time ascending/descending
#    Given I am logged in as Administrator
#    And I am on Manage Users page
#    When I click on registrationtime link
#    Then i want to see sorted data by registrationtime and ascending
#    When I click on registrationtime link
#    Then i want to see sorted data by registrationtime and descending

  @wip @view_roles @viewing
  Scenario: View roles
    Given I am logged in as Administrator
    And I am on Main page
    When I click on Manage Site link
    When I click on Manage Users link
    Then I want to see 'Manage Users' page
    When I click on Roles link
    Then I want to see 'Manage Roles' page
    And I want to see table with data

#  @wip @filtering @filtering_by_name @filtering_roles
#  Scenario: Filter roles records by name
#    Given I am logged in as root
#    And I am on Manage Roles page
#    Then I write admin in name Filter
#    Then I want to see filtered data
#
#  @wip @filtering @filtering_by_description @filtering_roles
#  Scenario: Filter roles records by description
#    Given I am logged in as root
#    And I am on Manage Roles page
#    Then I write Editor in description Filter
#    Then I want to see filtered data
#
#  @wip @filtering @filtering_by_rule_name @filtering_roles
#  Scenario: Filter roles records by rule name
#    Given I am logged in as root
#    And I am on Manage Roles page
#    Then I write Rule name in rulename Filter
#    Then I want to see filtered data

  @wip @view_permissions @viewing
  Scenario: View permissions
    Given I am logged in as root
    And I am on Manage Permissions page
    Then I want to see 'Manage Permissions' page
    And I want to see table with data

#  @wip @filtering @filtering_by_name @filtering_permissions
#  Scenario: Filter permissions records by name
#    Given I am logged in as root
#    And I am on Manage Permissions page
#    Then I write admin in name Filter
#    Then I want to see filtered data
#
#  @wip @filtering @filtering_by_description @filtering_permissions
#  Scenario: Filter permissions records by description
#    Given I am logged in as root
#    And I am on Manage Permissions page
#    Then I write Delete own goods in description Filter
#    Then I want to see filtered data
#
#  @wip @filtering @filtering_by_rule_name @filtering_permissions
#  Scenario: Filter permissions records by rule name
#    Given I am logged in as root
#    And I am on Manage Permissions page
#    Then I write isOwnGoods in rulename Filter
#    Then I want to see filtered data
