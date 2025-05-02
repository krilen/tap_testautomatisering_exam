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
    
        self.page.get_by_test_id("add-input-title").fill(book_info[0][1:-1])
        self.page.get_by_test_id("add-input-author").fill(book_info[1][1:-1])


    # My books page
    
    @property
    def my_books_page_empty(self):
        """
        Methond that checks to see if the default text when no books are listed
        is present on the webpage
        """
        return self.page.get_by_text(re.compile("När du valt, kommer dina favoritböcker att visas här", re.IGNORECASE))
    
    # Catalog
    
    @property
    def count_catalog_bookrows(self):
        """
        Method that counts the number of books that are listed in the catalog
        """
        return self.page.locator("main").locator(".book").count()


    def get_testid_by_bookrow(self, bookrow):
        """
        Method that gets the test id by fetching a bookrow in the catalog and
        convering the title into a testid
        Takes a parameter for which row.
         - F: means the first row, also known as row 0
         - L: means the last row
         - Any number will be the requested row by number always starts with 0
        """
        
        if not isinstance(bookrow, str):
            return None
        
        if bookrow == "L":
            book_index = self.count_catalog_bookrows -1
            
        elif bookrow == "F":
            book_index = 0
            
        else:
            try:
                book_index = int(bookrow)
                
            except:
                return None
            
        return "star-" +self.page.locator("main").locator(".book").nth(book_index).inner_text().split("\"")[1]


    def get_testid_by_booktitle(self, booktitle, prefix="star"):
        """
        Method that converts a book title into a testid
        Takes a title
        And a prefix
         - "star": for the catalog
         - "fav": for my books
        """
        
        if not isinstance(booktitle, str):
            return None
            
        return prefix +"-" +booktitle


    def verify_catalog_text(self, text):
        """
        Finds a specific text in the catalog
        Takes a text and a parameter
        """
        return self.page.locator("main").locator(".book").last.get_by_text(re.compile(text, re.IGNORECASE))