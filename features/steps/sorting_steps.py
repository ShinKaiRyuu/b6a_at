from behave import *
from nose.tools import assert_equal

use_step_matcher("re")


@then("i want to see sorted data by (?P<sort_by>.+) and (?P<sort_order>.+)")
def step_impl(context, sort_by, sort_order):
    context.page.wait_for_loading()
    sorted_data = context.page.get_data()
    if sort_by == 'updatedby':
        if sort_order == 'ascending':
            actual_sorted_data = sorted(context.page.get_data(), key=lambda x: x['updated']['updated_by'])
        else:
            actual_sorted_data = sorted(context.page.get_data(), key=lambda x: x['updated']['updated_by'], reverse=True)
    else:
        if sort_order == 'ascending':
            actual_sorted_data = sorted(context.page.get_data(), key=lambda x: x['{}'.format(sort_by)])
        else:
            actual_sorted_data = sorted(context.page.get_data(), key=lambda x: x['{}'.format(sort_by)], reverse=True)
    assert_equal(sorted_data, actual_sorted_data)

