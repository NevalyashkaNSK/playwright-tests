from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)


        self.search_input = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")

    def search(self, name: str):
        self.search_input.fill(name)
        self.search_button.click()