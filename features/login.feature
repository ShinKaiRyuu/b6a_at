Feature: Log in

  Scenario: Successful login
    Given I am on Main page
    When I click on Login link
    Then I want to see Login page
    When I login with username 'admin' and password '123456'
    Then I want to see Main page
    And I want to see that I am logged in
    When I click on Logout link
    Then I want to see that I am logged out

  Scenario: Unsuccessful login
    Given I am on Login page
    When I login with username 'abcd@ed.ba' and password '111111'
    Then I want to see error message "Invalid login or password"
