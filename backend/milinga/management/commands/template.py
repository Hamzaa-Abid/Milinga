#https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'template'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("Template gestartet!")
