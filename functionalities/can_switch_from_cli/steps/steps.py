from behave import given, when, then
import unittest
from bash_command import BashCommand

@given('that Warmy is up and running')
def start_services(context):
    pass

@when('i ask to switch on[/off] through the CLI')
def send_message(context):
    pass


@then('the switch is turned on[/off]')
def check_switch_status(context):
    pass



###################scenario 2

@given(u'that I have a terminal')
def open_bash(context):
    context.terminal = BashCommand(r='output')

@when(u'I type \'Warmy up\' in the terminal')
def run_string(context):
    context.terminal.command = 'Warmy up'
    result = context.terminal.run()
    #assuming the bash command returns something, will be removed
    print(result)

@then(u'Warmy service starts')
def check_Warmy_status(context):
    context.terminal.command = 'Warmy status'
    result = context.terminal.run()
    test_case = unittest.TestCase()
    test_case.assertEqual(result, 'up and running')
