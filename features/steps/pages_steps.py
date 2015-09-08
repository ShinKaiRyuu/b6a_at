from behave import *
from nose.tools import assert_true, assert_equal, assert_in

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
    links = context.page.get_links()
    link = context.page.get_link(context.page_data['name'])
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
