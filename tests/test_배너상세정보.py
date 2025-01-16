from pages.배너상세정보 import Banner

def test_배너1_클릭하여_상세정보와_확인(driver):
    text = Banner(driver).banner1_get_text()
    expected_up = text[0]
    expected_title = text[1]
    expected_writers = text[2]
    print(f"목록 up: {expected_up}")
    print(f"목록 title: {expected_title}")
    print(f"목록 writers: {expected_writers}")

    Banner(driver).banner1_click()
    detail_actual_title = Banner(driver).get_banner1_detail_title()
    print(f"상세 title: {detail_actual_title}")
    assert detail_actual_title == expected_title

    Banner(driver).banner1_detail_check_writer(expected_writers)

    detail_actual_up = Banner(driver).get_detail_check_up()
    assert detail_actual_up.upper() == expected_up.upper()
