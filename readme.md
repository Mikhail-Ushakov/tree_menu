# Тестовое задание для компании UpTrader

## Django приложение позволяет через админку создавать древовидное меню

1. Клонируйте репозиторий:

```
git clone https://github.com/Mikhail-Ushakov/tree_menu.git
```

2. Установите виртуальное окружение:

```
python -m venv venv
```

3. И активируйте:

```
venv/Scripts/activate
```

4. Установите зависимости:

```
pip install -r requirements.txt
```

5. Перейдите в папку проекта:

```
cd tree_menu
```

6. Миграции:

```
python manage.py migrate
```

7. Создайте суперюзера:

```
python manage.py createsuperuser
```

8. В папке с файлом manage.py запустите сервер:

```
python manage.py runserver
```