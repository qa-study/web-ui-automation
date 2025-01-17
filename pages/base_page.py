import utilities.helper as helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element_wait(self, selector, locator):
        """
        element가 화면에 표시될 때까지 대기하는 메서드입니다.
        NoSuchElementException 등의 예외를 방지하고자 동적 메서드 수행 전 사전 조건으로 추가합니다.
        :param locator:
        :return:
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((selector, locator))
        )

    def driver_title(self, expected_title):
        """
        브라우저 타이틀 기대값과 실제값을 비교하여, 일치한 경우 Pass, 일치하지 않은 경우 Fail 처리합니다.
        :param expected_title:
        :return:
        """
        actual_title = self.driver.title
        assert actual_title == expected_title

    def click_element(self, selector, locator):
        """
        selenium의 click() 메서드를 커스터마이징 한 메서드입니다.
        element를 가져온 후 클릭합니다.
        :param selector:
        :param locator:
        :return:
        """
        self.element_wait(selector, locator)
        element = self.driver.find_element(by=selector, value=locator)
        helper.highlight(element)
        element.click()

    def input_element(self, selector, locator, text):
        """
        selenium의 send_keys() 메서드를 커스터마이징 한 메서드입니다.
        element를 가져온 후 입력합니다.
        :param selector:
        :param locator:
        :param text:
        :return:
        """
        self.element_wait(selector, locator)
        element = self.driver.find_element(by=selector, value=locator)
        element.send_keys(text)
        helper.highlight(element)

    def is_displayed(self, selector, locator):
        """
        selenium의 is_displayed() 메서드를 커스터마이징 한 메서드입니다.
        element를 가져온 후 화면에 표시되는 지 확인합니다.
        :param selector:
        :param locator:
        :return:
        """
        self.element_wait(selector, locator)
        element = self.driver.find_element(by=selector, value=locator)
        element.is_displayed()
        helper.highlight(element)