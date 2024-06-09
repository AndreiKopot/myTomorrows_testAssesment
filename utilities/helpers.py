import allure
from playwright.sync_api import Page
import string
import random


class Helpers():

    def __init__(self, page: Page) -> None:
        self.page = page

    def create_screenshot(self, name) -> None:
        png_bytes = self.page.screenshot()
        allure.attach(
            png_bytes,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def email_random(self) -> str:
        length = 10
        result = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
        email = str(result)
        return email

    def hcp_random(self) -> str:
        length = 8
        result = ''.join(str(random.randint(0, 9)) for _ in range(length))
        hcp = str(result)
        return hcp
