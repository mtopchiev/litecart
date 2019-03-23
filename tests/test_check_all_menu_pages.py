from fixture.application import Application
import pytest
@pytest.fixture
def app(request):   # создаем фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def check_page(app, page_name = "TEXT"):    #метод если текст ссылки совпадает с заголовком
    app.driver.find_element_by_xpath("//span[contains(.,'%s')]" % page_name).click()
    app.driver.find_element_by_xpath("//h1[contains(.,'%s')]" % page_name)

def check_page_h1(app, page_name="TEXT", h1="text"): #метод для страниц у которых title отличается от текста ссылки
    app.driver.find_element_by_xpath("//span[contains(.,'%s')]" % page_name).click()
    app.driver.find_element_by_xpath("//h1[contains(.,'%s')]" % h1)

def check_page_url(app, page_url="TEXT", h1="text"): #дополнительный локатор url для совпадающих текстов
    app.driver.find_element_by_css_selector("a[href*='%s']" % page_url).click()
    app.driver.find_element_by_xpath("//h1[contains(.,'%s')]" % h1)


def test_check_all_menu_pages(app):  # открываем страницу и проверяем наличие правилього заголовка
    app.login_admin()
    check_page_h1(app, page_name="Appearence", h1="Template")
    check_page(app, "Logotype")
    check_page(app, "Catalog")
    check_page(app, "Product Groups")
    check_page(app, "Option Groups")
    check_page(app, "Manufacturers")
    check_page(app, "Suppliers")
    check_page(app, "Delivery")
    check_page(app, "Sold Out Statuses")
    check_page(app, "Quantity Units")
    check_page(app, "CSV Import/Export") #подменю без разделяющей строки

    check_page(app, "Countries") #следующий раздел меню

    check_page(app, "Currencies")

    check_page(app, "Customers")
    check_page(app, "CSV Import/Export")
    check_page(app, "Newsletter")

    check_page(app, "Geo Zones")

    check_page(app, "Languages")
    check_page(app, "Storage Encoding")

    check_page_h1(app, page_name="Modules", h1="Job Modules")
    check_page_url(app, page_url="http://localhost/litecart/admin/?app=modules&doc=customer", h1="Customer Modules")

    check_page_h1(app, page_name="Shipping", h1="Shipping Modules")
    check_page_h1(app, page_name="Payment", h1="Payment Modules")
    check_page_h1(app, page_name="Order Total", h1="Order Total Modules")
    check_page_h1(app, page_name="Order Success", h1="Order Success Modules")
    check_page_h1(app, page_name="Order Action", h1="Order Action Modules")

    check_page(app, "Orders")
    check_page(app, "Order Statuses")

    check_page(app, "Pages")

    check_page_h1(app, page_name="Reports", h1="Monthly Sales")
    check_page(app, "Most Sold Products")
    check_page(app, "Most Shopping Customers")

    check_page(app, "Settings")

    check_page_h1(app, page_name="Defaults", h1="Settings")
    check_page_h1(app, page_name="General", h1="Settings")
    check_page_h1(app, page_name="Listings", h1="Settings")
    check_page_h1(app, page_name="Images", h1="Settings")
    check_page_h1(app, page_name="Checkout", h1="Settings")
    check_page_h1(app, page_name="Advanced", h1="Settings")
    check_page_h1(app, page_name="Security", h1="Settings")

    check_page(app, "Slides")

    check_page_h1(app, page_name="Tax", h1="Tax Classes")
    check_page(app, "Tax Rates")

    check_page_h1(app, page_name="Translations", h1="Search Translations")
    check_page_h1(app, page_name="Scan Files", h1="Scan Files For Translations")
    check_page(app, "CSV Import/Export")
    check_page(app, "Users")

    check_page(app, "vQmods")

    app.driver.quit()



