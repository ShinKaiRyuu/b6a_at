Feature: Manage users module

  Scenario: View users
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Users link
    Then I want to see Manage Users page
    And I want to see all users

  @wip @filter_users
  Scenario: View users. Filter records by Username
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I write admin in username Filter
    Then I want to see filtered users

  @wip @filter_users
  Scenario: View users. Filter records by email
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I write admin@nomail.com in email Filter
    Then I want to see filtered users

  @wip @filter_users
  Scenario: View users. Filter records by registration ip
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I write ::1 in registration_ip Filter
    Then I want to see filtered users

  @wip @filter_users
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

  @now
  Scenario: Update user. Update account details
    Given created user
    And fail

#  Scenario: Update user. Update profile details
#
#  Scenario: Update user. View information
#
#  Scenario: Update user. Update assignments
#
#  Scenario: Update user. Delete user
#
#  Scenario: Update user. Block user
  @wip @delete_users
  Scenario: Delete user
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I delete created user
    Then I want to see dialog box and click No
    Then I want to see user in list
    When I delete created user
    Then I want to see dialog box and click Yes
    Then I want to see created user is deleted

#  Scenario: Block user
#
#  Scenario: View roles
#
#  Scenario: View roles. Filter roles
#
#  Scenario: Create new role
#
#  Scenario: Update role
#
#  Scenario: Delete role










#  Scenario: View permissions

#  Scenario: View permissions. Filter permissions

#  Scenario: Create new permission

#  Scenario: Update permission

#  Scenario: Delete permission
