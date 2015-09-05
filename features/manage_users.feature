Feature: Manage users module

  Scenario: View users
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Users link
    Then I want to see 'Manage Users' page
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

  @wip @filter_users @filter_users_by_registration_date
  Scenario: View users. Filter records by registration date
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I write 2015-08-07 in registration_at Filter
    Then I want to see filtered users

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
  Scenario: Update user. Update account details
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
  Scenario: Update user. Update profile details
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
  Scenario: Update user. View information
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
  Scenario: Update user. Update assignments
    Given created user
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I want to see created user in list
    When I view created user information
    Then I want to see 'Update User Account Details' page
    When I click on Assignments link
    Then I want to see 'User Assignments' page
    Then I want to see empty user assignmnets
    Then I want to add root assignmnet
    Then I want to see not empty user assignmnets
    When I click on Logout link
    Then I want to login with these user
    When I open Manage Users page
    Then I must not see 'Access denied' text
    When I click on Logout link
    Given I am logged in as Administrator
    And I am on Manage Users page
    Then I want to see created user in list
    When I view created user information
    Then I want to see 'Update User Account Details' page
    When I click on Assignments link
    Then I want to see 'User Assignments' page
    Then I want to remove root assignmnet
    Then I want to see empty user assignmnets
    When I click on Logout link
    Then I want to login with these user
    When I open Manage Users page
    Then I must see 'Access denied' text

    #  Scenario: Update user. Delete user
    #
    #  Scenario: Update user. Block user

  Scenario Outline: Testing creating form
    Given I am logged in as Administrator
    And I am on Create User page
    When I fill create user form with <username>,<email>,<password>
    Then I want to get result - <result>
    Examples:
      | username           | email              | password | result                                                                        |
      | empty              | faker.email        | 123456   | I want to see error message "Username cannot be blank."                       |
      | faker.user_name    | empty              | 123456   | I want to see error message "Email cannot be blank."                          |
      | admin              | faker.email        | 123456   | I want to see error message "Username "admin" has already been taken."        |
      | faker.user_name    | root@nomail.com    | 123456   | I want to see error message "Email "root@nomail.com" has already been taken." |
      | faker.user_name    | faker.email        | 1234     | I want to see error message "Password should contain at least 6 characters."  |
      | script alert('aaa' | faker.email        | 123456   | I want to see error message "Username is invalid."                            |
      | faker.user_name    | script alert('aaa' | 123456   | I want to see error message "Email is not a valid email address."             |




  Scenario: View users. Sort records by username ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I click on username link
    Then i want to see sorted users by username and ascending
    When I click on username link
    Then i want to see sorted users by username and descending

  Scenario: View users. Sort records by username ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I click on email link
    Then i want to see sorted users by email and ascending
    When I click on email link
    Then i want to see sorted users by email and descending
    # TODO fix time sort
  Scenario: View users. Sort records by registration time ascending/descending
    Given I am logged in as Administrator
    And I am on Manage Users page
    When I click on registrationtime link
    Then i want to see sorted users by registrationtime and ascending
    When I click on registrationtime link
    Then i want to see sorted users by registrationtime and descending


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

  Scenario: View roles
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Users link
    Then I want to see 'Manage Users' page
    When I click on Roles link
    Then I want to see 'Manage Roles' page
    And I want to see all roles

  Scenario: View roles. Filter roles by name
    Given I am logged in as root
    And I am on Manage Roles page
    Then I write admin in name Filter
    Then I want to see filtered roles

  Scenario: View roles. Filter roles by description
    Given I am logged in as root
    And I am on Manage Roles page
    Then I write Editor in description Filter
    Then I want to see filtered roles

  Scenario: View roles. Filter roles by rule name
    Given I am logged in as root
    And I am on Manage Roles page
    Then I write Rule name in rulename Filter
    Then I want to see filtered roles

  Scenario: View permissions
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Users link
    Then I want to see 'Manage Users' page
    When I click on Permissions link
    Then I want to see 'Manage Permissions' page
    And I want to see all permissions

  Scenario: View permissions. Filter permissions by name
    Given I am logged in as root
    And I am on Manage Permissions page
    Then I write admin in name Filter
    Then I want to see filtered permissions

  Scenario: View permissions. Filter permissions by description
    Given I am logged in as root
    And I am on Manage Permissions page
    Then I write Delete own goods in description Filter
    Then I want to see filtered permissions

  Scenario: View permissions. Filter permissions by rule name
    Given I am logged in as root
    And I am on Manage Permissions page
    Then I write isOwnGoods in rulename Filter
    Then I want to see filtered permissions
