from behave import given, when, then
from playwright.sync_api import expect

from pages.laslistan import Laslistan


@given(u'att man befinner sig på webbsidan Läslistan och sidan lägg till bok')
def step_given__on_the_webpage_add_books(context):
    context.laslistan = Laslistan(context.page)
    context.page.goto(context.base_url)
    
    context.laslistan.navigation_button_click("add-book")


@then(u'när man kommer till lägg till bok sidan bör inte en bok kunnas läggas till')
def step_then__add_book_page(context):
    expect(context.page.get_by_test_id("add-submit")).to_be_disabled()


@then(u'fälten för titel och författare skall vara tomma')
def step_then__title_and_author_fields_be_empty(context):
    expect(context.page.get_by_test_id("add-input-title")).to_be_empty()
    expect(context.page.get_by_test_id("add-input-author")).to_be_empty()


@when(u'man skriver in titel och författare till en bok')
def step_when__add_books_title_and_author(context): 
    context.laslistan.add_book("Moby-Dick", "Herman Melville")


@then(u'skall en bok kunnas läggas till')
def step_then__possible_to_add_a_book(context):
    expect(context.page.get_by_test_id("add-submit")).not_to_be_disabled()


@when(u'man skriver in titel och författare till en bok: {titel}, {forfattare}')
def step_when__add_books_title_an_or_auhor(context, titel, forfattare):
    context.laslistan.add_book(titel, forfattare)


@then(u'måste både titel och författare anges för att en bok skall "{accepteras:d}"')
def step_then__verify_if_book_can_be_added(context, accepteras):
    if bool(accepteras):
        expect(context.page.get_by_test_id("add-submit")).not_to_be_disabled()
        
    else:
        expect(context.page.get_by_test_id("add-submit")).to_be_disabled()


@when(u'klickar man på lägg till ny bok knappen')
def step_when__click_to_add_book(context):
    context.page.get_by_test_id("add-submit").click(timeout=200)
