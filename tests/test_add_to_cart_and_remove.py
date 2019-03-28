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

    # Product_in_cart = app.driver.find_element_by_xpath("//td[@style='text-align: center;']").text
    # Productint =int(Product_in_cart)

#--------
    # повторяем цикл удаления пока в таблице есть sku любого товара
    # while len(app.driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody//td[3]")) > 0:
    #
    #
    #     app.driver.find_element_by_xpath("(//button[contains(.,'Remove')])[1]").click() # кликаем удалить 1 товар из корзины
    #     time.sleep(2)
    #     # указание ожидания до завершения анимации удаления товара из корзины. ждем обновления числа в счетчике корзины
    #     wait = WebDriverWait(app.driver, 10)  # seconds
    #     wait.until(EC.element_to_be_clickable((By.NAME, 'remove_cart_item')))
    #
#------------
    # Удаление товаров из корзины

    products = app.driver.find_elements_by_css_selector('td.item') #список товаров в корзине
    block = app.driver.find_element_by_css_selector('div#checkout-cart-wrapper') #выделили блок содержащий кнопку remove
    for i in range(len(products)):
        remove = app.driver.find_elements_by_css_selector('button[value = Remove]') #выделили кнопку remove
        for j in remove:
            wait.until(EC.visibility_of(block.find_element_by_css_selector('form[name=cart_form]'))) #ждем обработку удаления и видимость оставшихся товаров
            wait.until(EC.visibility_of(j)).click()     #жмем кнопку удалить
            wait.until(EC.staleness_of(products[0])) #ждем обновление первого товара в списке корзины
            break
        continue
    wait.until(EC.staleness_of(app.driver.find_element_by_css_selector('div#box-checkout-summary')))

    # проверяем что в корзине не осталось ни одного sku
    assert len(app.driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody//td[3]")) == 0



