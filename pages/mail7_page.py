from playwright.sync_api import Page

from utilities.helpers import Helpers


class Mail7Page(Helpers):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def navigate_to_registered_mailbox(self) -> None:
        self.page.goto(f'https://console.mail7.io/admin/inbox/inbox?username=andytest@mail7.io',
                       wait_until='domcontentloaded')

    def navigate_to_mail7(self, email: str) -> None:
        self.page.goto(f'https://console.mail7.io/admin/inbox/inbox?username={email}@mail7.io', wait_until='domcontentloaded')

    def open_verifiation_email(self) -> None:
        self.page.wait_for_timeout(5000)
        self.page.click(
            '.btn:has-text("Refresh")'
        )

        self.page.wait_for_selector(
            '.subject:has-text("Welcome to myTomorrows!")'
        )

        self.page.click(
            '.subject:has-text("Welcome to myTomorrows!")'
        )

    def click_activate_account_btn(self) -> Page:

        iframe_element = self.page.wait_for_selector('.message iframe')
        iframe_content = iframe_element.content_frame()

        if not iframe_content:
            raise Exception('Message iframe is null!')

        confirm_link = iframe_content.wait_for_selector(
            'a:has-text("Activate your account")'
        )

        confirm_link.click()

        page_promise = self.page.context.wait_for_event('page')

        page_promise.wait_for_load_state()

        return page_promise