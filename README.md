# user_request_app


## Что делает проект

Проект отправляет запросы на другое приложения (чтобы клонировать приложение user_response_app
)

```Bash 
git clone https://github.com/aidarhaertdinov/user_response_app.git
```
Реализована базовая и токеновая аутентификация.

## Как собрать и запустить проект

### Для Windows:

1. Клонировать проект выполнив команду
```Bash 
git clone https://github.com/aidarhaertdinov/user_request_app.git
```
2. Создать виртуальное окружение выполнив команду 
```Bash
python -m venv venv
``` 
3. Активировать виртуальное окружение выполнив команду
```Bash
venv\Scripts\activate
```  
4. Установить пакеты выполнив команду 
```Bash
pip freeze > requirements.txt
```
5. Установить миграцию выполнив команду 
```Bash
pip install flask-migrate
``` 
6. Создать репозиторий миграции выполнив команду 
```Bash
flask db init
``` 

## Используемые Конфигураций (Config)

```Python
PROTOCOL_REST_BACKEND = os.getenv('PROTOCOL_REST_BACKEND') or 'http://'
```
- протокол приложения

```Python
URL_REST_BACKEND = os.getenv('URL_REST_BACKEND') or '127.0.0.1'
```
- адрес приложения

```Python
PORT_REST_BACKEND = os.getenv('PORT_REST_BACKEND') or '5000'
```
- порт приложения

```Python
SECRET_KEY = os.urandom(32)
```
- используют значение секретного ключа в качестве криптографического ключа, полезного для генерации подписей или токенов. [ссылка на документацию](https://explore-flask.readthedocs.io/en/latest/configuration.html)

```Python
WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY') or os.urandom(32)
```
- для защиты веб-форм от атаки под названием Cross-Site Request Forgery. [ссылка на документацию](https://flask-wtf.readthedocs.io/en/0.15.x/config/)

```Python
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or False
```
- если установлен  `True`, то Flask-SQLAlchemy будет отслеживать изменения объектов и посылать сигналы. [ссылка на документацию](https://flask-sqlalchemy-russian.readthedocs.io/ru/latest/config.html)

```Python
ADMIN_EMAIL = os.getenv('PROTOCOL_REST_BACKEND') or 'admin@mail.ru'
```
- установленная электронная почта для администратора

```Python
ADMIN_PASSWORD = os.getenv('PROTOCOL_REST_BACKEND') or '123'
```
- установленный пароль для администратора

```Python
TOKEN = os.getenv('TOKEN') or 'default token'
```
- установленный токен по умолчанию 


