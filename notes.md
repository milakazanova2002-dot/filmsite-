python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
venv\Scripts\activate

pip install django

Создаём проект:
django-admin startproject filmsite .

Создаём первое приложение:
python manage.py startapp films

Первый запуск:
python manage.py runserver


view -> url
