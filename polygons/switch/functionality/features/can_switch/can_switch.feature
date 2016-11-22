Scenario Outline: switch_can_switch
GIVEN  switch is connected to a power cable (one cable in, one cable out)
       switch has port_in open
WHEN   switch receives a continuous "on" signal
THEN   switch lets current flow between the two power cables

GIVEN  switch is connected to a power cable (one cable in, one cable out)
       switch has port_IN open
WHEN   no signal is received
THEN   no current flows between the two power cables

GIVEN  switch is connected to a power cable (one cable in, one cable out)
       switch has port_IN closed
WHEN   always
THEN   no current flows betewwn the two power cables

