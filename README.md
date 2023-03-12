# user_request_app


## Назначение проекта

Приложение имитирует работу frontend: отправляет запросы на user_response_app и отображает на экране полученные данные

```Bash 
git clone https://github.com/aidarhaertdinov/user_response_app.git
```

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

### Все переменные окружения представлены в `.env` файле

`PROTOCOL_REST_BACKEND = os.getenv('PROTOCOL_REST_BACKEND')` - протокол приложения

`URL_REST_BACKEND = os.getenv('URL_REST_BACKEND')` - адрес приложения

`PORT_REST_BACKEND` - порт приложения

`SECRET_KEY = os.getenv('SECRET_KEY')` - используют значение секретного ключа в качестве криптографического ключа, полезного для генерации подписей или токенов. [ссылка на документацию](https://explore-flask.readthedocs.io/en/latest/configuration.html)

`WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')` - для защиты веб-форм от атаки под названием Cross-Site Request Forgery. [ссылка на документацию](https://flask-wtf.readthedocs.io/en/0.15.x/config/)

`SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')` - если установлен  `True`, то Flask-SQLAlchemy будет отслеживать изменения объектов и посылать сигналы. [ссылка на документацию](https://flask-sqlalchemy-russian.readthedocs.io/ru/latest/config.html)

`ADMIN_EMAIL = os.getenv('PROTOCOL_REST_BACKEND')` - установленная электронная почта для администратора

`ADMIN_PASSWORD = os.getenv('PROTOCOL_REST_BACKEND')` - установленный пароль для администратора

`TOKEN = os.getenv('TOKEN')` - установленный токен по умолчанию 

P.S. `.env` файла не должно быть в репозитории. Сохранен для того чтобы, другой человек мог использовать приложение.
Никаких учетных записей не должно быть.

### Для того чтобы работали Pytest необходимо запущенное `user_response_app` приложение

