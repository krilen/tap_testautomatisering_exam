from behave import given, when, then
from playwright.sync_api import expect

from pages.laslistan import Laslistan

@given(u'att man befinner sig på webbsidan Lässidan och sidan katalog')
def step_given__on_the_webpage_my_books(context):
    context.laslistan = Laslistan(context.page)
    context.page.goto(context.base_url)
    
    context.laslistan.navigation_button_click("catalog")
    

@then(u'bokrad, "{bokrad}", är inte markerad')
def step_then__bookrow_is_not_marked(context, bokrad):
    testid = context.laslistan.get_testid_by_bookrow(bokrad)
    
    expect(context.page.get_by_test_id(testid)).to_have_class("star")


@when(u'klickar på markeringsknappen för bokraden, "{bokrad}"')
def step_impl(context, bokrad):
    testid = context.laslistan.get_testid_by_bookrow(bokrad)
    context.page.get_by_test_id(testid).click(timeout=200, force=True)


@then(u'bokrad, "{bokrad}", är markerad')
def step_then__bookrow_is_marked(context, bokrad):
    testid = context.laslistan.get_testid_by_bookrow(bokrad)
    
    expect(context.page.get_by_test_id(testid)).to_have_class("star selected")


@when(u'"{antal_klick:d}" klickningar på markeringsknappen för bokraden, "{bokrad}"')
def step_when__toggling_of_a_bookrow(context, antal_klick, bokrad):
    testid = context.laslistan.get_testid_by_bookrow(bokrad)
    
    for _ in range(antal_klick):
        context.page.get_by_test_id(testid).click(timeout=200, force=True)


@then(u'antal klickningar avgör om bokraden, "{bokrad}", blir markerad, "{markerad:d}", eller inte')
def step_then_toggle_even_odd_marks_bookrow(context, bokrad, markerad):
    testid = context.laslistan.get_testid_by_bookrow(bokrad)
    
    if bool(markerad):
        expect(context.page.get_by_test_id(testid)).to_have_class("star selected")
    
    else:
        expect(context.page.get_by_test_id(testid)).to_have_class("star")
