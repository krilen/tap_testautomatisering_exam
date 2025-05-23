from behave import given, then
from playwright.sync_api import expect

from pages.laslistan import Laslistan


@given(u'att man befinner sig på webbsidan Lässidan och sidan mina böcker')
def step_given__on_the_webpage_my_books(context):
    context.laslistan = Laslistan(context.page)
    context.page.goto(context.base_url)
    
    context.laslistan.navigation_button_click("favorites")
    

@then(u'när man kommer till mina böcker sidan informeras man om att här kommer dina favoritböcker listas')
def step_then__my_books_page_empty(context):
    locator = context.laslistan.my_books_page_empty
    
    expect(locator).to_be_visible()
    

@then(u'när man kommer till mina böcker sidan informeras man inte längre om att här kommer favoritböcker att listas')
def step_then__my_books_page_empty(context):
    locator = context.laslistan.my_books_page_empty
    
    expect(locator).not_to_be_visible()


@then(u'kan man se att boken finns listad som en favoritbok: "{title}"')
def step_then__book_listed_as_favorite(context, title):
    testid = context.laslistan.get_testid_by_booktitle(title, "fav")

    expect(context.page.get_by_test_id(testid)).to_be_visible()


@then(u'kan man se att boken inte finns listad som en favoritbok: "{title}"')
def step_then__book_not_listed_as_favorite(context, title):
    testid = context.laslistan.get_testid_by_booktitle(title, "fav")

    expect(context.page.get_by_test_id(testid)).not_to_be_visible()
