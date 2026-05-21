# diploma_project
# Автотесты для SSO Ростелеком (Умный дом Web)

## Что это за проект

Автотесты для проверки входа, регистрации и восстановления пароля на сайте Ростелекома (продукт «Умный дом»).

## Что проверяем

- Вход по телефону, почте и логину
- Регистрацию нового пользователя
- Восстановление пароля
- Ошибки при неверных данных

## Как запустить

### 1. Скачать проект

```bash
git clone https://github.com/твой-аккаунт/smarthome-sso-tests.git
cd smarthome-sso-tests
2. Установить зависимости
bash
pip install -r requirements.txt
3. Запустить тесты
bash
pytest tests/ -v
Где лежат тесты
Файл	Что проверяет
test_auth.py	Вход в личный кабинет
test_registration.py	Регистрацию
test_password_reset.py	Восстановление пароля
Важно
Перед запуском нужно создать тестового пользователя и прописать его данные в conftest.py:

python
test_account = {
    "phone": "+79000000000",
    "email": "test@mail.ru",
    "password": "Qwerty123"
}
Результаты
Всего тестов 20
 Pass 9
 Fail 11

Если тест упал
Смотрим ошибку в консоли. Чаще всего проблема в:

Неправильном локаторе

Долгой загрузке страницы

Отсутствии тестовых данных

Структура проекта
text
smarthome-sso-tests/
├── conftest.py          # Настройки и тестовые данные
├── requirements.txt     # Библиотеки
├── pages/               # Page Object модели
│   ├── base_page.py
│   ├── auth_page.py
│   ├── reg_page.py
│   └── reset_page.py
└── tests/               # Сами тесты
    ├── test_auth.py
    ├── test_registration.py
    └── test_password_reset.py
