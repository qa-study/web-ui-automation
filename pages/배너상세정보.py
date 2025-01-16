import elements.el_webtoon_main as element
import elements.el_webtoon_detail as ele_detail
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Banner(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def banner1_get_text(self):
        title = BasePage.get_title(self, By.XPATH, element.xpath_webtoon_banner_1_text)
        text = title.split("\n")
        return text

    def banner1_click(self):
        BasePage.click_element(self, By.XPATH, element.xpath_webtoon_banner_1)

    def get_banner1_detail_title(self):
        BasePage.is_displayed(self, By.XPATH, ele_detail.xpath_webtoon_banner_detail_title)
        actual_title = BasePage.get_title(self, By.XPATH, ele_detail.xpath_webtoon_banner_detail_title)
        return actual_title

    def extract_data(self, raw_data):
        # 제거할 단어들
        exclude_words = ["∙", "•", "글", "그림", "원작", "15세 이용가"]

        # raw_data를 개행으로 분리
        data_list = raw_data.split("\n")

        # 제외 단어를 필터링하여 새로운 리스트 생성
        filtered_data = [item.strip() for item in data_list if item.strip() and item.strip() not in exclude_words]

        return filtered_data

    def get_actual_writer(self):
        BasePage.is_displayed(self, By.XPATH, ele_detail.xpath_webtoon_banner_detail_writers)
        actual_writers = BasePage.get_title(self, By.XPATH, ele_detail.xpath_webtoon_banner_detail_writers)
        print(f"detail get_actual_writers: {actual_writers}")
        result = self.extract_data(actual_writers)
        print(result)


    def banner1_detail_check_writer(self, expected_writers):
        # 상세정보에 있는 첫번째 작가가 목록에 있는 작가 목록중 포함되어 있으면 true반환
        self.is_displayed(By.XPATH, ele_detail.xpath_webtoon_banner_detail_writer1)
        first_actual_writer = BasePage.get_title(self, By.XPATH, ele_detail.xpath_webtoon_banner_detail_writer1)
        print(f"detail first_actual writer: {first_actual_writer}")
        if "/" in expected_writers:
            # "/" 기준으로 문자열 나누기
            writer_list = expected_writers.split("/")
        else:
            # "/"가 없으면 리스트로 감싸기
            writer_list = [expected_writers]

        for writer in writer_list:
            print(f"-----writer: {writer}, actual_writer: {first_actual_writer}")
            if first_actual_writer in writer:
                return True
            else:
                print(f"'{first_actual_writer}'는 '{writer}'에 포함되어 있지 않습니다.")

        return False

    def get_detail_check_up(self):
        text = BasePage.get_title(self, By.XPATH, ele_detail.xpath_webtoon_content1)
        text_list = text.split("\n")
        #text_list: ['1화 19세기로', 'up', '별점', '9.86', '25.01.15']
        actual_up = text_list[1]
        return actual_up

