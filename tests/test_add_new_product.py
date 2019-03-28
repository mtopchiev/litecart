from fixture.application import Application
import pytest
import random
import string
from selenium.webdriver.support.ui import Select



#добавить новый товар
#заполнить только информацию на вкладках General, Information и Prices.
#Картинку с изображением товара нужно уложить в репозиторий вместе с кодом.
#После сохранения товара нужно убедиться, что он появился в каталоге (в админке).


#генерим набор из букв, цифр, пробелов
def random_string(prefix, maxlen):  #prefix это слово перед сгенерированной кашей, maxlen это максимальная длина строки
    syblols = string.ascii_letters + string.digits +" "*10 #сгенерили строку с алфавитом и набором цифр и 10 пробелами
    return prefix + "".join([random.choice(syblols) for i in range(random.randrange(maxlen))]) #склеенный набор рандомных букв/цифр в строку

@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

itemname= random_string("name",9)
short_description = "Lorem Ipsum is simply dummy text"
description = "t was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
quantity="10"
current_path_to_image = "D:\GitHub\litecart\pictures"
picture_name = "IMG_4751.jpg"
manufacturer = "ACME Corp."
purchase_price= "24.99"

def test_shop_signup(app):
    app.login_admin()
    app.driver.find_element_by_xpath("//span[contains(.,'Catalog')]").click()
    app.driver.find_element_by_xpath("// a[contains(., 'Add New Product')]").click()
    app.driver.find_element_by_xpath("(// input[@ value='1'])[1]").click() # выбираем статус Enabled
    app.driver.find_element_by_name("name[en]").click()
    app.driver.find_element_by_name("name[en]").send_keys(itemname) #название товара
    app.driver.find_element_by_xpath("//input[contains(@data-name,'Subcategory')]").click()
    app.driver.find_element_by_xpath("//input[contains(@name,'product_groups[]')]").click() #указали gender unisex
    app.driver.find_element_by_name("quantity").click()
    app.driver.find_element_by_name("quantity").send_keys(quantity)
    app.driver.find_element_by_name("sold_out_status_id").click()
    Select(app.driver.find_element_by_name('sold_out_status_id')).select_by_visible_text("-- Select --")
    app.driver.find_element_by_css_selector("input[name^=new_images]").send_keys(current_path_to_image+'\\'+picture_name) #фото товара

    app.driver.find_element_by_xpath("//a[contains(.,'Information')]").click() # перешли на вкладку информация
    app.driver.find_element_by_name("manufacturer_id").click()
    Select(app.driver.find_element_by_name('manufacturer_id')).select_by_visible_text(manufacturer)#производитель
    app.driver.find_element_by_name("short_description[en]").click()
    app.driver.find_element_by_name("short_description[en]").send_keys(short_description) #короткое описание
    app.driver.find_element_by_name("short_description[en]").click()
    app.driver.find_element_by_css_selector("div[class='trumbowyg-editor']").send_keys(description) #полное описание

    app.driver.find_element_by_xpath("//a[contains(.,'Prices')]").click()  # перешли на вкладку Prices
    app.driver.find_element_by_name("purchase_price").click()
    app.driver.find_element_by_name("purchase_price").clear()

    app.driver.find_element_by_name("purchase_price").send_keys(purchase_price)  # указали цену
    app.driver.find_element_by_name("purchase_price_currency_code").click()
    Select(app.driver.find_element_by_name('purchase_price_currency_code')).select_by_visible_text("US Dollars")  # валюта
    app.driver.find_element_by_name("save").click() #сохранили товар

    app.driver.find_element_by_xpath("// a[contains(., 'Catalog')]").click() #переходим в каталог
    newitem = len(app.driver.find_elements_by_xpath("// a[contains(., '"+itemname+"')]")) #ищем cозданный товар в каталоге






