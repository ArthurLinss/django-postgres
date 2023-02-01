# Django-Postgres

Example demonstrating use of django with postgres DB. Also includes evnironment setup. Wrapped up with docker support.


# Setup

```
pip install django
pip install django-environ
pip install psycopg2-binary (for macos, otherwise: pip install psycopg2)
```

# Further Reading
- https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
- https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial

# Commands

Setup:
```
python3 -m venv venv
source venv/bin/activate
django-admin startproject blabla
cd blabla
django-admin startapp bla
(deactivate)
```

Dev:
```
touch .env
python manage.py check
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

Git:
```
git init
touch .gitignore
touch README.md
git status
git add .
git status
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/exitfromparadise/django-postgres.git
git remote --v
git push -u origin main
```

# Postgres

Use pgadmin to check database in development. The important stuff happens in settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
```

Checkout in left coloumn: postgres -> Databases -> dbtest -> Schemas -> public -> Tables


# Env

Typical .env file for postgres (in root directory):

```
SECRET_KEY=XZY
DB_NAME=test
DB_USER=username
DB_PASSWORD=passwort
DB_HOST=localhost
DB_PORT=5432
```


# Docker


```
docker build -t django-postgres .
```

```
docker-compose build
docker-compose up
```

or
```
docker-compose up --build
```
(you could also add `-d` for detachted mode).

Useful:
```
docker-compose down --volumes
```
(create DB init, https://stackoverflow.com/questions/59715622/docker-compose-and-create-db-in-postgres-on-init)


```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose down
```
