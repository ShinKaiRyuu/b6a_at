import time

from behave import *
from nose.tools import assert_equal, assert_true, assert_in

from helpers.data_helpers import create_user_data

use_step_matcher("re")


@when(
    "I create new user")
def step_impl(context):
    user = create_user_data()
    context.page.create_new_user(**user)
    context.user_data = user


@step("I want to see all users")
def step_impl(context):
    users = context.page.get_users()
    assert_true(len(users) >= 1)


@when("I delete created user")
def step_impl(context):
    context.page.delete_user(context)


@then("I want to see user in list is (?P<status>.+)")
def step_impl(context, status):
    user = [user for user in context.page.get_users() if user['username'] == context.user_data['username']]
    assert_equal(len(user), 1)
    if status == 'not deleted':
        assert_equal(user['email'], context.user_data['email'])
    if status == 'not blocked':
        assert_true(context.page.is_element_present('block_user_link'))
    if status == 'blocked':
        assert_true(context.page.is_element_present('unblock_user_link'))


@then("I want to see user is (?P<status>.+)")
def step_impl(context, status):
    context.page.filter_user('username_filter', context.user_data['username'])
    user = [user for user in context.page.get_users() if user['username'] == context.user_data['username']]
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
def step_impl(context, filter_text, filter_name):
    context.filter_name = filter_name + '_filter'
    context.filter_text = filter_text
    context.page.filter_user(context.filter_name, context.filter_text)


@then("I want to see filtered users")
def step_impl(context):
    filter_name = context.filter_name.replace('_filter', '').replace('_at', '_time')
    users = context.page.get_users()
    for user in users:
        if filter_name == 'registration_time':
            registration_time = time.strftime('%Y-%m-%dT%H:%M:%SZ',
                                              time.strptime(user[filter_name], '%B %d, %Y %I:%M'))
            assert_in(context.filter_text, registration_time)
        elif filter_name != "registration_time":
            assert_in(context.filter_text, user[filter_name])


@then("I want to see created user in list")
def step_impl(context):
    user = [user for user in context.page.get_users() if user['username'] == context.user_data['username']]
    assert_equal(len(user), 1)
    user = user[0]
    assert_equal(user['email'], context.user_data['email'])


@then("I want to be able to login created user")
def step_impl(context):
    context.execute_steps('''
        Given I am on Main page
        When I click on Login link
        Then I want to see Login page
        When I login with username '{}' and password '{}'
        Then I want to see Main page
        And I want to see that I am logged in
        When I click on Logout link
        Then I want to see that I am logged out
    '''.format(context.user_data['username'], context.user_data['password']))


@when("I block created user")
def step_impl(context):
    context.page.block_user(context)


@when("I unblock created user")
def step_impl(context):
    context.page.unblock_user(context)


@then("I want to login with these user")
def step_impl(context):
    context.execute_steps('''
            Given I am on Main page
            When I click on Login link
            Then I want to see Login page
            When I login with username '{}' and password '{}'
            '''.format(context.user_data['username'], context.user_data['password']))
