from locators import TestLocators
from config import Config


class TestConstructor:

    # Тест_11. Проверка перехода к разделу булки
    def test_change_chapter_to_brad(self, driver):
        driver.find_element(*TestLocators.CHAPTER_SOUSES).click()
        driver.find_element(*TestLocators.CHAPTER_BRAD).click()
        current_chapter = driver.find_element(*TestLocators.CURRENT_CHAPTER).get_attribute('class')

        assert Config.CURRENT_CHAPTER_CLASS in current_chapter

    # Тест_12. Проверка перехода к разделу соусы
    def test_change_chapter_to_souses(self, driver):
        driver.find_element(*TestLocators.CHAPTER_SOUSES).click()
        current_chapter = driver.find_element(*TestLocators.CURRENT_CHAPTER).get_attribute('class')

        assert Config.CURRENT_CHAPTER_CLASS in current_chapter

    # Тест_13. Проверка перехода к разделу начинки
    def test_change_chapter_to_fillings(self, driver):
        driver.find_element(*TestLocators.CHAPTER_FILLING).click()
        current_chapter = driver.find_element(*TestLocators.CURRENT_CHAPTER).get_attribute('class')

        assert Config.CURRENT_CHAPTER_CLASS in current_chapter
