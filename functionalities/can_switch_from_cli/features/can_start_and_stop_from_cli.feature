Feature: can start and stop from cli

    Scenario: start and check from linux terminal
        GIVEN that I have a terminal
          AND Warmy is not running        
          AND I type "Warmy up" in the terminal
         WHEN I wait for the service to start
          AND I type "Warmy status" in the terminal
         THEN I Warmy tells me it's running          

    Scenario: check from linux terminal (not running)
        GIVEN that I have a terminal
          AND Warmy is not running
         WHEN I type "Warmy status" in the terminal
         THEN I Warmy tells me it's not running
        
