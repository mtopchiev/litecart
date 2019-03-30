from fixture.application import Application
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 1) зайти в админку
# 2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
# 3) открыть на редактирование какую-нибудь страну или начать создание новой
# 4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой --
# они ведут на внешние страницы и открываются в новом окне, именно это и нужно проверить.
# требуется именно кликнуть по ссылке, чтобы она открылась в новом окне, потом переключиться в новое окно, закрыть его,
# вернуться обратно, и повторить эти действия для всех таких ссылок.
# Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна.

@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_external_links(app):
    app.login_admin()
    app.driver.get("http://localhost/litecart/admin/?app=countries&doc=countries") # открыли список стран
    app.driver.find_element_by_xpath("//a[@class ='button'][contains(.,'Add New Country')]").click() #открыли страницу с ссылками
    wait = WebDriverWait(app.driver, 10)
    main_window = app.driver.current_window_handle #сохранили id текущего окна
    old_windows = app.driver.window_handles
    links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'i.fa.fa-external-link')))
    for i in range(0, len(links)): #открываем по очереди ссылки
        str_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'i.fa.fa-external-link')))
        str_links[i].click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_windows = app.driver.window_handles
        result = list(set(new_windows) - set(old_windows))
        new_window = result[0] # id нового открытого окна
        app.driver.switch_to.window(new_window)
        app.driver.close() # закрыли новое окно
        app.driver.switch_to.window(main_window)
