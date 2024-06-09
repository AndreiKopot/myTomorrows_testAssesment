from playwright.sync_api import Page, expect

class ChoosePwPage():
    wrong_pws = ["1q2w3e4r","1q2w3e $","1q2w3e$"]
    correct_pw = "1q2w3e4r!Q"
    def __init__(self, page: Page) -> None:
        self.page = page

    def check_fields_validation(self, tab: Page):
        expect(tab.get_by_text('Choose a password')).to_be_visible()
        activate_button = tab.get_by_role("button", name="Activate account")

        # Check negative passwords
        for pw in self.wrong_pws:
            tab.get_by_placeholder("Enter your password").fill(pw)
            tab.get_by_placeholder("Confirm your password").fill(pw)
            expect(activate_button).to_be_disabled()

        # Check positive password
        tab.get_by_placeholder("Enter your password").fill(self.correct_pw)
        tab.get_by_placeholder("Confirm your password").fill(self.correct_pw)
        expect(activate_button).to_be_enabled()

    def click_activate_button(self, tab: Page):
        tab.get_by_role("button", name="Activate account").click()

    def error_message_shown(self,tab:Page):
        tab.wait_for_selector(
            'mat-snack-bar-container:has-text("Password is already set.")'
        )