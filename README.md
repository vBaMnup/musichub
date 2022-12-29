# Проект Musichub

### Описание
MusicHub - приложение для музыкантов и любителей музыки. Могут могут добавлять треки и лицензии, создавать альбомы и плейлисты, оставлять комментарии и лайки, прослушать и скачивать музыку.
### Возможности

- Регистрация
- Авторизация
- Публикация треков
- Подписки на авторов
- Создание альбомов
- Добавление треков в плейлисты
- Комментарии к альбомам и трекам
- Прослушивание и скачивание музыки
### Технологии

- Python 3.10
- Django 4.1.4
- Django REST Framework
- PostgreSQL
- psycopg2
- Djoser
- Pillow

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

``` bash
git clone git@github.com:vBaMnup/musichub.git
```
Создать и активировать виртуальное окружение:
```bash
python3 -m venv venv
. venv/bin/activate
```
Установить зависимост
```bash
pip install -r requirements.txt
```
Добавить в файл .env (musichub/musichub/config/):
```python
DB_ENGINE='Ваша база данных PostgresSQL'
DB_NAME='Имя базы данных'
POSTGRES_USER='Пользователь базы данных'
POSTGRES_PASSWORD='Пароль пользователя базы данных'
DB_HOST='Хост базы данных'
DB_PORT='Порт базы данных'
SECRET_KEY='Ваш секретный ключ'
DEBUG=Режим разработчика (True or False)
```

Перейти в директорию с manage.py
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatics
```
Запустить проект:
```bash
python manage.py runserver
```
### Пример использования
Регистрация пользователя POST /api/v1/users
```json
{
  "email": "user@example.com",
  "username": "string",
  "first_name": "string",
  "last_name": "string",
  "password": "string"
}
```
Получение токена POST /api/v1/auth/token/login/
```json
{
  "password": "string",
  "username": "string"
}
```
Загрузка трека POST /api/v1/audio/track/
```json
{
  "title": "string",
  "license": 0,
  "genre": [
    0
  ],
  "album": 0,
  "file": "http://example.com",
  "private": true,
  "cover": "http://example.com",
}
```
Подробнее с документацией можно ознакомиться: /redoc или /swagger
### Автор
[Paskov Andrey](https://vk.com/andrey_paskov)