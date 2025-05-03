from behave import when, then
from playwright.sync_api import expect

@when(u'markerar böcker i en speciell ordning: "{order}"')
def step_when__marking_books_special_order(context, order):
    bocker_markerad_ordning = context.laslistan.verify_book([int(b) for b in order.split(",")])
    
    context.laslistan.ordning_bocker_markerade_katalog = context.laslistan.mark_books_catalog(bocker_markerad_ordning)
    
    
@then(u'ordningen på böckerna är den som i katalogen med "{last_title}" som sist')
def step_impl(context, last_title):
    markerade_bocker_favoriter = context.laslistan.sort_order_favorit_books(context.laslistan.ordning_bocker_markerade_katalog)
    markerade_bocker_favoriter.append(last_title)
    
    favoriter_lista = context.page.get_by_test_id("book-list").get_by_role("listitem")
    
    for i in range(favoriter_lista.count()):
        expect(favoriter_lista.nth(i).get_by_text(markerade_bocker_favoriter[i])).to_be_visible()

