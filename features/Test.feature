Feature: Navigate to thinkmoney

    Scenario: Navigate to homepage
        As a Customer
        When I visit the thinkmoney website
        Then I see the thinkmoney homepage

    Scenario: Navigate to Manage your money page
        As a Customer
        When I click the login button
        Then I see the "Manage your money" page

    Scenario: Navigate to Login page
        As a Customer
        When I click the Continue To Login button
        Then I see the Login page
        
