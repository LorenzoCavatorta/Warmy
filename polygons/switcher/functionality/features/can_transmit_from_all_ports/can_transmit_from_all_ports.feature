Scneario Outilne:  switcher
GIVEN  switcher is connected to control_unit
       switcher is connected to scheduler
WHEN   scheduler sends an "on[/off]" signal to swicher
THEN   switcher sends an "on[/off]" signal to control_unit

GIVEN  switcher is connected to control_unit
       switcher is connected to user_control
WHEN   user_control sends an "on[/off]" signal to swicher
THEN   switcher sends an "on[/off]" signal to control_unit

Core:  python service 
Adapter OUT:  usb connection
	      some kind of library to connect arduino to python
Adapter	IN:   periodically reads content of a file
	      (...messaging service in the future?)
