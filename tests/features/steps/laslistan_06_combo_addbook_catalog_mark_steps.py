from behave import when


@when(u'går till katalogsidan')
def step_when__go_to_catalog_page(context):
    context.laslistan.navigation_button_click("catalog")
