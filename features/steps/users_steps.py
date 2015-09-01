import time

from behave import *
from nose.tools import assert_equal, assert_true, assert_in
from faker import Faker

from helpers.data_helpers import make_ordered_dict

use_step_matcher("re")

_faker = None


def get_faker():
    global _faker
    if not _faker:
        _faker = Faker()
    return _faker


@when(
    "I create new user")
def step_impl(context):
    faker = get_faker()
    username = faker.user_name()
    email = faker.email()
    password = faker.password()
    keys = ['username', 'email', 'password']
    kwargs = make_ordered_dict(keys, locals())
    context.page.create_new_user(**kwargs)
    context.user = kwargs


@step("I want to see all users")
def step_impl(context):
    users = context.page.get_users()
    assert_true(len(users) >= 1)


@when("I delete created user")
def step_impl(context):
    context.page.delete_user(context)


@then("I want to see user in list")
def step_impl(context):
    result = 0
    for user in context.page.get_users():
        if user['username'] == context.user['username']:
            assert_equal(user['email'], context.user['email'])
            assert_equal(user['registration_ip'], context.user['registration_ip'])
            assert_equal(user['registration_time'], context.user['registration_time'])
            assert_equal(user['confirmation'], context.user['confirmation'])
            result = 1
    assert_equal(result, 1)


@then("I want to see created user is deleted")
def step_impl(context):
    result = 0
    for user in context.page.get_users():
        if user['username'] == context.user['username']:
            assert_equal(user['email'], context.user['email'])
            assert_equal(user['registration_ip'], context.user['registration_ip'])
            assert_equal(user['registration_time'], context.user['registration_time'])
            assert_equal(user['confirmation'], context.user['confirmation'])
            result = 1
    assert_equal(result, 0)
    context.page.replace_bad_elements('.close')
    success_message = context.page.success_message.text
    assert_in('User has been deleted', success_message)


@then("I write (?P<filter_text>.+) in (?P<filter_name>.+) Filter")
def step_impl(context, filter_text, filter_name):
    context.filter_name = filter_name + '_filter'
    context.filter_text = filter_text
    context.page.filter_user(context.filter_name, context.filter_text)


@then("I want to see filtered users")
def step_impl(context):
    filter_name = context.filter_name.replace('_filter', '').replace('_at', '_time')
    result = 0
    for user in context.page.get_users():
        if filter_name == 'registration_time':
            registration_time = time.strftime('%Y-%m-%dT%H:%M:%SZ',
                                              time.strptime(user[filter_name], '%B %d, %Y %I:%M'))
            if context.filter_text not in registration_time:
                result = 1
        elif context.filter_text not in user[filter_name]:
            result = 1
    assert_equal(result, 0)


@then("I want to see created user in list")
def step_impl(context):
    result = 0
    for user in context.page.get_users():
        if user['username'] == context.user['username']:
            assert_equal(user['email'], context.user['email'])
            result = 1
    assert_equal(result, 1)


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
    '''.format(context.user['username'], context.user['password']))
