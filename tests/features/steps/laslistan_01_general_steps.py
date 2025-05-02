from behave import given, when, then
from playwright.sync_api import expect

from pages.laslistan import Laslistan


@given(u'att jag befinner mig på webbsidan Läslistan')
def step_given__on_the_webpage(context):
    context.laslistan = Laslistan(context.page)
    context.page.goto(context.base_url)


@then(u'bör jag se att titeln på webbsidan är "{title}"')
def step_then__title_of_the_webpage(context, title):
    expect(context.page).to_have_title(title)


@then(u'att webbsidan har en rubrik med texten "{headline}"')
def step_then__have_the_heading(context, headline):
    locator = context.laslistan.heading(headline)

    expect(locator).to_be_visible()
    expect(locator).to_have_count(1)
    
    
@then(u'bör jag kunna se att det finns "{button_count:d}" st navigationsknappar på webbsidan')
def step_then__count_navigation_button(context, button_count):
    expect(context.page.locator("header").get_by_role("button")).to_have_count(button_count)
    
    
@then(u'bör jag kunna se att det är rätt namn och testid på vardera navigationsknapp på webbsidan')
def step_then__see_navigation_button_and_testid(context):
    for row in context.table:
        locator = context.laslistan.verify_navigation_button(row["namn"], row["testid"])
            
        expect(locator).to_have_count(int(row["count"]))


@when(u'när jag klickar på en navigeringsknapp med ett specifikt test-id: "{testid}"')
def step_when__click_on_navbutton(context, testid):
    context.laslistan.navigation_button_click(testid)


@then(u'bör jag se att den aktuella navigeringknappen, "{testid}", blivit deaktiverad')
def step_then__verify_navigation_button_deactivated(context, testid):
    expect(context.page.get_by_test_id(testid)).to_be_disabled()


@then(u'självaste innehållet för sidan har ett div element med en speciell class: "{divclass}"')
def step_then__verify_navigation_webpage(context, divclass):
    expect(context.page.locator("main").locator(divclass)).to_be_visible()
