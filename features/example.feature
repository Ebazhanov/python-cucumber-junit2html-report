Feature: Simple Addition

  Scenario: Add two numbers
    Given I have entered 3 into the calculator
    And I have entered 5 into the calculator
    When I press add
    Then the result should be 8 on the screen