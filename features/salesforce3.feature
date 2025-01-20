Feature: Salesforce Automation create lead using existing account

  Scenario: Log in and create a lead
    Given I am logged in to salesforce
    When I am create a lead
    Then I am converting the lead to account using existing account successfully

