# Django-Postgres

This django example demonstrates the following tools and technologies:
- postgreSQL DB
- docker resp. docker-compose support
- HTMX in django templates
- environment variables (settings)
- self-defined management commands
- simple test cases
- many to many field usage

# Setup

```
pip install django
pip install django-environ
pip install psycopg2-binary (for macos, otherwise: pip install psycopg2)
pip install django-crispy-forms crispy-tailwind
```

# Further Reading
- https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
- https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
- https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/
- HTMX: https://www.youtube.com/watch?v=KVq_DjIfnBo&list=WL&index=1&ab_channel=JustDjango
- HTMX tutorial: https://justdjango.com/blog/dynamic-forms-in-django-htmx

# TODO:

- fix env settings for postgresql database (for production)
- adding auto-tests
- add api maybe

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
python manage.py test
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


# MTM

Note that MTM fields return a queryset. To get subject of a teacher, do
```
Teacher.objects.filter(name="Niels Bohr")[0].subject.all()[0]
```

# HTMX
```
<script src="https://unpkg.com/htmx.org@1.8.5"></script>
<!-- have a button POST a click via AJAX -->


<body>
<script>
    document.body.addEventListener("htmx:configRequest", (event) => {
        event.detail.headers['X-CSRFToken'] = "{{ csrf_token }}";
    }) 
</script>
```


# TODO

Currently, manually setting name for "HOST" in settings.py is needed between switchting from local run to local docker run:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "dbtest",
        'USER': "postgres",
        'PASSWORD': "passwort",
        #'HOST': "db", # for docker
        'HOST' : 'localhost', # for local run
        'PORT': "5432",
    }
}
```
