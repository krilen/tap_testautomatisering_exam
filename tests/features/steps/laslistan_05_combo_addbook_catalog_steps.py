from behave import then
from playwright.sync_api import expect


@then(u'när man går till katalogens sida har boken med dess titel: "{titel}" och författare: "{forfattare}" hamnat i listan med böcker')
def step_then(context, titel, forfattare):
    context.laslistan.navigation_button_click("catalog")
    
    locator_title = context.laslistan.verify_catalog_text(titel)
    expect(locator_title).to_be_visible()
    
    locator_forfattare = context.laslistan.verify_catalog_text(forfattare)
    expect(locator_forfattare).to_be_visible()


@then(u'ett korrekt katalog testid: "{testid}" har skapats')
def step_impl(context, testid):
    expect(context.page.get_by_test_id(testid)).to_be_visible()
