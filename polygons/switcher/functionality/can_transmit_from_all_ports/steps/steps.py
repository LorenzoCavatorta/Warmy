from behave import given, when, then

@given('port_out is open and port_in is open')
def check_port_in(context):
    assert False

@when('receives an on[/off] signal')
def receives_signal(context):
    assert False

@then('sends an on[/off] signal')
def sends_signal(context):
    assert False
