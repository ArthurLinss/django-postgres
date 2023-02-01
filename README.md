# Django-Postgres

Example demonstrating use of django with postgres DB. Also includes evnironment setup.

# Setup

```
pip install django
pip install django-environ
pip install psycopg2-binary (for macos, otherwise: pip install psycopg2)
```

# Further Reading
- https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8

# Commands

Setup:
```
python3 -m venv venv
source venv/bin/activate
django-admin startproject blabla
cd blabla
django-admin startapp bla
```
Dev:
```
python manage.py check
python manage.py migrate
python manage.py makemigrations
```

# Postgres

Use pgadmin to check database in development.

Checkout in left coloumn: postgres -> Databases -> dbtest -> Schemas -> public -> Tables
