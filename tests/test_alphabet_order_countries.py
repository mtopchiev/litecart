from fixture.application import Application
import pytest

# Сделайте сценарии, которые проверяют сортировку стран и геозон (штатов) в учебном приложении litecart.
# а) проверить, что страны расположены в алфавитном порядке
# б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить, что зоны расположены в алфавитном порядке


@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_alphabet_order_countries(app): #проверяем, что страны расположены в алфавитном порядке
    app.login_admin()
    app.driver.get("http://localhost/litecart/admin/?app=countries&doc=countries") # открыли список стран
    len_country_list=len(app.driver.find_elements_by_css_selector("table td:nth-of-type(5) a")) #определили длину списка

    list_countries = [] # создали список будущий стран
    for i in range(1, int(len_country_list+2)):
        country_name = app.driver.find_element_by_css_selector("table tr:nth-of-type("+str(i)+") td:nth-of-type(5) a").text
        list_countries.append(country_name)     # создаем список стран в порядке как на сайте
    list_countries_sort = sorted(list_countries) # сортируем полученный список, как правильно
    assert list_countries_sort == list_countries #сравниваем списки

    print(list_countries)
    print(type(list_countries))

    #print(country[1])

    # таблица: .dataTable
    # < table class="dataTable">
    #
    # .row
    # <tr class="row">
    #
    # element.getAttribute("innerText")
    #
    # "table td:nth-of-type(5)" в таблице элементы в текстом страны
    #
    #










