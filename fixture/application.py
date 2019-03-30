from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

    def eshop_checkout(self):
        self.driver.get("http://localhost/litecart/en/checkout")
######

    def remove_all_items_from_cart(self):
        products = self.driver.find_elements_by_css_selector('td.item')  # список товаров в корзине
        block = self.driver.find_element_by_css_selector(
            'div#checkout-cart-wrapper')  # выделили блок содержащий кнопку remove
        wait = WebDriverWait(self.driver, 10)
        for i in range(len(products)):
            remove = self.driver.find_elements_by_css_selector('button[value = Remove]')  # выделили кнопку remove
            for j in remove:
                wait.until(EC.visibility_of(block.find_element_by_css_selector(
                    'form[name=cart_form]')))  # ждем обработку удаления и видимость оставшихся товаров
                wait.until(EC.visibility_of(j)).click()  # жмем кнопку удалить
                wait.until(EC.staleness_of(products[0]))  # ждем обновление первого товара в списке корзины
                break
            continue
        wait.until(EC.staleness_of(self.driver.find_element_by_css_selector('div#box-checkout-summary')))
        # проверяем что в корзине не осталось ни одного sku
        assert len(self.driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody//td[3]")) == 0


    def open_first_item_page(self):
        self.driver.find_element_by_xpath(
            "(//li[@class='product column shadow hover-light'])[1]").click()


    def add1_item_to_cart(self):
        qnt = self.driver.find_element_by_css_selector("span.quantity")  # сохранили количество товаров в корзине
        intqnt = int(qnt.text)
        nextQntStr = str(intqnt + 1)  # требуемое количество товаров в корзине после добавления 1 товара
        self.driver.find_element_by_name("add_cart_product").click()  # нажимаем кнопку добавить в корзину
        # указание ожидания до завершения анимации добавления в корзину. ждем обновления числа в счетчике корзины
        wait = WebDriverWait(self.driver, 10)  # seconds
        qnt2 = By.CSS_SELECTOR, 'span.quantity'
        # wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'span.quantity'),nextQntStr)) #строка ниже равнозначна этой
        wait.until(EC.text_to_be_present_in_element((qnt2), nextQntStr))