from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    # Тест_3. Проверка входа по кнопке "Войти в аккаунт"
    def test_login_by_button_enter_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).send_keys('landik_654@yandex.ru')
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('123456')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)), 'Вход не выполнен'

    # Тест_4. Проверка входа по кнопке Личный Кабинет
    def test_login_by_button_private_office(self, driver):
        driver.find_element(*TestLocators.BUTTON_PRIVATE_OFFICE).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).send_keys('landik_654@yandex.ru')
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('123456')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)), 'Вход не выполнен'

    # Тест_5. Проверка входа через форму регистрации
    def test_login_by_button_in_registration_form(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.LINK_ENTER_IN_REGISTRATION_FORM).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).send_keys('landik_654@yandex.ru')
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('123456')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)), 'Вход не выполнен'

    # Тест_6. Проверка входа через форму Восстановления пароля
    def test_login_by_link_forgot_password(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_FORGOT_PASSWORD).click()
        driver.find_element(*TestLocators.LINK_LOGIN).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).send_keys('landik_654@yandex.ru')
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('123456')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)), 'Вход не выполнен'

