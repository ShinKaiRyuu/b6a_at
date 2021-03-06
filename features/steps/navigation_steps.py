from behave import *
from nose.tools import assert_in
from webium.driver import get_driver

import pages

use_step_matcher("re")

PAGES_MAP = {
    'Main': pages.MainPage,
    'Login': pages.LoginPage,
    'Manage Products': pages.ManageProductsPage,
    'Create Product': pages.CreateProductPage,
    'View Product': pages.ViewProductPage,
    'Product': pages.ProductPage,
    'Manage Users': pages.ManageUsersPage,
    'Create User': pages.CreateUserPage,
    'Manage Partners': pages.ManagePartnersPage,
    'Create Partner': pages.CreatePartnerPage,
    'Update User Account Details': pages.UpdateUserAccountDetailsPage,
    'Update User Profile Details': pages.UpdateUserProfileDetailsPage,
    'User Information': pages.UserInformationPage,
    'User Assignments': pages.UserAssignmentsPage,
    'Create Role': pages.CreateRolePage,
    'Manage Roles': pages.ManageRolesPage,
    'Create Permission': pages.CreatePermissionPage,
    'Manage Permissions': pages.ManagePermissionPage,
    'Manage Pages': pages.ManagePagesPage,
    'Create Page': pages.CreatePagePage,
    'Parent Page': pages.ParentPagePage,
    'Additional Page': pages.AdditionalPagePage,
    'Inventory Group': pages.ManageInventorygroupsPage,
    'Update Inventory Group': pages.UpdateInventorygroupsPage,
    'Update item': pages.UpdateItemsPage,
    'Scoreboard': pages.ScoreboardPage,
    'Items': pages.ScoreboardItemsPage,
    'Partnership Portal': pages.PartnershipPortalPage,
}


@when("I open (?P<page_name>.+) page")
@step("I am on (?P<page_name>.+) page")
def step_impl(context, page_name):
    context.page_name = page_name
    page = PAGES_MAP[page_name]
    context.page = page(url=''.join([context.app_url, page.url_path]))
    context.page.open()
    context.page.wait_for_loading()


@then("I want to see '(?P<page_name>.+)' page")
def step_impl(context, page_name):
    context.page.wait_for_loading()
    page = PAGES_MAP[page_name]
    assert_in(page.url_path, get_driver().current_url)
    context.page = page()
