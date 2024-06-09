import pytest
from playwright.sync_api import Page


from utilities.helpers import Helpers
from pages.start_page import StartPage
from pages.user_details_page import UserDetailsPage
from pages.verify_email_page import VerifyEmailPage
from pages.mail7_page import Mail7Page
from pages.choose_pw_page import ChoosePwPage
from pages.additional_info_page import AdditionalInfoPage


@pytest.fixture
def start_page(page: Page) -> StartPage:
    return StartPage(page)

@pytest.fixture
def details_page(page: Page) -> UserDetailsPage:
    return UserDetailsPage(page)

@pytest.fixture
def helpers(page: Page) -> Helpers:
    return Helpers(page)

@pytest.fixture
def verify_email_page(page: Page) -> VerifyEmailPage:
    return VerifyEmailPage(page)

@pytest.fixture
def mail7_page(page: Page) -> Mail7Page:
    return Mail7Page(page)

@pytest.fixture
def choose_pw_page(page: Page) -> ChoosePwPage:
    return ChoosePwPage(page)

@pytest.fixture
def additional_info_page(page: Page) -> AdditionalInfoPage:
    return AdditionalInfoPage(page)

