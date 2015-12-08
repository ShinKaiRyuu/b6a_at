import time

from behave import *
from nose.tools import assert_equal, assert_in

use_step_matcher("re")


@then("I write (?P<filter_text>.+) in (?P<filter_name>.+) Filter")
@then("I select (?P<filter_text>.+) in (?P<filter_name>.+) Filter")
def step_impl(context, filter_text, filter_name):
    context.filter_name = filter_name
    context.filter_text = filter_text
    if filter_text == 'page_name':
        context.filter_text = context.parent_page_data['name']
    if filter_text == 'partner_name':
        context.filter_text = context.partner_data['name']
    if filter_text == 'product_title':
        context.filter_text = context.product_data['title']
    context.page.filter_data(context.filter_name, context.filter_text)


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
        elif filter_name == 'updatedby':
            assert_in(context.filter_text.lower(), data['updated_by'].lower())
        else:
            assert_in(context.filter_text.lower(), data[filter_name].lower())
