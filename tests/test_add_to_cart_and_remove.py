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


def test_add_to_cart_and_remove(app):
    app.eshop_home()
    for i in range(0, 3):
        app.driver.find_element_by_xpath("(//li[@class='product column shadow hover-light'])[1]").click() # открыли первый товар в рандомном списке

        qnt = app.driver.find_element_by_css_selector("span.quantity") # сохранили количество товаров в корзине
        intqnt = int(qnt.text)
        nextQntStr = str(intqnt + 1)    #требуемое количество товаров в корзине после добавления 1 товара

        app.driver.find_element_by_name("add_cart_product").click() #нажимаем кнопку добавить в корзину
        #указание ожидания до завершения анимации добавления в корзину. ждем обновления числа в счетчике корзины
        wait = WebDriverWait(app.driver, 10)  # seconds
        qnt2=By.CSS_SELECTOR,'span.quantity'
        #wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'span.quantity'),nextQntStr)) #строка ниже равнозначна этой
        wait.until(EC.text_to_be_present_in_element((qnt2), nextQntStr))
        app.eshop_home()

    app.driver.find_element_by_xpath("//a[contains(.,'Checkout »')]").click()  # перешли в корзину

    Product_in_cart = app.driver.find_element_by_xpath("//td[@style='text-align: center;']").text
    Productint =int(Product_in_cart)
    j=0
    while  Productint > 0:
        j = j + 1
        print(j)
        time.sleep(2)
        app.driver.find_element_by_xpath("(//button[contains(.,'Remove')])[1]").click() # кликаем удалить 1 товар из корзины
        # указание ожидания до завершения анимации удаления товара из корзины. ждем обновления числа в счетчике корзины
        wait = WebDriverWait(app.driver, 10)  # seconds
        wait.until(EC.visibility_of_element_located((By.NAME, 'remove_cart_item')))
        Product_in_cart = app.driver.find_element_by_xpath("//td[@style='text-align: center;']").text
        Productint = int(Product_in_cart)


    #wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'em'),"There are no items in your cart."))





