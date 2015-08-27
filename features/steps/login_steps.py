from behave import *
from nose.tools import assert_equal, assert_in

from helpers.driver_helpers import update_driver_cookies
from helpers.app_helpers import ADMIN_CREDENTIALS

use_step_matcher("re")



@when("I login with username '(?P<username>.+)' and password '(?P<password>.+)'")
def step_impl(context, username, password):
    credentials = {
        'username': username,
        'password': password,
    }
    context.page.login_with(credentials)


@given("I am logged in as Administrator")
def step_impl(context):
    context.execute_steps('''
        Given I am on Main page
    ''')
    update_driver_cookies(context.driver, ADMIN_CREDENTIALS)


@then("I want to see that I am (?P<login_status>.+)")
def step_impl(context, login_status):
    assert login_status in ['logged in', 'logged out']
    assert_equal(login_status, context.page.get_login_status())


@then('I want to see error message "(?P<error_message>.+)"')
def step_impl(context, error_message):
    assert_in(error_message, context.page.get_error_messages())
