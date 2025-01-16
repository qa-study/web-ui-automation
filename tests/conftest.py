import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    # 옵션 객체 추가하여 테스트 시작 시 브라우저 창 최대화 Default 적용
    options = Options()
    options.add_argument("--start-maximized")

    # WebDriver 초기화 작업 후 네이버 웹툰 URL 열기
    driver = webdriver.Chrome(options=options)
    driver.get("https://comic.naver.com/index")
    driver.implicitly_wait(5)
    yield driver