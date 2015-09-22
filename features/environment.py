from datetime import datetime
from sys import platform

from webium.driver import get_driver

from helpers.app_helpers import APP_URL
from helpers.driver_helpers import get_updated_driver
from helpers import app_helpers


def before_all(context):
    if 'linux' in platform:
        from pyvirtualdisplay import Display
        context.xvfb = Display(visible=0, size=(1366, 768)).start()
    else:
        context.save_screenshots = True
        context.close_after_all = False

    context.driver = get_updated_driver()
    context.app_url = APP_URL
    context.created_items = {}
    context.skip_filters = 1
    context.skip_sorting = 1


def before_scenario(context, scenario):
    if context.skip_filters == 1:
        if 'Filter' in scenario.name:
            scenario.mark_skipped()
    if context.skip_sorting == 1:
        if 'Sort' in scenario.name:
            scenario.mark_skipped()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        if getattr(context, 'save_screenshots', True):
            take_screenshot(scenario, context.step_name)
    get_driver().delete_all_cookies()
    delete_created_items(context)


def before_step(context, step):
    context.step_name = step.name


def after_all(context):
    if getattr(context, 'close_after_all', True):
        get_driver().quit()

    if hasattr(context, 'xvfb'):
        context.xvfb.stop()


def take_screenshot(scenario, step_name):
    scenario_name = scenario.name.replace('@', '')
    feature_filename = scenario.filename.split('/')[-1].split('.')[0]
    datetime_part = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    dir_name = './test-results/screenshots'
    get_driver().get_screenshot_as_file('{0}/{1}__{2}__{3}__{4}.png'.format(
        dir_name, datetime_part, feature_filename, scenario_name, step_name))


def delete_created_items(context):
    delete_map = {
        'users': app_helpers.delete_user,
        'products': app_helpers.delete_product,
        'partners': app_helpers.delete_partner,
        'pages': app_helpers.delete_page,
        'inventory_group': app_helpers.delete_inventory_group,
    }

    if context.created_items:
        for item_type, ids in context.created_items.items():
            for _id in ids:
                delete_map[item_type](_id)
