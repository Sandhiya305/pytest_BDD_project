Feature: Salesforce Automation create new account add contact and opportunity

  Scenario: Create new account, add contact and opportunity
    Given I am logged in to salesforce
    When I am able to create new account
    When I am create a new contact
    When I am create a new opportunity
    Then I am attaching the contact and opportunity  to new account successfully
