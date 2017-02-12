from behave import given, when, then
import unittest
from time import sleep
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

@when(u'I type "{text}" in the terminal')
def run_string(context, text):
    context.terminal.command = text
    result = context.terminal.run()
    #assuming the bash command returns something, will be removed
    print(result)

@when(u'I wait for the service to start')
def wait_for_worker_start(context):
    #ToDo: look ad doc to inspect that statup ops are finished
    sleep(1)

@given(u'I type "{text}" in the terminal')
def run_string(context, text):
    context.terminal.command = text
    result = context.terminal.run()
    #assuming the bash command returns something, will be removed
    print(result)

@then(u'I Warmy tells me it\'s running')
def check_Warmy_is_up(context):
    context.terminal.command = 'Warmy status'
    result = context.terminal.run()
    test_case = unittest.TestCase()
    test_case.assertEqual(result, 'up and running')

@given(u'Warmy is not running')
def stop_Warmy(context):
    context.terminal.command = 'Warmy down'
    context.terminal.run()

@then(u'I Warmy tells me it\'s not running')
def check_Warmy_is_down(context):
    context.terminal.command = 'Warmy status'
    result = context.terminal.run()
    test_case = unittest.TestCase()
    test_case.assertEqual(result, 'Warmy worker is not active')
