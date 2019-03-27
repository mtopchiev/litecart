from fixture.application import Application
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time



@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
WebDriverWait

def test_add_to_cart_and_remove(app):
    app.eshop_home()
    for i in range(0, 3):
        app.driver.find_element_by_xpath("(//li[@class='product column shadow hover-light'])[1]").click()

        #qnt = app.driver.find_element_by_xpath("//span[@class='quantity'][contains(.,'0')]")
        #qnt = app.driver.find_element_by_css_selector("div#cart span.quantity")
        qnt = app.driver.find_element_by_css_selector("span.quantity")
        intqnt = int(qnt.text)
        listqnt = list(qnt.text)
        nextQntStr = str(intqnt + 1)

        app.driver.find_element_by_name("add_cart_product").click()
        wait = WebDriverWait(app.driver, 10)  # seconds
        #app.driver.refresh()
      #  wait.until(EC.text_to_be_present_in_element(listqnt,nextQntStr))
                #Element(By.cssSelector("span.quantity")), String.valueOf(count + 1)));

        qnt2 = app.driver.find_element_by_xpath("//span[@class='quantity'][contains(.,'"+str(i+1)+"')]")

        app.eshop_home()

    time.sleep(5)