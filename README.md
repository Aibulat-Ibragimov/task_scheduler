# Task_scheduler
## **Описание проекта**

Проект представляет собой веб-приложение, которое позволит пользователям добавлять, просматривать, редактировать и удалять задачи.

## **Стэк технологий**

Python 3.9 <br>
Django 4.2.11 <br>
djangorestframework 3.15.1 <br>
tzdata==2024.1 <br>
sqlparse==0.4.4 <br>
typing_extensions==4.10.0 <br>
asgiref==3.8.1 <br>

---


## Локальный запуск проекта

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Aibulat-Ibragimov/task_scheduler.git
cd kittygram_final
```

Cоздать и активировать виртуальное окружение, установить зависимости:

```bash
python3 -m venv venv && \ 
    source venv/scripts/activate && \
    python -m pip install --upgrade pip && \
    pip install -r backend/requirements.txt
```

Выполнить миграции:

```bash
python manage.py makemigrations tasks
python manage.py migrate
```

Запустите сервер разработки Django:

```bash
python manage.py runserver
```

**~~Автор проекта:~~** Ибрагимов Айбулат https://github.com/Aibulat-Ibragimov