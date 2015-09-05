Feature: Manage pages module

  @done @partner @partner_open_partners_page
  Scenario: Open pages page
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Pages link
    Then I want to see 'Manage Pages' page
    And I want to see table with all pages in it