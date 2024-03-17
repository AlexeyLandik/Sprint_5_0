from locators import TestLocators


class TestConstructor:

    # Тест_11. Проверка перехода к разделу булки
    def test_change_chapter_to_brad(self, driver):
        driver.find_element(*TestLocators.CHAPTER_SOUSES).click()
        driver.find_element(*TestLocators.CHAPTER_BRAD).click()
        current_chapter = driver.find_element(*TestLocators.CURRENT_CHAPTER).text

        assert current_chapter == 'Булки'

    # Тест_12. Проверка перехода к разделу соусы
    def test_change_chapter_to_souses(self, driver):
        driver.find_element(*TestLocators.CHAPTER_SOUSES).click()
        current_chapter = driver.find_element(*TestLocators.CURRENT_CHAPTER).text

        assert current_chapter == 'Соусы'

    # Тест_13. Проверка перехода к разделу начинки
    def test_change_chapter_to_fillings(self, driver):
        driver.find_element(*TestLocators.CHAPTER_FILLING).click()
        current_chapter = driver.find_element(*TestLocators.CURRENT_CHAPTER).text

        assert current_chapter == 'Начинки'
