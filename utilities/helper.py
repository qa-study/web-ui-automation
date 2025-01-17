import time


def highlight(element, effect_time=0.1, color="#FF0000", border=5):
    """
    엘리먼트에 상호작용할 때, CSS 하이라이팅 적용
    :param element: CSS를 적용할 엘리먼트
    :param effect_time: CSS효과 지속시간
    :param color: CSS border의 컬러 HEX코드
    :param border: border의 굵기
    :return:
    """
    driver = element._parent
    original_style = element.get_attribute('style')
    def apply_style(style):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)
    apply_style(f"border: {border}px solid {color};")
    time.sleep(effect_time)
    apply_style(original_style)