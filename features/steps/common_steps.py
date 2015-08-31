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


@step("I reloading page")
def step_impl(context):
    context.driver.refresh()
    context.page.wait_for_loading(240)


@step('fail')
@step('Fail')
def step_impl(context):
    raise NotImplementedError
