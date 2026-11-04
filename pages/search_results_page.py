from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.filter_dropdown = page.get_by_test_id("filter-sort")
        self.apply_button = page.get_by_test_id("apply-filters-button")
        self.price_elements = page.locator("[data-testid^='search-result-price']")

    def wait_for_open(self):
        self.price_elements.first.wait_for(state="visible")

    def apply_filter(self, filter_type: str):
        self.filter_dropdown.select_option(label=filter_type)

        self.apply_button.click()

        self.page.wait_for_url("**sort=**") # Вот тут я долго не мог понять, что надо дождаться, пока урл изменится

        self.price_elements.first.wait_for(state="visible")

    def get_prices(self, n: int):
        prices = []
        for i in range(n):
            price_text = self.price_elements.nth(i).text_content()

            price = float(price_text.replace("RUB", "").strip())
            prices.append(price)
        return prices
