#from profiles import ProfileHelper
#from .models import ChatMessage
#from django.db.models import Q

from channels.db import database_sync_to_async
#from django.contrib.auth import get_user_model

async def handleWSRequest(consumer, cmd, request):
    if cmd == '...':
        return {}
    elif cmd == '...':
        user = await get_user_data(consumer.scope['user'].id)

        await consumer.sendToGroup("userid_"+receiver_id, 'chat',{

        })
        await consumer.sendToOtherMe('chat',{

        })
        await save_message(
            sender_id=user.id,
            receiver_id=receiver_id,
            message=message,
            time_sent=time_sent,
        )


@database_sync_to_async
def get_user_data(user_id):
    return get_user_model().objects.select_related('profile').get(id=user_id)

@database_sync_to_async
def save_message(sender_id, receiver_id, message, time_sent):
    ChatMessage(
        sender_id=sender_id,
        receiver_id=receiver_id,
        message=message,
        time_sent=time_sent,
    ).save()
