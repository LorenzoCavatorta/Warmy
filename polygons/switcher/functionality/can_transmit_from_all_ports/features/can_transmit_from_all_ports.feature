Feature: can trasmit from all ports

Scneario Outilne: sends when receives
    GIVEN port_out is open and port_in is open
    WHEN receives an on[/off] signal 
    THEN sends an on[/off] signal 

Scenario Outline: errors when can not send
    GIVEN port_out is closed and port_in is open
    WHEN receives an on[/off] signal
    THEN returns an error message to port_in
