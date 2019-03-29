from fixture.application import Application
import pytest
import random
from selenium.webdriver.support.ui import Select

# разработать тест регистрации нового пользователя в магазине
#1) регистрация нового пользователя
#2) логаут после регистрации
#3) авторизация созданным пользователем
#4) логаут

@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_signup_customer(app):
    driver = app.driver
    driver.get("http://localhost/litecart")
    driver.find_element_by_css_selector('form[name=login_form] a').click()
    FirstName = GenUserName()
    driver.find_element_by_css_selector('input[name=firstname]').send_keys("Name" + str(FirstName))
    LastName = GenUserName()
    driver.find_element_by_css_selector('input[name=lastname]').send_keys("Last" + str(LastName))
    driver.find_element_by_css_selector('input[name=address1]').send_keys('2148  Haul Road')
    driver.find_element_by_css_selector('input[name=postcode]').send_keys('11650')
    driver.find_element_by_css_selector('input[name=city]').send_keys('Minneapolis')
    Select(driver.find_element_by_css_selector('select[name=country_code]')).select_by_value('US')
    Email = GenMail()
    driver.find_element_by_css_selector('input[name=email]').send_keys(Email)
    driver.find_element_by_css_selector('input[name=phone]').send_keys('651-261-7923')
    driver.find_element_by_css_selector('input[name=password]').send_keys('password')
    driver.find_element_by_css_selector('input[name=confirmed_password]').send_keys('password')
    driver.find_element_by_css_selector('button[name=create_account]').click()

# Выход из аккаунта
    driver.find_element_by_link_text("Logout").click()

# Вход в аккаунт по зарегистрированным данным
    driver.find_element_by_css_selector('input[name=email]').send_keys(Email)
    driver.find_element_by_css_selector('input[name=password]').send_keys('password')
    driver.find_element_by_css_selector('button[name=login]').click()

# Окончательный выход из аккаунта
    driver.find_element_by_link_text("Logout").click()

# генерим уникальный e-mail
def GenMail():
    array = [chr(i) for i in range(65, 91)]
    random.shuffle(array)
    key = ""
    for i in range(7):
        key += array.pop()
    mail = key.lower() + '@gmail.com'
    return mail

# генерим набор букв
def GenUserName():
    array = [chr(i) for i in range(65, 91)]
    random.shuffle(array)
    key = ""
    for i in range(7):
        key += array.pop()
    user_name = key.title()
    return user_name
