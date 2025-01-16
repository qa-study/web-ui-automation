from pages.탭_내비게이션 import 탭_내비게이션


def test_웹툰_탭_이동_확인(driver):
    탭_내비게이션(driver).webtoon_page_redirect()


def test_베스트도전_탭_이동_확인(driver):
    탭_내비게이션(driver).best_page_redirect()


def test_도전만화_탭_이동_확인(driver):
    탭_내비게이션(driver).challenge_page_redirect()


def test_마이페이지_탭_이동_확인(driver):
    탭_내비게이션(driver).mypage_page_redirect()