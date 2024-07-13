from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_object.base_page import BasePage


class OrderPageLocators():
    #Локаторы кнопок с которых переходим на форму
    BUTTON_ORDER_TOP = (By.XPATH,"//div[contains(@class, 'Header')]/button[text()='Заказать']")
    BUTTON_ORDER_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home')]/button[text()='Заказать']")

    BUTTON_CLOSE_COOKIE_WIN = (By.XPATH, "//button[contains(text(),'да все привыкли')]")

    #Локаторы на форме 1 оформления заказа
    INPUT_NAME = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    INPUT_SURNAME = (By.XPATH,"//input[contains(@placeholder, 'Фамилия')]")
    INPUT_ADDRESS = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    INPUT_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_STATION_VALUE = (By.XPATH, "//div[contains(text(), 'Черкизовская')]") #//li[@class='select-search__row']
    INPUT_TELEPHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    BUTTON_NEXT_FORM1 = (By.XPATH, "//button[contains(text(), 'Далее')]")
    #Локаторы на форме 2 оформления заказа
    DELIVERY_DATE = (By.XPATH, "//div[@class='react-datepicker__input-container']/input")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    RENTAL_PERIOD_VALUE = (By.XPATH, "//div[contains(text(), 'сутки')]")
    COLOR_SCOOTER = (By.XPATH, "//label[@for='black']")
    COMMENT = (By.XPATH,"//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER_FORM = (By.XPATH,"//div[contains(@class, 'Order')]/button[text()='Заказать']")

    #Локаторы всплывающего окна с сообщением об успешном создании заказа
    POP_UP_CONFIRM_WINDOW = (By.XPATH,"//div[text()='Хотите оформить заказ?']")
    BUTTON_YES_POP_UP_WINDOW = (By.XPATH, "//button[contains(text(),'Да')]")
    POP_UP_ORDER_PROCESSED = (By.XPATH, "//div[text()='Заказ оформлен']")
    BUTTON_YES_ORDER_PROCESSED = (By.XPATH,"//button[contains(text(),'Посмотреть статус')]")

    #Локаторы логотипов
    LOGO_SCOOTER = (By.XPATH,"//img[@alt='Scooter']")
    LOGO_YA =(By.XPATH,"//img[@alt='Yandex']")



class OrderPage(BasePage):
    #Переход на форму заказа с главной страницы
    #Кнопка заказать вверху страницы
    def click_button_order_top_of_page(self):
        self.find_element_located(OrderPageLocators.BUTTON_ORDER_TOP, time=3).click()

    # Кнопка заказать в середине страницы
    def click_button_order_bottom_of_page(self, driver):
        element = driver.find_element(By.XPATH, "//div[contains(text(), 'Курьер забирает самокат')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element_located(OrderPageLocators.BUTTON_ORDER_BOTTOM, time=4).click()

    #Кнопка закрытия куки
    def click_button_cookie(self):
        self.find_element_located(OrderPageLocators.BUTTON_CLOSE_COOKIE_WIN, time=4).click()

    # Форма 1 оформления заявки
    def set_name(self, name):
        self.find_element_located(OrderPageLocators.INPUT_NAME, time=3).send_keys(name)

    def set_surname(self, surname):
        self.find_element_located(OrderPageLocators.INPUT_SURNAME, time=3).send_keys(surname)

    def set_address(self, address):
        self.find_element_located(OrderPageLocators.INPUT_ADDRESS, time=3).send_keys(address)

    def set_station(self):
        self.find_element_located(OrderPageLocators.INPUT_STATION, time=3).click()
        self.find_element_located(OrderPageLocators.INPUT_STATION_VALUE, time=5).click()

    def set_telephone(self, telephone):
        self.find_element_located(OrderPageLocators.INPUT_TELEPHONE, time=3).send_keys(telephone)

    def click_button_next_form1(self):
        self.find_element_located(OrderPageLocators.BUTTON_NEXT_FORM1, time=5).click()

    # Форма 2 оформления заявки
    def set_delivery_date(self, today=None):
        today = date.today()
        current_date = f'{today.day}.{'{0:0>2}'.format(today.month)}.{today.year}'
        self.find_element_located(OrderPageLocators.DELIVERY_DATE, time=3).click()
        self.find_element_located(OrderPageLocators.DELIVERY_DATE, time=3).send_keys(Keys.ENTER)


    def set_rental_period(self):
        self.find_element_located(OrderPageLocators.RENTAL_PERIOD, time=3).click()
        self.find_element_located(OrderPageLocators.RENTAL_PERIOD_VALUE, time=3).click()

    def set_color_scooter(self):
        self.find_element_located(OrderPageLocators.COLOR_SCOOTER, time=3).click()

    def set_order_comment(self, comment):
        self.find_element_located(OrderPageLocators.COMMENT, time=3).send_keys(comment)

    def click_button_order_form2(self):
        self.find_element_located(OrderPageLocators.BUTTON_ORDER_FORM, time=3).click()

    #Всплывающее окно подтверждения заказа
    def pop_up_confirm_win(self):
        self.find_element_located(OrderPageLocators.POP_UP_CONFIRM_WINDOW, time=5)

    def pop_up_confirm_win_button_click(self):
        self.find_element_located(OrderPageLocators.BUTTON_YES_POP_UP_WINDOW, time=3).click()

    def pop_up_processed_win(self):
        self.find_element_located(OrderPageLocators.POP_UP_ORDER_PROCESSED, time=5)
        return True

    def pop_up_processed_win_button_click(self):
        self.find_element_located(OrderPageLocators.BUTTON_YES_ORDER_PROCESSED, time=3).click()



    # Нажимаем на логотип Самоката
    def click_logo_scooter(self):
        self.find_element_located(OrderPageLocators.LOGO_SCOOTER, time=5).click()


    # Нажимаем на логотип Яндекса
    def click_logo_ya(self):
        self.find_element_located(OrderPageLocators.LOGO_YA, time=5).click()


    #Шаг заполнения 1й страницы формы
    def set_form1_order(self, name, surname, address, telephone ):
        self.click_button_cookie()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station()
        self.set_telephone(telephone)
        self.click_button_next_form1()


    #Шаг заполнения 2й страницы формы
    def set_form2_order(self, comment):
        self.set_delivery_date()
        self.set_rental_period()
        self.set_color_scooter()
        self.set_order_comment(comment)
        self.click_button_order_form2()

    #Подтвердить оформление заказа на окне подтверждения оформления
    def confirm_order(self):
        self.pop_up_confirm_win()
        self.pop_up_confirm_win_button_click()

    # Подтвердить оформление заказа на окне подтверждения оформления
    def processed_order(self):
        self.pop_up_processed_win()
        self.pop_up_processed_win_button_click()



