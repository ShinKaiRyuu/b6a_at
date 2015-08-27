from behave import *
from nose.tools import assert_equal, assert_in

use_step_matcher("re")


@when("I login with username '(?P<username>.+)' and password '(?P<password>.+)'")
def step_impl(context, username, password):
    credentials = {
        'username': username,
        'password': password,
    }
    context.page.login_with(credentials)


@given("I am logged in as administrator")
def step_impl(context):
    context.execute_steps('''
        Given I am on Main page
        When I click on Login link
        Then I want to see Login page
        When I login with username 'admin' and password '123456'
        Then I want to see Main page
        And I want to see that I am logged in
    ''')

# @given("I am logged in with username '(?P<username>.+)' and password '(?P<password>.+)'")
# def step_impl(context, username, password):
#     context.execute_steps('''
#         Given I am on Login page
#         When I login with username '{username}' and password '{password}'
#         Then I want to see My Account page
#     '''.format(username=username, password=password))

@then("I want to see that I am (?P<login_status>.+)")
def step_impl(context, login_status):
    assert login_status in ['logged in', 'logged out']
    assert_equal(login_status, context.page.get_login_status())


@then('I want to see error message "(?P<error_message>.+)"')
def step_impl(context, error_message):
    assert_in(error_message, context.page.get_error_messages())

