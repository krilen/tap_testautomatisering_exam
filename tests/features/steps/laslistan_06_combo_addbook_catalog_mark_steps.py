from behave import when
from playwright.sync_api import expect

from pages.laslistan import Laslistan


@when(u'går till katalogsidan')
def step_when__go_to_catalog_page(context):
    context.laslistan.navigation_button_click("catalog")

