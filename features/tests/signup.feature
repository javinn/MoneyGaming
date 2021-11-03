
Feature: Signup Scenarios

  Scenario: New User Verification
    Given Open SignUp Page
    When Select Mr Title
    And Enter First Name
    And Enter Last Name
    And Accept Terms and Conditions
    And Submit the Form
    Then DOB required Message Appears