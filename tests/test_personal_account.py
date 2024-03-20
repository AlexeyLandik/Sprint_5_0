from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import Config


class TestPersonalAccount:

    # Тест_7. Проверка перехода в Личный Кабинет
    def test_click_button_personal_office(self, driver):
        driver.find_element(*TestLocators.BUTTON_PRIVATE_OFFICE).click()
        login_url = driver.current_url

        assert login_url == Config.LOGIN_PAGE_STELLAR_BURGERS, 'Переход не выполнен'

    # # Тест_8. Проверка клика по Конструктору
    def test_click_button_constructor(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).send_keys(Config.EMAIL)
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys(Config.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        driver.find_element(*TestLocators.BUTTON_CONSTRUKTOR).click()
        home_page_url = driver.current_url

        assert home_page_url == Config.MAIN_PAGE_STELLAR_BURGERS, 'Переход не выполнен'

    # Тест_9. Проверка клика по Stellar Burger
    def test_click_button_stellar_burgers(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).send_keys(Config.EMAIL)
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys(Config.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        driver.find_element(*TestLocators.BUTTON_STELLAR_BURGERS).click()
        home_page_url = driver.current_url

        assert home_page_url == Config.MAIN_PAGE_STELLAR_BURGERS, 'Переход не выполнен'

    # Тест_10. Проверка выхода по кнопке Выйти в личном кабинете
    def test_exit_by_button_in_personal_office(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).send_keys(Config.EMAIL)
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys(Config.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        driver.find_element(*TestLocators.BUTTON_PRIVATE_OFFICE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT_IN_PROFILE))
        driver.find_element(*TestLocators.BUTTON_EXIT_IN_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_LOGIN))
        login_page = driver.current_url

        assert login_page == Config.LOGIN_PAGE_STELLAR_BURGERS, 'Выход из аккаунта не выполнен'
