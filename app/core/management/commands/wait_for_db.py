"""
Django command to wait for DB to be available.
"""
import time

from django.db import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    "DDjango command to wait for database."

    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
