from fixture.application import Application
import pytest

#Сделайте сценарий, проверяющий наличие стикеров у всех товаров в учебном приложении litecart на главной странице.
# Стикеры -- это полоски в левом верхнем углу изображения товара, на которых написано New или Sale или что-нибудь другое.
# Сценарий должен проверять, что у каждого товара имеется ровно один стикер.


@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_check_stickers_on_img(app):
    app.eshop_home()
    n = len(app.driver.find_elements_by_xpath("(//div[@class='image-wrapper'])")) #узнали количество товара на главной страницы

    for i in range(1, n): # цикл проверяющий каждый товар на странице

        stickers = app.driver.find_elements_by_xpath("(//div[@class='image-wrapper'])["+str(i)+"]//div[contains(@class,'sticker')]") #ищем все элементы стикеры i-ного товара

        Q = len(stickers) == 1  #подсчитываем количество найденных стикеров у i-ного товара и сравниваем с требованием 1 стикер на товар
        print(Q)

        assert Q == True # проверка. Если у товаров по одному стикеру, тест пройден, иначе тест падает.

    app.driver.quit()

