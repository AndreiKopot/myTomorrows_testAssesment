from playwright.sync_api import Page, expect

from utilities.helpers import Helpers


class AdditionalInfoPage(Helpers):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def fill_in_the_form(self, tab: Page) -> None:
        hcp = self.hcp_random()
        tab.wait_for_selector('span:has-text("Welcome to myTomorrows!")')
        tab.click('mat-select[ng-reflect-placeholder="General practitioner"]')
        tab.click('//span[contains(text(),"Nurse")]')
        tab.click('mat-select[ng-reflect-placeholder="Oncology"]')
        tab.click('//span[contains(text(),"Critical Care")]')
        tab.click('mat-select[ng-reflect-placeholder="Country"]')
        tab.click('//span[contains(text(),"Algeria")]')
        tab.get_by_placeholder("12345678").fill(hcp)
        tab.get_by_label('Yes').check()


    def click_complete_setup_btn(self, tab: Page)-> None:
        tab.get_by_role("button", name="Complete setup").click()

