from behave import *
from nose.tools import assert_true, assert_equal, assert_in, assert_false

from helpers.data_helpers import create_page_data

use_step_matcher("re")


@step("I want to see table with all pages")
def step_impl(context):
    pages = context.page.get_data()
    assert_true(len(pages) >= 1)


@when("I create new page")
def step_impl(context):
    page = create_page_data()
    context.page.create_new_page(**page)
    context.page_data = page


@step("I want to see created page in list")
@step("I want to see updated page in list")
def step_impl(context):
    context.page.filter_data('name', context.page_data['name'])
    page = [page for page in context.page.get_data() if page['name'] == context.page_data['name']]
    assert_equal(len(page), 1)
    page = page[0]
    assert_equal(page['status'].lower(), context.page_data['status'])


@then("I want to see created page in link list")
def step_impl(context):
    link = context.page.get_link(context.page_data['name'])
    links = context.page.get_links()
    assert_in(links, link)
    context.link = link
    link.click()


@then("I want to see created page and it content")
def step_impl(context):
    assert_true(context.driver.title, context.page_data['title'])


@when("I dragndrop created page to top position")
def step_impl(context):
    context.page.dragndrop_page(context.parent_page_id)


@then("I want to see created page in top position")
def step_impl(context):
    pages = context.page.get_data()
    assert_true(pages[0]['name'], context.parent_page_data['name'])
    context.driver.refresh()


@then("I want to see created page in top of list")
def step_impl(context):
    links = context.page.get_links()
    assert_true(links[0].text, context.parent_page_data['name'])
    context.driver.refresh()


@step("I want to see created page in header")
def step_impl(context):
    header_links = context.page.get_headers_links()
    assert_true(header_links[0].text, context.parent_page_data['name'])


@when("I open parent")
def step_impl(context):
    context.page.filter_data('name', context.parent_page_data['name'])
    context.page.open_page(context.parent_page_data['slug'])


@then("I want to see parent")
def step_impl(context):
    assert_in(context.parent_page_data['title'], context.driver.title)


@step("I want to see additional link")
def step_impl(context):
    assert_true(context.additional_page_data['name'] in context.driver.page_source)


@when("I open additional")
def step_impl(context):
    context.page.open_additional_page(context.additional_page_data['name'])


@then("I want to see no link to draft parent page")
def step_impl(context):
    context.page.filter_data('name', context.parent_page_data['name'])
    assert_false(context.page.is_element_present('link_to_page'))


@then("I want to see no link to draft additional page")
def step_impl(context):
    context.page.filter_data('name', context.additional_page_data['name'])
    assert_false(context.page.is_element_present('link_to_page'))


@when("I open page from parent context_data")
def step_impl(context):
    context.driver.get(url=''.join([context.app_url, '/site/page?slug=', context.parent_page_data['slug']]))


@when("I open page from additional context_data")
def step_impl(context):
    context.driver.get(url=''.join([context.app_url, '/site/page?slug=', context.additional_page_data['slug']]))


@when("I update page")
def step_impl(context):
    context.page.view_page(context.parent_page_data, context.parent_page_id)


@step("I want to see page details")
def step_impl(context):
    actual_page_data = context.page.get_page_details()
    assert_equal(actual_page_data, context.parent_page_data)


@then("I want to change page details")
def step_impl(context):
    page = create_page_data()
    context.page.update_page_details(**page)
    context.old_page_data = context.parent_page_data
    context.page_data = page
