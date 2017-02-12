Feature: can start Warmy from cli

    Scenario: start from ubuntu terminal
        GIVEN that I have a terminal
        WHEN I type 'Warmy up' in the terminal
        THEN Warmy service starts
        
