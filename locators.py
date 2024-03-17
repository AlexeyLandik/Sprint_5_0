from selenium.webdriver.common.by import By


class TestLocators:
    BUTTON_ENTER_ACCOUNT = By.XPATH, ".//*[contains(@class, 'button_button_size_large')]"   # кнопка "Войти в аккаунт"
    LINK_REGISTRATION = By.XPATH, ".//*[contains(text(), 'Зарегистрироваться')]"    # ссылка "Зарегистрироваться"
    FIELD_REGISTRATION_NAME = By.XPATH, ".//label[text()='Имя']/parent::div/input"  # поле "Имя"
    FIELD_REGISTRATION_EMAIL = By.XPATH, ".//label[text()='Email']/parent::div/input"   # поле "Email@
    FIELD_REGISTRATION_PASSWORD = By.XPATH, ".//label[text()='Пароль']/parent::div/input"   # поле "Пароль"
    BUTTON_REGISTRATION = By.XPATH, ".//button[contains(@class, 'button_button_size_medium')]"  # кнопка
    # "Зарегистрироваться"
    BUTTON_LOGIN = By.XPATH, ".//button[text()='Войти']"    # кнопка "Войти"
    TEXT_ERROR_PASSWORD = By.XPATH, ".//*[text()='Некорректный пароль']"    # сообщение "Некорректный пароль"
    BUTTON_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"   # кнопка "Оформить заказ"
    BUTTON_PRIVATE_OFFICE = By.XPATH, ".//*[text()='Личный Кабинет']"   # кнопка "Личный Кабинет"
    LINK_ENTER_IN_REGISTRATION_FORM = By.XPATH, ".//*[text()='Войти']"  # ссылка "Войти" в форме регистрации
    LINK_FORGOT_PASSWORD = By.XPATH, ".//*[text()='Восстановить пароль']"   # ссылка "Восстановить пароль"
    LINK_LOGIN = By.XPATH, ".//*[text()='Войти']"   # ссылка "Войти" в форме восстановления пароля
    BUTTON_CONSTRUKTOR = By.XPATH, ".//*[text()='Конструктор']"  # кнопка "Конструктор"
    BUTTON_STELLAR_BURGERS = By.XPATH, ".//*[@class='AppHeader_header__logo__2D0X2']"   # логотип Stellar Burgers
    BUTTON_EXIT_IN_PROFILE = By.XPATH, ".//*[text()='Выход']"   # кнопка Выйти в личном кабинете
    CHAPTER_BRAD = By.XPATH, ".//*[text()='Булки']/parent::div[contains(@class,'tab_tab__1SPyG')]"  # вкладка Булки
    CHAPTER_SOUSES = By.XPATH, ".//*[text()='Соусы']/parent::div[contains(@class,'tab_tab__1SPyG')]"  # вкладка Соусы
    CHAPTER_FILLING = By.XPATH, ".//*[text()='Начинки']/parent::div[contains(@class,'tab_tab__1SPyG')]"  # вкладка
    # Начинки
    CURRENT_CHAPTER = By.XPATH, ".//div[contains(@class,'current')]/span"    # название текущей вкладки в Конструкторе
