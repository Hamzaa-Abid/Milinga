from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# {
#     'id':'10',
#     'name': 'Peter Schmidt',
#     'imageURL': 'https://www.gravatar.com/avatar/0887faaf19731676293739952122229d?s=128&d=identicon&r=PG',
#     'messages': [{
#         'message': 'Hi! Wie geht es dir? Hast du Zeit?',
#         'timestamp': 1580230188,
#         'sentByMe' : True,
#     },{
#         'message': 'Danke gut, ja hab ich!',
#         'timestamp': 1580230198,
#         'sentByMe' : False,
#     }],
# }

class ChatMessage(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        # blank=False,
        null=True,
        db_index=True,
        related_name='messages_sent',
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        # blank=False,
        null=True,
        db_index=True,
        related_name='messages_received',
    )
    message = models.TextField(
        null=False,
        blank=False,
    )
    time_sent = models.DateTimeField()
    time_read = models.DateTimeField(blank=True, null=True)

    receiver_notified = models.BooleanField(blank=False, null=False, default=False)

