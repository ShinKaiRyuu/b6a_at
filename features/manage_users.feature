Feature: Manage users module

  Scenario: View users
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Users link
    Then I want to see Manage Users page
    And I want to see all users

  @wip @filter_users @filter_users_by_username
  Scenario: View users. Filter records by Username
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I write admin in username Filter
    Then I want to see filtered users

  @wip @filter_users @filter_users_by_email
  Scenario: View users. Filter records by email
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I write admin@nomail.com in email Filter
    Then I want to see filtered users

  @wip @filter_users @filter_users_by_ip
  Scenario: View users. Filter records by registration ip
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I write ::1 in registration_ip Filter
    Then I want to see filtered users

  @wip @filter_users @filter_users_by_registration_date
  Scenario: View users. Filter records by registration date
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I write 2015-08-07 in registration_at Filter
    Then I want to see filtered users


#  Scenario: View users. Sort records
#

  @wip @create_user
  Scenario: Create new user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I click on Create link
    And I click on Create User link
    Then I want to see Create User page
    When I create new user
    Then I want to see Update User Account Details page
    And I am on Manage Users page
    Then I want to see created user in list
    When I click on Logout link
    Then I want to be able to login created user

  @wip @update_users @update_user_account_details
  Scenario: Update user. Update account details
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I update created user
    Then I want to see Update User Account Details page
    Then I want to change my username  & email & password
    And I am on Manage Users page
    Then I want to see updated user in list
    When I click on Logout link
    Then I want to be able to login with new data
    Then I want to login with old data
    And  I want to see error message "Invalid login or password"

  @wip @update_users @update_user_profile_details
  Scenario: Update user. Update profile details
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I update created user
    Then I want to see Update User Account Details page
    When I click on Profile details link
    Then I want to see Update User Profile Details page
    And I want to see user profile details
    Then I want to change my name public email bio location partner
    And I want to see user profile details

  @wip @update_users @update_user_view_information
  Scenario: Update user. View information
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I want to see created user in list
    When I view created user information
    Then I want to see Update User Account Details page
    When I click on Information link
    Then I want to see User Information page
    And i want to see user information details

  @wip @update_users @update_user_assignments
  Scenario: Update user. Update assignments
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I want to see created user in list
    When I view created user information
    Then I want to see Update User Account Details page
    When I click on Assignments link
    Then I want to see User Assignments page
    Then I want to see empty user assignmnets
    Then I want to add root assignmnet
    When I open Create Role page
    Then I must not see '            Access denied        ' text
    When I open Create Permission page
    Then I must not see '            Access denied        ' text
    Then I want to remove root assignmnet
    When I open Create Role page
    Then I must see '            Access denied        ' text
    When I open Create Permission page
    Then I must see '            Access denied        ' text


#  Scenario: Update user. Delete user
#
#  Scenario: Update user. Block user

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
    Then I want to see Main page

  Scenario: View roles
    Given I am logged in as Administrator
    When I open Create Role page
    Then I must see '            Access denied        ' text
    When I click on Logout link
    Given I am logged in as root

  Scenario: View roles. Filter roles
    Given I am logged in as root
    And I am on Manage Roles page
    Then I write admin in username Filter
    Then I want to see filtered users
#
#  Scenario: Create new role
#
#  Scenario: Update role
#
#  Scenario: Delete role

  Scenario: View permissions
    Given I am logged in as Administrator
    When I open Create Permission page
    Then I must see '            Access denied        ' text
    When I click on Logout link
    Given I am logged in as root

  Scenario: View permissions. Filter permissions
    Given I am logged in as root
    And I am on Manage Roles page
    Then I write admin in username Filter
    Then I want to see filtered users

#  Scenario: Create new permission

#  Scenario: Update permission

#  Scenario: Delete permission
