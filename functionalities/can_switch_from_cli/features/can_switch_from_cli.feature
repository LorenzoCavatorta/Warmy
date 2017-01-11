Feature: can switch from CLI

    Scenario: switches in standard conditions
        GIVEN that Warmy is up and running
        WHEN i ask to switch on[/off] through the CLI
        THEN the switch is turned on[/off]
