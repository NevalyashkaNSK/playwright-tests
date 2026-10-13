from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()

BASE_URL = 'http://2.26.162.45:8080/'
EXPECTED_ERROR = 'Invalid login or password.'


def test_invalid_login(page: Page):
    username = fake.user_name()
    password = fake.password()

    page.goto(BASE_URL)
    page.get_by_role('link', name='Login').click()  # использовал другой поиск по роли для практики
    page.get_by_test_id('login-username').fill(username)
    page.get_by_test_id('login-password').fill(password)
    page.get_by_test_id('login-submit').click()

    spinner = page.get_by_test_id("login-submit-spinner")
    spinner.wait_for(state='visible')
    is_visible = spinner.is_visible()
    assert is_visible, f"Спиннер не появился. Actual result: {is_visible}, Expected result: True"

    error = page.get_by_test_id("login-error-inline")
    error.wait_for(state='visible')
    expect(error).to_have_text(EXPECTED_ERROR)
    actual_text = error.text_content()
    assert actual_text == EXPECTED_ERROR, f'Ожидалось: {EXPECTED_ERROR!r}, получено: {actual_text!r}'
