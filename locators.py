# locators.py
#главная страница
xpath_enter_in_account_button = "//button[text()='Войти в аккаунт']" # Кнопка «Войти в аккаунт»
xpath_of_order_button = "//section[2]//button"
xpath_of_personal_page = ".//p[text()='Личный Кабинет']"
xpath_of_menu = "//section[1]/div/div"
xpath_of_h2 = "//h2"

#страница логина

xpath_email_login_input = "//fieldset[1]//input"  # Поле для ввода электронной почты
xpath_password_login_input = "//fieldset[2]//input"  # Поле для ввода пароля
xpath_login_button = "//button[text()='Войти']"
xpath_constructor_button = "//p[text()='Конструктор']"
xpath_logo_button = "//div/header/nav/div/a"  # логотип
xpath_login_logout_button = "//button[text()='Выход']"
xpath_password_error ="//div[contains(@class, 'input_type_password') and contains(@class, 'input_status_error')]"


#страница регистрации

xpath_name_input = "//fieldset[1]//input" # Поле для ввода имени
xpath_email_input = "//fieldset[2]//input"  # Поле для ввода электронной почты
xpath_password_input = "//fieldset[3]//input"  # Поле для ввода пароля
xpath_link_enter = "//a[text()='Войти']"
xpath_register_button = "//button[text()='Зарегистрироваться']"  # "//div//button" Кнопка для регистрации


