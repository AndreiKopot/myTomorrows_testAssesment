from utilities.helpers import Helpers
from pages.start_page import StartPage
from pages.user_details_page import UserDetailsPage
from pages.verify_email_page import VerifyEmailPage
from pages.mail7_page import Mail7Page
from pages.choose_pw_page import ChoosePwPage
from pages.additional_info_page import AdditionalInfoPage
import allure


@allure.title("sign Up positive")
@allure.description("This test covers positive scenario of sign up")
@allure.tag("UI", "POSITIVE")
def test_sign_up_positive(
        helpers: Helpers,
        start_page: StartPage,
        details_page: UserDetailsPage,
        verify_email_page: VerifyEmailPage,
        mail7_page: Mail7Page,
        choose_pw_page: ChoosePwPage,
        additional_info_page: AdditionalInfoPage) -> None:

    email = helpers.email_random()
    start_page.start_creating_account()
    helpers.create_screenshot("Sign up page")

    start_page.click_create_account_btn()

    helpers.create_screenshot("User details page")
    details_page.fill_in_user_details(email)
    helpers.create_screenshot("User details filled")
    details_page.click_next_verification_btn()

    verify_email_page.click_resend_link()
    helpers.create_screenshot("Verification page")

    mail7_page.navigate_to_mail7(email)
    mail7_page.open_verifiation_email()
    helpers.create_screenshot("Mail7 page")
    new_tab = mail7_page.click_activate_account_btn()

    helpers.create_screenshot("Choose password page")
    choose_pw_page.check_fields_validation(new_tab)
    choose_pw_page.click_activate_button(new_tab)

    additional_info_page.fill_in_the_form(new_tab)
    helpers.create_screenshot("Additional form")
    additional_info_page.click_complete_setup_btn(new_tab)


