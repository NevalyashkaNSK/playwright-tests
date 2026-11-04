import pytest
from pytest import ExitCode

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config.config_reader import ConfigReader


@pytest.mark.parametrize("name, n, filter_type", [
    ("city", 10, "Price: low to high"),
    ("city", 15, "Price: high to low"),
    ("habits", 10, "Price: low to high"),
    ("habits", 15, "Price: high to low"),
])
def test_search_and_filter(page, name, n, filter_type):
    config = ConfigReader()

    # 1. Перейти на главную страницу
    page.goto(config.base_url)

    # 2. Ввести в поиск name
    home_page = HomePage(page)
    home_page.search(name)

    # 3. Перейти на страницу результатов
    search_results = SearchResultsPage(page)
    search_results.wait_for_open()

    # 4. Установить фильтр
    search_results.apply_filter(filter_type)

    # 5. Получить цены первых n статей
    prices = search_results.get_prices(n)

    # 6. Проверить, что цены отсортированы
    if "low to high" in filter_type:
        assert prices == sorted(prices), "Цены не отсортированы {prices}"
    else:
        assert prices == sorted(prices, reverse=True), f"Цены не отсортированы по убыванию: {prices}"
    print(f"URL: {page.url}")
    print(f"Цены: {prices}")