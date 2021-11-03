from behave import given, when, then


@given("Open SignUp Page")
def step_impl(context):
    context.app.sign_up.open_signup()


@when("Select Mr Title")
def step_impl(context):
    context.app.sign_up.select_mr_title()


@when("Enter First Name")
def step_impl(context):
    context.app.sign_up.enter_first_name()


@when("Enter Last Name")
def step_impl(context):
    context.app.sign_up.enter_last_name()


@when("Accept Terms and Conditions")
def step_impl(context):
    context.app.sign_up.check_accept_terms()


@when("Submit the Form")
def step_impl(context):
    context.app.sign_up.submit_form()


@then("DOB required Message Appears")
def step_impl(context):
    context.app.sign_up.verify_dob_error_msg()