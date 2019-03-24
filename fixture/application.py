from selenium import webdriver


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)

    def login_admin(self, login="admin", password="admin"):
        #self.app = Application()
        self.driver.get("http://localhost/litecart/admin/")
        self.driver.find_element_by_name("username").click()
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys("%s" % login)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("%s" % password)
        self.driver.find_element_by_name("login").click()

    def destroy(self):
        self.driver.quit()

    def eshop_home(self):
        self.driver.get("http://localhost/litecart/en/")
