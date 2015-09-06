import time

from behave import *
from nose.tools import assert_equal, assert_in

use_step_matcher("re")


@then("I want to see filtered data")
def step_impl(context):
    filter_name = context.filter_name
    datas = context.page.get_data()
    for data in datas:
        if filter_name == 'order':
            assert_equal(int(context.filter_text), int(data[filter_name]))
        elif filter_name == 'price':
            assert_equal(float(context.filter_text), float(data[filter_name]))
        elif filter_name == 'registrationtime':
            assert_in(context.filter_text,
                      time.strftime('%Y-%m-%dT%H:%M:%SZ', time.strptime(data[filter_name], '%B %d, %Y %I:%M')))
        else:
            assert_in(context.filter_text.lower(), data[filter_name].lower())
