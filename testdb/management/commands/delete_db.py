

from django.core.management.base import BaseCommand, CommandError
from django.db import connection


class Command(BaseCommand):

    help = 'resets db'

    def add_argument(self, parser):
        pass

    def handle(self, *args, **kwargs):
        print("delete DB")

        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE;")
            cursor.execute("CREATE SCHEMA public;")


        print("deleted DB, now run: ")
        print("   python manage.py migrate")
