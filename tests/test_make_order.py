import allure
from constants import Constants
from page_object.order_page import OrderPage


@allure.epic('Проверка оформления заказа')
class TestOrderPage:
   @allure.feature('Проверяем что при успешном оформлении заказа появляется окно об успешном создании заказа. Переход по кнопке из шапки страницы')

   def test_go_from_top_button_make_order_get_pop_up_win_order_success(self, driver):
       make_order = OrderPage(driver)
       make_order.go_to_site_scooter(Constants.HOME_PAGE_URL)
       #Переходим на форму заказа по кнопке Заказать из шапки
       make_order.click_button_order_top_of_page()
       #Заполняем форму заказа
       make_order.set_form1_order(Constants.NAME1, Constants.SURNAME1, Constants.ADDRESS1, Constants.TELEPHONE1)
       make_order.set_form2_order(Constants.COMMENT1)
       #Подтверждаем создание заказа
       make_order.confirm_order()
       #Проверяем открытие окна созданного заказа
       assert make_order.pop_up_processed_win() == True
       #Закрываем окно созданного заказа
       make_order.pop_up_processed_win_button_click()
       #Нажимаем на логотип самоката
       make_order.click_logo_scooter()
       url = driver.current_url
       #Проверяем произошел ли переход на домашнюю страницу
       assert url == Constants.HOME_PAGE_URL

   @allure.feature('Проверяем что при успешном оформлении заказа появляется окно об успешном создании заказа. Переход по кнопке из середины страницы')
   def test_go_from_button_bottom_make_order_get_pop_up_win_order_success(self, driver):
       make_order = OrderPage(driver)
       make_order.go_to_site_scooter(Constants.HOME_PAGE_URL)
       #Переходим на форму заказа по кнопке Заказать с середины страницы
       #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
       make_order.click_button_order_bottom_of_page(driver)
       # Заполняем форму заказа
       make_order.set_form1_order(Constants.NAME1, Constants.SURNAME1, Constants.ADDRESS1, Constants.TELEPHONE1)
       make_order.set_form2_order(Constants.COMMENT1)
       # Подтверждаем создание заказа
       make_order.confirm_order()
       # Проверяем открытие окна созданного заказа
       assert make_order.pop_up_processed_win() == True
       # Закрываем окно созданного заказа
       make_order.pop_up_processed_win_button_click()
       # Нажимаем на логотип яндекса
       make_order.click_logo_ya()
       window_after = driver.window_handles[1]
       driver.switch_to.window(window_after)
       make_order.wait_page()
       url = driver.current_url
       # Проверяем произошел ли переход на страницу Дзен
       assert url == Constants.DZEN_REDIRECT_URL


