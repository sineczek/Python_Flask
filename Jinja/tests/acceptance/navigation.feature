Feature: Test navigation

  Scenario: Homepage can go to Exchange
    Given I am on the homepage
    When I click on the "Go to exchange" link
    Then I am on the exchange page


  Scenario: Homepage can go to Hotel form
    Given I am on the homepage
    When I click on the "Go to Hotel Form" link
    Then I am on the hotel form page