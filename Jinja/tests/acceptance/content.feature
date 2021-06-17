Feature: Test that page have correct content

  Scenario: Exchange page has a correct title
    Given I am on the exchange page
    Then There is a title shown on the page
    And The title tag has content "This is Exchange page."


  Scenario: Homepage page has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has content "This is the Homepage."


  Scenario: Exchange page currency dropdown menu
    Given I am on the exchange page
    When I can click on field with id "currency"
    Then "USD" currency value is selected



  Scenario: Exchange page amount field
    Given I am on the exchange page
    When I can click on field with id "amount"
    Then "amount" field has value "100"


  Scenario: I can exchange currency
    Given I am on the exchange page
    When I can click on field with id "currency"
    And I can choose currency "Euro"
    And I can insert "200" in the "amount" field
    #And I click submit button with id "submit" text field
    #Then Data is send
    #And I am on exchange results page
    #And The title tag has content "This is Exchange Result page."