from behave import given, when, then
from playwright.sync_api import expect

from pages.laslistan import Laslistan

@given(u'att jag befinner mig på webbsidan Lässidan och sidan mina böcker')
def step_given__on_the_webpage_my_books(context):
    context.laslistan = Laslistan(context.page)
    context.page.goto(context.base_url)
    
    context.laslistan.navigation_button_click("favorites")
    

@then(u'när man kommer till mina böcker sidan bör det inte finnas någon favorit bok listad')
def step_then__my_books_page_empty(context):
    locator = context.laslistan.my_books_page_empty
    
    expect(locator).to_be_visible()
    
    