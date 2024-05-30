#https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
from django.core.management.base import BaseCommand, CommandError

from datetime import datetime
from chat.models import ChatMessage

class Command(BaseCommand):
    help = 'template'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ChatMessage.objects.get(time_read=blank)
        now = datetime.now().time()
        print("test", now)


