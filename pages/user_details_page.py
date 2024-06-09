from playwright.sync_api import Page, expect


from utilities.helpers import Helpers


class UserDetailsPage(Helpers):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.enter_your_details_text = page.get_by_text('Enter your details')

    def fill_in_user_details(self, email:str) -> None:
        expect(self.enter_your_details_text).to_be_visible()
        self.page.locator('input:below(:text("Email Address"), 60)').fill(f'{email}@mail7.io')
        self.page.locator('input:below(:text("Confirm Email"), 60)').fill(f'{email}@mail7.io')
        self.page.get_by_placeholder("First name").fill("Andy")
        self.page.get_by_placeholder("Last name").fill("Test")
        self.page.get_by_role("checkbox",
                         name="By ticking this box, I consent to the processing of my personal data for the purposes of getting in touch with myTomorrows and create a profile on myTomorrows' platform.").check()

    def click_next_verification_btn(self) -> None:
        self.page.get_by_role("button", name="Next: verification").click()

    def fill_in_user_details_with_user_registered(self) -> None:
        expect(self.enter_your_details_text).to_be_visible()
        self.page.locator('input:below(:text("Email Address"), 60)').fill('andytest@mail7.io')
        self.page.locator('input:below(:text("Confirm Email"), 60)').fill('andytest@mail7.io')
        self.page.get_by_placeholder("First name").fill("Andy")
        self.page.get_by_placeholder("Last name").fill("Test")
        self.page.get_by_role("checkbox",
                              name="By ticking this box, I consent to the processing of my personal data for the purposes of getting in touch with myTomorrows and create a profile on myTomorrows' platform.").check()
