from huey import crontab
from huey.contrib.djhuey import periodic_task, task
from huey.contrib.djhuey import db_periodic_task, db_task
import datetime
from milinga import EMail

from django.core.mail import send_mail as django_send_mail
@task()
def send_mail(subject, text, recipient):
    django_send_mail('[milinga] '+subject, text, 'info@milinga.com', [recipient], fail_silently=False,)

from chat.models import ChatMessage 
@db_periodic_task(crontab(minute='*/30'))
def send_mail_on_unread_chat():
    oUnreadMessages = ChatMessage.objects.filter(time_read=None, receiver_notified=False, time_sent__lt=datetime.datetime.now()-datetime.timedelta(minutes=15))

    oReceivers = set()
    for oUnreadMessage in oUnreadMessages:
        oReceivers.add(oUnreadMessage.receiver)

    for oReceiver in oReceivers:
        EMail.notify_unread_chat_message(oReceiver)
    
    oUnreadMessages.update(receiver_notified=True)