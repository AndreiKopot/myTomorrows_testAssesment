from playwright.sync_api import Page, expect


class StartPage():

    URL = 'https://platform-qa.mytomorrows.com'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.signup_button = page.locator("xpath=//a[normalize-space()='Create account']")
        self.create_account_heading = page.get_by_role("heading", name="Create your account")
        self.create_account_button = page.locator("xpath = //span[@class='mdc-button__label']")

    # Navigate to myTomorrows website and button click
    def start_creating_account(self) -> None:
        self.page.goto(self.URL, wait_until='domcontentloaded')
        self.signup_button.click()

    def click_create_account_btn(self) -> None:
        expect(self.create_account_heading).to_be_visible()
        self.create_account_button.click()
