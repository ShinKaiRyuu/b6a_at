from behave import *
from nose.tools import assert_equal, assert_in

from helpers.driver_helpers import update_driver_cookies
from helpers.app_helpers import ADMIN_CREDENTIALS, MANAGER_CREDENTIALS

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


@given("I am logged in as Manager")
def step_impl(context):
    context.execute_steps('''
        Given I am on Main page
    ''')
    context.driver.delete_all_cookies()
    context.driver.refresh()
    update_driver_cookies(context.driver, MANAGER_CREDENTIALS)
    context.driver.refresh()


@then("I want to see that I am (?P<login_status>.+)")
def step_impl(context, login_status):
    assert login_status in ['logged in', 'logged out']
    assert_equal(login_status, context.page.get_login_status())


@then('I want to see error message "(?P<error_message>.+)"')
def step_impl(context, error_message):
    assert_in(error_message, context.page.get_error_messages())


@then("I want to login with these user")
def step_impl(context):
    context.execute_steps('''
            Given I am on Main page
            When I click on Login link
            Then I want to see 'Login' page
            When I login with username '{}' and password '{}'
            '''.format(context.user_data['username'], context.user_data['password']))


@then("I want to login with old data")
def step_impl(context):
    context.execute_steps('''
            Given I am on Main page
            When I click on Login link
            Then I want to see 'Login' page
            When I login with username '{}' and password '{}'
            '''.format(context.old_user_data['username'], context.old_user_data['password']))
