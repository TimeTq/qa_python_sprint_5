# Описание тестов

### [Раздел «Конструктор»](tests/test_constructor.py)
* `test_click_on_constructor_x_path_class_added_to_element` - 
проверка того, что при клике на конструктор к нему добавляется класс, подсвечивающий кнопку

### [Вход](tests/test_login.py)
* `test_user_enter_from_pages_user_cred_main_page` -
проверка входа в аккаунт уже зарегистрированным пользователем

### [Выход из аккаунта](tests/test_logout.py)
* `test_user_exit_from_account_page_login_account_login_page`
проверка выхода из аккаунта уже зарегистрированного пользователя

### [Переход в личный кабинет](tests/test_personal_account.py)
* `test_user_exit_from_account_page_login_account_login_page` -
проверка перехода в личный кабинет из основной страницы

### [Переход из личного кабинета в конструктор ](tests/test_personal_account_to_constructor.py)
* `test_user_click_button_account_page_login_account_main_page` -
проверка перехода из личного кабинета в конструктор на главной странице

### [Регистрация](tests/test_registration.py)
* `test_user_registration_allowed_credentials_success_registration` -
проверка регистрации нового пользователя

* `test_user_registration_short_password_bad_password_warning` -
проверка регистрации с "коротким" паролем