from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_and_close(app):
    app.login_admin()
    app.driver.quit()

#запуск корпоративной версии firefox по старой схеме
# driver = webdriver.Firefox(firefox_binary="C:\Program Files\Firefox ESR 45\\firefox.exe", capabilities={"marionette": False})
# driver.get("http://localhost/litecart/admin/")
# driver.find_element_by_name("username").click()
# driver.find_element_by_name("username").clear()
# driver.find_element_by_name("username").send_keys("admin")
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("admin")
# driver.find_element_by_name("login").click()
# driver.quit()

# #запуск Chrome
# driver = webdriver.Chrome()
# driver.get("http://localhost/litecart/admin/")
# driver.find_element_by_name("username").click()
# driver.find_element_by_name("username").clear()
# driver.find_element_by_name("username").send_keys("admin")
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("admin")
# driver.find_element_by_name("login").click()
# driver.quit()

# #запуск Ie
# driver = webdriver.Ie(capabilities={"requireWindowFocus": True})
# driver.get("http://localhost/litecart/admin/")
# driver.find_element_by_name("username").click()
# driver.find_element_by_name("username").clear()
# driver.find_element_by_name("username").send_keys("admin")
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("admin")
# driver.find_element_by_name("login").click()
# driver.quit()
