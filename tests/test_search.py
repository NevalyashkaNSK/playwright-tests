import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage, FilterType
from config.config_reader import ConfigReader


@pytest.mark.parametrize("name", ["city", "habits"])
@pytest.mark.parametrize("n", [10, 15])
@pytest.mark.parametrize("filter_type", [FilterType.LOW_TO_HIGH, FilterType.HIGH_TO_LOW])
def test_search_and_filter(page, name, n, filter_type):
    config = ConfigReader()
    page.goto(config.base_url)

    home_page = HomePage(page)
    home_page.search(name)

    search_results = SearchResultsPage(page)
    search_results.apply_filter(filter_type)
    prices = search_results.get_prices(n)

    if filter_type == FilterType.LOW_TO_HIGH:
        assert prices == sorted(prices), f"Цены не отсортированы по возрастанию: {prices}"
    else:
        assert prices == sorted(prices, reverse=True), f"Цены не отсортированы по убыванию: {prices}"
