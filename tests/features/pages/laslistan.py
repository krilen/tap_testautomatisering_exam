import re

def parse_empty_string(v):
    if v == '""':
        return None
    else:
        return v[1:-1]



class Laslistan():
    
    
    def __init__(self, page):
        self.page = page


    def heading(self, text):
        """
        Method that goes through all of the headings (hX) with a specific text
        Takes a parameter for the specific text (string) and returns the locator of the
        found heading element with the text
        """
        if not isinstance(text, str):
            return None

        search_text = re.compile(text, re.IGNORECASE)

        return self.page.get_by_role("heading", name=search_text)

    @property
    def _navigation(self):
        """
        Method to get the navigation part of the page
        """
        return self.page.get_by_role("navigation")


    #@property
    #def navigation_buttons(self):
    #	"""
    #	Method to get the navigation buttons on the page
    #	"""
    #	return self._navigation.get_by_role("button")


    def verify_navigation_button(self, name, testid):
        """
        Method to verify a navigation button by its name and testid
        Takes two parameters the namne and the testid for that button.
        By selecting the navigation button using its testid and verifying that button has that name
        """
        if not isinstance(name, str) or not isinstance(testid, str):
            return None

        return self._navigation.get_by_test_id(testid).get_by_text(re.compile(name, re.IGNORECASE))


    def navigation_button_click(self, testid):
        """
        Method that goes through the navigation buttons on the page before any of them are clicked
        If the button is disabled we are already on the correct page and the button is disabled and
        can not be clicked.
        Takes a parameter for the testid for the navigation button we are looking for to click on
        """
        button_count = self.page.locator("header").locator("button").count()

        is_disabled = False

        for i in range(button_count):
            button = self.page.locator("header").locator("button").nth(i)

            if button.get_attribute('data-testid') == testid:
                is_disabled = button.get_attribute('disabled') is not None
                break

        if not is_disabled:
            self.page.get_by_test_id(testid).click(timeout=200)



    def add_book(self, title, author):
        """
        Method for adding title and autor to the form
        Takes two parameters title and author
        Allows empty strings can be used if needed
        """
        book_info = []

        if parse_empty_string(title) == None:
            book_info.append("")

        else:
            book_info.append(title)

        if parse_empty_string(author) == None:
            book_info.append("")

        else:
            book_info.append(author)
    
        self.page.get_by_test_id("add-input-title").fill(book_info[0])
        self.page.get_by_test_id("add-input-author").fill(book_info[1])


    # My books page
    
    @property
    def my_books_page_empty(self):
        return self.page.get_by_text(re.compile("När du valt, kommer dina favoritböcker att visas här", re.IGNORECASE))
