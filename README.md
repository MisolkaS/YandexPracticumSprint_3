# Sprint_5
#в некоторых тестах есть time.sleep(), понимаю, что костыль, но по-другому firefox валится, не смотря на то, что 
#все задержки на видимость и кликабельность написаны, ругается, что какой-то слой перекрывает элемент

confest.py

    Фикстуры

    driver:
        Фикстура для создания экземпляра веб-драйвера (Chrome или Firefox) для каждого теста.
        Используется для запуска тестов в разных браузерах.

    driver_session:
        Фикстура для создания экземпляра веб-драйвера на уровне сессии (Chrome или Firefox).
        Используется для тестов, которые требуют сохранения состояния между тестами.

    menu_item:
        Фикстура, возвращающая список элементов меню (Соусы, Начинки, Булки)

    registration_url:
        Фикстура, возвращающая URL страницы регистрации

    main_url:
        Фикстура, возвращающая URL главной страницы.

    login_url:
        Фикстура, возвращающая URL страницы входа.

    forgot_password_url:
        Фикстура, возвращающая URL страницы восстановления пароля.

    profile_url:
        Фикстура, возвращающая URL страницы профиля пользователя.

    registration_data:
        Фикстура, возвращающая данные для регистрации пользователя (имя, email, пароль).


locators.py

    локаторы


wait_and_click.py

    wait_and_send_keys
        Ждет, пока элемент, указанный по Xpath, станет видимым, и отправляет ему заданные клавиши.

    wait_for_url
        Ждет, пока текущий URL страницы не станет равным указанному. 

    wait_and_click
        Ждет, пока элемент станет видимым и кликабельным, затем выполняет клик по нему. 

    wait_for_class_to_appear
        Ждет, пока указанный класс не появится у элемента, найденного по Xpath. 


generate_data.py
    
    генерация данных для тестов (имя, email, пароль)


test_navigate.py

        test_navigate_click_button_lk_on_main_page_success
            Переход по клику на «Личный кабинет».
        
        test_navigate_from_login_page_click_button_constructor_success
            Проверяет переход на главную страницу по нажатию кнопки «Конструктор» на странице входа.
        
        test_navigate_from_login_page_click_logo_success
            Проверяет переход на главную страницу по нажатию логотипа Stellar Burgers на странице входа.
        
        test_navigate_from_login_page_click_button_logout_success
            Проверяет возможность выхода из аккаунта по нажатию кнопки «Выйти» в личном кабинете.


test_auth.py

    test_login_click_button_enter_in_account_on_main_page_success
        Тестирует вход по кнопке «Войти в аккаунт» на главной странице.
    
    test_login_click_button_lk_on_main_page_success
        Тестирует вход через кнопку «Личный кабинет» на главной странице.
    
    test_login_click_link_enter_on_registration_page_success
        Тестирует вход через ссылку «Войти» на странице регистрации.
    
    test_login_click_button_lk_on_registration_page_success
        Тестирует вход через кнопку «Личный кабинет» на странице регистрации.
    
    test_login_click_link_enter_on_forgot_password_page_success
        Тестирует вход через кнопку «Личный кабинет» на странице восстановления пароля.

test_constructor.py

     test_check_menu_activation_and_scroll_success
        Тестируем меню и прокрутку
            Тест test_check_menu_activation_and_scroll_success принимает следующие параметры:
            start: Индекс начального элемента меню.
            menu_id: Индекс элемента меню для активации.
            menu_item_text: Ожидаемый текст заголовка, который должен появиться после активации элемента меню.

test_registration.py

    test_registration_success
        тестируем регистрацию нового пользователя с использованием функции случайной генерации необходимых данных
    
    test_invalid_password_error
        тестируем возникновение ошибки при вводе неправильного пароля