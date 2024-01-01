from behave import given, when, then


@given('I have entered {number} into the calculator')
def step_given(context, number):
    context.number = int(number)


@when('I press add')
def step_when(context):
    context.result = context.number + context.number


@then('the result should be {expected_result} on the screen')
def step_then(context, expected_result):
    assert context.result == int(expected_result), f"Expected {expected_result}, but got {context.result}"
