#from profiles import ProfileHelper
from .models import Credits
from calendarapp.models import Lesson
from django.db.models import Q
from milinga import datetime

from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

async def handleWSRequest(consumer, cmd, request):
    if cmd == 'get':
        return await get_credits(consumer.scope['user'])
    elif cmd == 'give':
        oCredits = await save_credits(
            teacher = consumer.scope['user'],
            ownerId = request['to'],
            credits = request['credits'],
            date = datetime.now(),
        )

        oCreditsJson = {
            'id': oCredits.id,
            'credits': oCredits.credits,
            'ownerId': request['to'],
            'teacherId': consumer.scope['user'].id,
            'date': datetime.toTimestamp(oCredits.date),
        }
        await consumer.sendToOtherMe('update_credits', oCreditsJson)
        await consumer.sendToGroup("userid_"+str(request['to']), 'update_credits', oCreditsJson)
        return True

    # elif cmd == '...':
    #     user = await get_user_data(consumer.scope['user'].id)

    #     await consumer.sendToGroup("userid_"+owner_id, 'chat',{

    #     })
    #     await consumer.sendToOtherMe('chat',{

    #     })
    #     await save_message(
    #         sender_id=user.id,
    #         owner_id=owner_id,
    #         message=message,
    #         time_sent=time_sent,
    #     )


@database_sync_to_async
def get_credits(user):
    return [{
        'id': oCredits.id,
        'credits': oCredits.credits,
        'ownerId': oCredits.owner_id,
        'teacherId': oCredits.teacher_id,
        'date': datetime.toTimestamp(oCredits.date),
    } for oCredits in Credits.objects.filter(Q(teacher=user)|Q(owner=user)).order_by("-date")]

@database_sync_to_async
def save_credits(teacher, ownerId, credits, date):
    oCredits = Credits(
        teacher = teacher,
        owner = get_user_model().objects.get(id=ownerId),
        credits = credits,
        date = date,
    )
    oCredits.save()
    return oCredits

    # ChatMessage(
    #     sender_id=sender_id,
    #     owner_id=owner_id,
    #     message=message,
    #     time_sent=time_sent,
    # ).save()
