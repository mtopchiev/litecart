from fixture.application import Application
import pytest
#Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара.
# Проверить все товары представленные на главной странице.
# проверить следующее:
# а) на главной странице и на странице товара совпадает текст названия товара
# б) на главной странице и на странице товара совпадают цены (обычная или две цены:до акции/акционная)


@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_check_correct_page(app):
    app.eshop_home()
    n = len(app.driver.find_elements_by_xpath("(//div[@class='image-wrapper'])"))  # узнали количество товаров на главной страницы
    price=""    #создали дефолтные значения цен главной страницы
    regular_price=""
    campaign_price=""

    real_price="" #создали дефолтные значения цен страницы товара
    real_regular_price=""
    real_campaign_price=""

    for i in range(1, n):  # цикл проверяющий каждый товар на странице
        app.eshop_home() # открываем главную страницу
        cards = app.driver.find_elements_by_css_selector("a.link") # выделили элементы содержащие все карточки товара
        del cards[0] #удалили элемент не являющийся товаром

        card=cards[i-1]
        item_name = card.find_element_by_css_selector("div.name").text #сохраняем название с главной страницы

        try:
            price = card.find_element_by_css_selector("span.price").text #сохраняем обычную цену с главной страницы, если она есть
        except Exception:
            pass
        try:
            regular_price = card.find_element_by_css_selector("s.regular-price").text #сохраняем цену до акции с главной страницы, если она есть
        except Exception:
            pass
        try:
            campaign_price = card.find_element_by_css_selector("strong.campaign-price").text #сохраняем акционную цену с главной страницы, если она есть
        except Exception:
            pass

        app.driver.find_element_by_xpath("(//div[contains(@class,'name')])["+str(i)+"]").click() #перешли на карточку товара
        box_product=app.driver.find_element_by_xpath("//div[@id='box-product']")

        real_item_name = box_product.find_element_by_css_selector("h1.title").text #сохранили имя на странице
        try:
            real_price = box_product.find_element_by_css_selector("span.price").text # сохранили обычную цену на странице, если она есть
        except Exception:
            pass
        try:
            real_regular_price = box_product.find_element_by_css_selector("s.regular-price").text  # сохранили цену до акции на странице
        except Exception:
            pass
        try:
            real_campaign_price = box_product.find_element_by_css_selector("strong.campaign-price").text  # сохранили акционную цену на странице
        except Exception:
            pass
        #сравнваем данные с главной страницы с данными на листинге товара
        assert real_item_name == item_name
        assert real_price == price
        assert real_regular_price == regular_price
        assert real_campaign_price == campaign_price
        #сбрасываем переменные в конце цикла
        item_name = ""
        price = ""
        regular_price = ""
        campaign_price = ""
        real_price = ""
        real_regular_price = ""
        real_campaign_price = ""
