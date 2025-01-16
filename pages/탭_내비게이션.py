import elements.el_webtoon_main as element
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class 탭_내비게이션(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def webtoon_page_redirect(self):
        BasePage.click_element(self, By.XPATH, element.xpath_webtoon_webtoon_tap)
        BasePage.is_displayed(self, By.XPATH, element.xpath_webtoon_webtoon_day_weeks)
        BasePage.driver_title(self, element.xapth_webtoon_webtoon_title)

    def best_page_redirect(self):
        BasePage.click_element(self, By.XPATH, element.xpath_webtoon_best_tap)
        BasePage.is_displayed(self, By.XPATH, element.xpath_webtoon_best_text)
        BasePage.driver_title(self, element.xpath_webtoon_best_title)

    def challenge_page_redirect(self):
        BasePage.click_element(self, By.XPATH, element.xpath_webtoon_challenge_tap)
        BasePage.is_displayed(self, By.XPATH, element.xpath_webtoon_challenge_text)
        BasePage.driver_title(self, element.xpath_webtoon_challenge_title)

    def mypage_page_redirect(self):
        BasePage.click_element(self, By.XPATH, element.xpath_webtoon_mypage_tap)
        BasePage.driver_title(self, element.xpath_webtoon_naverlogin_title)