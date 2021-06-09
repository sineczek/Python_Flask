Feature: Test that page have correct content

  Scenario: Exchange page has a correct title
    Given I am on the exchange page
    Then There is a title shown on the page
    And The title tag has content "This is Exchange page."


  Scenario: Homepage page has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has content "This is the Homepage."



