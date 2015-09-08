from behave import *
from nose.tools import assert_equal, assert_true, assert_in

from helpers.data_helpers import create_user_data, modify_value

use_step_matcher("re")


@when("I create new user")
def step_impl(context):
    user = create_user_data()
    context.page.create_new_user(**user)
    context.user_data = user


@step("I want to see all users")
def step_impl(context):
    users = context.page.get_data()
    assert_true(len(users) >= 1)


@when("I delete created user")
def step_impl(context):
    context.page.delete_user(context.user_data['username'], context.user_id)


@then("I want to see user in list is (?P<status>.+)")
def step_impl(context, status):
    user = [user for user in context.page.get_data() if user['username'] == context.user_data['username']]
    assert_equal(len(user), 1)
    if status == 'not deleted':
        assert_equal(user[0]['email'], context.user_data['email'])
    if status == 'not blocked':
        assert_true(context.page.is_element_present('block_user_link'))
    if status == 'blocked':
        assert_true(context.page.is_element_present('unblock_user_link'))


@then("I want to see user is (?P<status>.+)")
def step_impl(context, status):
    context.page.filter_data('username', context.user_data['username'])
    user = [user for user in context.page.get_data() if user['username'] == context.user_data['username']]
    context.page.replace_bad_elements('.close')
    success_message = context.page.success_message.text
    if status == 'deleted':
        assert_equal(len(user), 0)
        assert_in('User has been deleted', success_message)
    if status == 'blocked':
        assert_equal(len(user), 1)
        assert_in('User has been blocked', success_message)
        assert_true(context.page.is_element_present('unblock_user_link'))
    if status == 'unblocked':
        assert_equal(len(user), 1)
        assert_in('User has been unblocked', success_message)
        assert_true(context.page.is_element_present('block_user_link'))


@then("I write (?P<filter_text>.+) in (?P<filter_name>.+) Filter")
@then("I select (?P<filter_text>.+) in (?P<filter_name>.+) Filter")
def step_impl(context, filter_text, filter_name):
    context.filter_name = filter_name
    context.filter_text = filter_text
    context.page.filter_data(context.filter_name, context.filter_text)


@then("I want to see updated user in list")
@then("I want to see created user in list")
def step_impl(context):
    context.page.filter_data('username', context.user_data['username'])
    user = [user for user in context.page.get_data() if user['username'] == context.user_data['username']]
    assert_equal(len(user), 1)
    user = user[0]
    assert_equal(user['email'], context.user_data['email'])
    context.user_data['registrationtime'] = user['registrationtime']
    context.user_data['confirmation'] = user['confirmation']
    if context.page.is_element_present('block_user_link'):
        context.user_data['blockstatus'] = "Not blocked"
    elif context.page.is_element_present('unblock_user_link'):
        context.user_data['blockstatus'] = "Blocked"


@then("I want to be able to login with new data")
@then("I want to be able to login created user")
def step_impl(context):
    context.execute_steps('''
        Given I am on Main page
        When I click on Login link
        Then I want to see 'Login' page
        When I login with username '{}' and password '{}'
        Then I want to see 'Main' page
        And I want to see that I am logged in
        When I click on Logout link
        Then I want to see that I am logged out
    '''.format(context.user_data['username'], context.user_data['password']))


@when("I block created user")
@when("I unblock created user")
def step_impl(context):
    context.page.block_user(context.user_data['username'], context.user_id)


@when("I view created user information")
@when("I update created user")
def step_impl(context):
    context.page.update_user(context.user_data['username'], context.user_id)


@then("I want to change my username  & email & password")
def step_impl(context):
    user = create_user_data()
    context.page.update_user_account_details(**user)
    context.old_user_data = context.user_data
    context.user_data = user


@step("I want to see user profile details")
def step_impl(context):
    user_data = context.page.view_user_profile_details()
    assert_equal(context.user_data['name'], user_data['name'])
    assert_equal(context.user_data['public_email'], user_data['public_email'])
    assert_equal(context.user_data['location'], user_data['location'])
    assert_equal(context.user_data['bio'], user_data['bio'])
    assert_equal(context.user_data['partner_id'], user_data['partner_id'])


@then("I want to change my name public email bio location partner")
def step_impl(context):
    user = create_user_data()
    context.page.update_user_profile_details(**user)
    context.user_data['name'] = user['name']
    context.user_data['public_email'] = user['public_email']
    context.user_data['location'] = user['location']
    context.user_data['bio'] = user['bio']
    context.user_data['partner_id'] = user['partner_id']


@step("i want to see user information details")
def step_impl(context):
    user_data = context.page.view_user_information()
    assert_equal(context.user_data['registrationtime'], user_data['registrationtime'])
    assert_in(context.user_data['confirmation'], user_data['confirmation'])
    assert_equal(context.user_data['blockstatus'], user_data['blockstatus'])


@then("I want to see empty user assignmnets")
def step_impl(context):
    assignments = context.page.view_assignments()
    assert_equal(len(assignments), 0)


@then("I want to see not empty user assignmnets")
def step_impl(context):
    assignments = context.page.view_assignments()
    assert_true(len(assignments) > 0)


@then("I want to add (?P<assignment_value>.+) assignmnet")
def step_impl(context, assignment_value):
    context.page.add_assignment(assignment_value)
    assignments = context.page.view_assignments()
    assert_equal(len(assignments), 1)


@then("I want to remove (?P<assignment_value>.+) assignmnet")
def step_impl(context, assignment_value):
    context.page.remove_assignment(assignment_value)
    assignments = context.page.view_assignments()
    assert_equal(len(assignments), 0)


@then("I must not see '(?P<text>.+)' text")
def step_impl(context, text):
    assert_true(text not in context.driver.page_source)


@then("I must see '(?P<text>.+)' text")
def step_impl(context, text):
    assert_true(text in context.driver.page_source)


@step("I want to see all roles")
def step_impl(context):
    roles = context.page.get_roles()
    assert_true(len(roles) >= 1)


@step("I want to see all permissions")
def step_impl(context):
    permissions = context.page.get_permissions()
    assert_true(len(permissions) >= 1)


@when("I fill create user form with (?P<username>.+),(?P<email>.+),(?P<password>.+)")
def step_impl(context, username, email, password):
    user = {}
    user.update(username=modify_value(username))
    user.update(email=modify_value(email))
    user.update(password=modify_value(password))
    context.page.create_new_user(**user)
