import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_backet_verification(browser):
    browser.get(link)
    assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"),"Где кнопка то? Нету кнопки"
    #time.sleep(30)
