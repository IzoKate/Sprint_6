from selenium.webdriver.common.by import By
from page_object.base_page import BasePage



class HomePageLocators:
    #Локаторы выпадащего списка в разделе «Вопросы о важном»
    QUESTION1 = (By.XPATH, "//div[@id='accordion__heading-0']")
    QUESTION2 = (By.XPATH, "//div[@id='accordion__heading-1']")
    QUESTION3 = (By.XPATH, "//div[@id='accordion__heading-2']")
    QUESTION4 = (By.XPATH, "//div[@id='accordion__heading-3']")
    QUESTION5 = (By.XPATH, "//div[@id='accordion__heading-4']")
    QUESTION6 = (By.XPATH, "//div[@id='accordion__heading-5']")
    QUESTION7 = (By.XPATH, "//div[@id='accordion__heading-6']")
    QUESTION8 = (By.XPATH, "//div[@id='accordion__heading-7']")
    QUESTION_TEXT = (By.XPATH, "//div[@aria-disabled='true']/parent::div/following-sibling::div/p")




class HomePage(BasePage):
    # Кликаем на вопросе выпадающего списка
    def click_accordion_question(self, question_num):
        self.find_element_located(question_num, time=5).click()

    #Получаем текст ответа на вопрос который кликнули
    def get_accordion_answer(self):
        question = self.find_element_located(HomePageLocators.QUESTION_TEXT)
        return question.text


