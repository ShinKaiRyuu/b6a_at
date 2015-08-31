from behave import *
from nose.tools import assert_equal, assert_true, assert_in

use_step_matcher("re")


@step("I want to see all users")
def step_impl(context):
    users = context.page.get_users()
    assert_true(len(users) >= 1)


@when("I delete created user")
def step_impl(context):
    context.user = context.page.delete_user(context)


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
