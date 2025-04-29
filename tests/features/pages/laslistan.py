import re


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

