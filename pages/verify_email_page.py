from playwright.sync_api import Page


class VerifyEmailPage():


    def __init__(self, page: Page) -> None:
        self.page = page


    def click_resend_link(self) -> None:
        self.page.wait_for_selector(
            'h1:has-text("Verify your email address")'
        )
        self.page.click(
            'span:has-text("click here to resend")'
        )
