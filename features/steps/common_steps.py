from behave import *

use_step_matcher("re")


@when("I click on (?P<element_name>.+) (?P<element_type>.+)")
def step_impl(context, element_name, element_type):
    types_map = {
        'link': 'link',
        'button': 'btn',
        'product': 'product'
    }
    element = '_'.join([element_name.lower().replace(' ', '_'), types_map[element_type]])
    getattr(context.page, element).click()


@then("I want to get result - (?P<result>.+)")
def step_impl(context, result):
    context.execute_steps("""
        Then {}
    """.format(result))

# @when("I choose option (?P<option>.+) of select (?P<select>.+)")
# def step_impl(context, option, select):
#     context.filter_type = select
#     context.filter_value = option
#     context.page.choose_option_of_select(option, select)
#
#
# @step("I click (?P<btn_text_or_title>.+) button")
# def step_impl(context, btn_text_or_title):
#     if hasattr(context.page, 'save_table'):
#         context.page.save_table()
#
#     if 'on table' in context.step_name:
#         context.page.click_btn_by_title(btn_text_or_title)
#     elif 'on widget' in context.step_name:
#         context.page.click_by_text(btn_text_or_title)
#     else:
#         context.page.click_btn_by_text(btn_text_or_title)


@step("I reloading page")
def step_impl(context):
    context.driver.refresh()
    context.page.wait_for_loading(240)


@step('fail')
@step('Fail')
def step_impl(context):
    raise NotImplementedError
