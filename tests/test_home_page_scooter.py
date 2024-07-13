import allure
import pytest
from constants import Constants
from page_object.home_page_scooter import HomePage
from page_object.home_page_scooter import HomePageLocators


@allure.epic('Проверяем раздел вопросов')
class TestHomePageScooter:

    @pytest.mark.parametrize('q_num, q_answer',
                             [
                                 [Constants.ANSWER_Q1, HomePageLocators.QUESTION1],
                                 [Constants.ANSWER_Q2, HomePageLocators.QUESTION2],
                                 [Constants.ANSWER_Q3, HomePageLocators.QUESTION3],
                                 [Constants.ANSWER_Q4, HomePageLocators.QUESTION4],
                                 [Constants.ANSWER_Q5, HomePageLocators.QUESTION5],
                                 [Constants.ANSWER_Q6, HomePageLocators.QUESTION6],
                                 [Constants.ANSWER_Q7, HomePageLocators.QUESTION7],
                                 [Constants.ANSWER_Q8, HomePageLocators.QUESTION8]
                             ])
    @allure.feature('Кликаем следующий вопрос и проверяем текст ответа')
    def test_click_accordion_question_get_answer(self, driver, q_num, q_answer):
        question = HomePage(driver)
        question.go_to_site_scooter(Constants.HOME_PAGE_URL)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        question.click_accordion_question(q_answer)
        answer = question.get_accordion_answer()
        assert answer == q_num

