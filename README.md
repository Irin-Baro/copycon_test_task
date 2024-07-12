# copycon_test_task
Тестовое задание от "Копикон" на позицию "Junior разработчик"

### Описание
>API сервис для выполнения POST запроса и извлечения значения поля __name.

### Технологии
- Python 3.9.10
- Django 4.2.14
- Django REST Framework
- Postman

### Запуск проекта

Клонируйте репозиторий с сайта Github:

```sh
git clone https://github.com/Irin-Baro/copycon_test_task.git
```

Установите и активируйте виртуальное окружение:

```sh
Для пользователей Windows:
python -m venv venv
source venv/Scripts/activate
```

Установите зависимости из файла requirements.txt:

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполните миграции:

```sh
python manage.py migrate
```

Запуск проекта - в папке с файлом manage.py выполните команду:

```sh
python manage.py runserver
```

Выполните запрос:

```sh
http://127.0.0.1:8000/api/test-task/
```

### Авторы

- [Ирина Баронская](https://t.me/irin_baro)
