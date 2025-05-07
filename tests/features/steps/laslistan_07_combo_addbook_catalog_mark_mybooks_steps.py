from behave import when


@when(u'går till mina böcker sidan')
def step_when__go_to_my_books_page(context):
    context.laslistan.navigation_button_click("favorites")
