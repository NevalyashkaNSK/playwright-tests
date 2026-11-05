from enum import StrEnum
from pages.base_page import BasePage


class FilterType(StrEnum):
    LOW_TO_HIGH = "Price: low to high"
    HIGH_TO_LOW = "Price: high to low"


class SearchResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.filter_dropdown = page.get_by_test_id("filter-sort")
        self.apply_button = page.get_by_test_id("apply-filters-button")
        self.price_elements = page.locator("[data-testid^='search-result-price']")
        self.loader = page.get_by_test_id("results-loader-svg")

    def apply_filter(self, filter_type: FilterType):
        self.filter_dropdown.select_option(label=filter_type.value)
        self.apply_button.click()
        self.loader.wait_for(state="hidden")

    def get_prices(self, n: int):
        prices = []
        for i in range(n):
            element = self.price_elements.nth(i)
            raw_price = element.get_attribute("data-price")
            price = float(raw_price) / 100.0
            prices.append(price)
        return prices
