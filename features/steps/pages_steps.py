from behave import *
from nose.tools import assert_true, assert_equal

use_step_matcher("re")


@step("I want to see table with all pages")
def step_impl(context):
    pages = context.page.get_pages()
    assert_true(len(pages) >= 1)


@then("i want to see sorted pages by (?P<sort_by>.+) and (?P<sort_order>.+)")
def step_impl(context, sort_by, sort_order):
    context.page.wait_for_loading()
    sorted_users = context.page.get_pages()
    if sort_order == 'ascending':
            actual_sorted_users = sorted(context.page.get_pages(), key=lambda x: x['{}'.format(sort_by)])
    else:
        actual_sorted_users = sorted(context.page.get_pages(), key=lambda x: x['{}'.format(sort_by)], reverse=True)
    assert_equal(sorted_users, actual_sorted_users)
