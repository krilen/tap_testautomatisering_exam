from behave import given, when, then
from playwright.sync_api import expect

from pages.laslistan import Laslistan

@given(u'att jag befinner mig på webbsidan läslistan')
def step_give__on_the_webpage(context):
    context.laslistan = Laslistan(context.page)
    context.page.goto(context.base_url)


@then(u'bör jag se att titeln på webbsidan är "{title}"')
def step_impl(context, title):
    expect(context.page).to_have_title(title)


@then(u'att webbsidan har en rubrik med texten "{headline}"')
def step_impl(context, headline):
    locator = context.laslistan.heading(headline)

    expect(locator).to_be_visible()
    expect(locator).to_have_count(1)