from fixture.application import Application
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 1) зайти в админку
# 2) открыть каталог, категорию, которая содержит товары (страница http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1)
# 3) последовательно открывать страницы товаров и проверять, не появляются ли в логе браузера сообщения (любого уровня)

@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_browser_logs(app):
    app.login_admin()
    app.driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog") #открыли каталог
    wait = WebDriverWait(app.driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Catalog']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Rubber Ducks']"))).click() #перешли в категорию уток
    number_products = wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Duck"))) # список товаров для счетчика

    for i in range(1, len(number_products)):
            products = app.driver.find_elements_by_xpath("(//a[contains(.,'Duck')])") #товары которые будем кликать
            products[i].click()
            product_name = app.driver.find_element_by_css_selector('input[name="name[en]"]').get_attribute('value') #имя товара для отображения в логах
            #печатаем логи браузера к каждому открытому товару
            print(i, '-', product_name)
            for log in app.driver.get_log("browser"):
                print("Message:", log)

            app.driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1") # вернулись к списку товаров в категории
