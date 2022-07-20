from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_find_basket_button(browser, language):
    link=f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,".btn-add-to-basket")))
    assert len(button.text) >= 1, f"element {button} is present"