Feature: Manage partners module

  @done @partner @partner_open_partners_page
  Scenario: Open partners page
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Partners link
    Then I want to see 'Manage Partners' page
    And I want to see all partners

  @done @partner @create_partner
  Scenario: Create partner
    Given I am logged in as Administrator
    When I click on Manage Site link
    When I click on Manage Partners link
    Then I want to see 'Manage Partners' page
    When I click on Create Partner button
    Then I want to see 'Create Partner' page
    When I create new partner
    Then I want to see 'Manage Partners' page
    And I want to see created partner in list

  @done @partner @delete_partner
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

  @done @partner @view_partner
  Scenario: View partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    When I view partner
    Then I want to see 'Create Partner' page
    And I want to see partner details

  @done @partner @update_partner
  Scenario: Update partner
    Given created partner
    Given I am logged in as Administrator
    And I am on Manage Partners page
    When I update partner
    Then I want to see 'Create Partner' page
    And I want to see partner details
    Then I want to change name starname staremail status
    And I am on Manage Partners page
    Then I want to see updated partner in list

  @done @partner @filter_partner_by_order
  Scenario: Filter partner by order
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I write 1 in order Filter
    Then I want to see filtered partners

  @done @partner @filter_partner_by_name
  Scenario: Filter products by name
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I write New in name Filter
    Then I want to see filtered partners

  @done @partner @filter_partner_by_created_by
  Scenario: Filter products by created_by
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I write admin in created_by Filter
    Then I want to see filtered partners

  @done @partner @filter_partner_by_updated_by
  Scenario: Filter products by updated_by
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I write root in updated_by Filter
    Then I want to see filtered partners

  @done @partner @filter_partner_by_status_enabled
  Scenario: Filter products by enabled
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I select Enabled in status Filter
    Then I want to see filtered partners

  @done @partner @filter_partner_by_status_disabled
  Scenario: Filter products by disabled
    Given I am logged in as Administrator
    And I am on Manage Partners page
    Then I select Disabled in status Filter
    Then I want to see filtered partners