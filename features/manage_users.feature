Feature: Manage users module

  Scenario: View users
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Users link
    Then I want to see Manage Users page
    And I want to see all users

  @wip
  Scenario: View users. Filter records
    Given I am logged in as Administrator
    And I am on Manage Users page


#  Scenario: View users. Sort records
#
#  Scenario: Create new user

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
#
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
