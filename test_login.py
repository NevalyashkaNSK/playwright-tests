from playwright.sync_api import Page, expect

def test_invalid_login(page: Page):
    page.goto('http://2.26.162.45:8080/')
    page.get_by_role('link', name='Login').click() # использовал другой поиск по роли для практики
    page.get_by_test_id('login-username').fill("random_user")
    page.get_by_test_id('login-password').fill("random_password")
    page.get_by_test_id('login-submit').click()
    expect(page.get_by_test_id("login-submit-spinner")).to_be_visible()
    expect(page.get_by_test_id("login-error-inline")).to_have_text("Invalid login or password.")
    # Как будто-бы expect легко и просто использовать везде. На практике часто нужно использовать что-то кроме него?
    # То что он делает проверку, а не просто ожидает чего-то, разве это лишнее? ну делает и делает проверку, как будто лишним не будет
