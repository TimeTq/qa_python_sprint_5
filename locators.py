MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
LOGIN_URL = 'https://stellarburgers.nomoreparties.site/login'
REGISTRATION_URL = 'https://stellarburgers.nomoreparties.site/register'
RECOVERY_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
ACCOUNT_URL = 'https://stellarburgers.nomoreparties.site/account/profile'


class MainPageLocators:
    LOGIN_BTN = ".//button[text()='Войти в аккаунт']"  # Кнопка входа на главной странице
    ACCOUNT_A = ".//p[text()='Личный Кабинет']/.."  # Кнопка "Личный кабинет" на главной странице

    BUN_DIV = ".//span[text()='Булки']/.."  # Кнопка "Булки" на главной странице
    SAUCE_DIV = ".//span[text()='Соусы']/.."  # Кнопка "Соусы" на главной странице
    FILLING_DIV = ".//span[text()='Начинки']/.."  # Кнопка "Начинки" на главной странице

    BUN_H2 = ".//h2[text()='Булки']"  # Подпись раздела "Булки" на главной странице
    SAUCE_H2 = ".//h2[text()='Соусы']"  # Подпись раздела "Соусы" на главной странице
    FILLING_H2 = ".//h2[text()='Начинки']"  # Подпись раздела "Начинки" на главной странице


class LogInPageLocators:
    EMAIL_INPUT = "//label[text()='Email']/..//input"  # Ввод имени
    PASSWORD_INPUT = "//label[text()='Пароль']/..//input"  # Ввод пароля
    ENTER_BTN = ".//button[text()='Войти']"  # Кнопка входа на странице ввода данных аккаунта


class RegisterPageLocators:
    ENTER_CREDENTIALS_FORM = ".//form"  # Форма регистрации

    REGISTRATION_BTN = ".//button[text()='Зарегистрироваться']"  # Кнопка регистрации

    NAME_INPUT = "//label[text()='Имя']/..//input"  # Ввод имени
    EMAIL_INPUT = "//label[text()='Email']/..//input"  # Ввод имени
    PASSWORD_INPUT = "//label[text()='Пароль']/..//input"  # Ввод пароля

    ERROR_PASSWORD_P = ".//p[text()='Некорректный пароль']"  # Отображение информации о неверном пароле

    LOGIN_A = ".//a[@href='/login']"


class RecoveryPasswordPageLocators:
    LOGIN_A = ".//a[@href='/login']"  # Кнопка входа на странице восстановления пароля


class AccountPageLocators:
    USER_NAME_INPUT = ".//label[text()='Имя']/../input"  # Поле со значением имени пользователя на странице профиля
    USER_LOGIN_INPUT = ".//label[text()='Логин']/../input"  # Поле со логином пользователя на странице профиля

    LOGOUT_BTN = ".//button[text()='Выход']"  # Кнопка выхода из аккаунта на странице профиля

    CONSTRUCTOR_A = ".//p[text()='Конструктор']/.."  # Кнопка «Конструктор» на странице профиля
    MAIN_LOGO_A = ".//div[@class='AppHeader_header__logo__2D0X2']/a"  # Логотип Stellar Burgers на странице профиля

