Feature:  control_unit can send on-off signals

Scenario Outline:
GIVEN  control_unit is connected to switch
       control_unit is connected to power_supply
       control_unit is connected to switcher
WHEN   control_unit receives an "on" (impulsive) signal
THEN   control_unit start sending a continuous "on" signal out

Scenario Outline:
GIVEN  control_unit is connected to switch
       control_unit is connected to power_supply
       control_unit is connected to switcher
       control_unit is sending a continuous "on" signal to switch
WHEN   switcher sends an "off" signal 
THEN   control_unit stops senting a continuous "on" signal to switch

Scenario Outline:
GIVEN  control_unit is connected to switch
       control_unit is connected to power_supply
       control_unit is connected to switcher
       control_unit is not sending a continuous "on" signal to switch
WHEN   switcher sends an "off" signal 
THEN   control_unit doesn't change its status

Scenario Outline:
GIVEN  control_unit is connected to switch
       control_unit is connected to power_supply
       control_unit is connected to switcher
       control_unit is sending a continuous "on" signal to switch
WHEN   switcher sends an "on" signal 
THEN   control_unit doesn't change its status
