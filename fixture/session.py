#методы для работы с сессией
class SessionHelper:


    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("login").submit()


    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_loggen_in():
            self.logout()

    def is_loggen_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_loggen_in_as(self, username):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div/div[1]/form/b").text =="("+username+")"

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_loggen_in():
            if self.is_loggen_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def get_logged_user(self):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div/[1]/form/b").text[1:-1]



