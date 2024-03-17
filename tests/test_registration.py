import random
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    #
    # Тест_1. Успешная регистрация с корректными данными
    def test_registration_successfully(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys("Alexey")
        (driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).
         send_keys(f'alexeylandik{random.randint(100, 999)}@yandex.ru'))
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('1234AF')
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN)), 'Регистрация не выполнена'

    # Тест_2. Проверка ввода невалидного пароля
    def test_registration_not_correct_password(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys("Alexey")
        (driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).
         send_keys(f'alexeylandik{random.randint(100, 999)}@yandex.ru'))
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('1234')
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.TEXT_ERROR_PASSWORD)), ('Валидность пароля '
                                                                                                   'не проверена')
