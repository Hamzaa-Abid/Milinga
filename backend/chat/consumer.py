import json
from milinga import datetime
from profiles import ProfileHelper
from .models import ChatMessage
from django.db.models import Q

from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

async def handleWSRequest(consumer, cmd, request):
    if cmd == 'get':
        oMe = consumer.scope['user']
        oQueryManager = ChatMessage.objects.filter(
            Q(sender=oMe)|Q(receiver=oMe)
        ).prefetch_related('sender__profile').prefetch_related('receiver__profile').order_by('time_sent')
        oMessages = await database_sync_to_async(list)(oQueryManager)
        oChatsById = {}
        for oMessage in oMessages:
            bSentByMe = False
            oChatPartner = oMessage.sender
            if oMessage.sender_id == oMe.id:
                bSentByMe = True
                oChatPartner = oMessage.receiver
            if oChatPartner.id not in oChatsById:
                oChatsById[oChatPartner.id] = {
                    'name': oChatPartner.first_name + ' ' + oChatPartner.last_name,
                    'profilePic': ProfileHelper.getProfilePicUrl(oChatPartner.profile.profilePic),
                    'messages': [],
                }
            oChatsById[oChatPartner.id]['messages'].append({
                'messageId': oMessage.id,
                'message': oMessage.message,
                'timestamp': datetime.toTimestamp(oMessage.time_sent),
                'sentByMe': bSentByMe,
                'timeRead': datetime.toTimestamp(oMessage.time_read) if oMessage.time_read!=None else None,
            })
        return oChatsById

        # return {
        #     '10' : {
        #         'name': 'Peter Schmidt',
        #         'imageURL': 'https://www.gravatar.com/avatar/0887faaf19731676293739952122229d?s=128&d=identicon&r=PG',
        #         'messages': [
        #             {
        #                 'message': 'Hi! Wie geht es dir? Hast du Zeit?',
        #                 'timestamp': 1580230188,
        #                 'sentByMe' : True,
        #             },{
        #                 'message': 'Danke gut, ja hab ich!',
        #                 'timestamp': 1580230198,
        #                 'sentByMe' : False,
        #             },
        #         ],
        #     },
        # }
    elif cmd == 'sendmsg':
        user = await get_user_data(consumer.scope['user'].id)
        receiver_id = request.get("to")
        message = request.get("msg", "")
        time_sent = datetime.now()#.replace(microsecond=0)

        oChatMessage = await save_message(
            sender_id=user.id,
            receiver_id=receiver_id,
            message=message,
            time_sent=time_sent,
        )

        await consumer.sendToGroup(
            group = "userid_"+str(receiver_id),
            wstype = 'update_chat',
            obj = {
                'userId': user.id,
                'messageId': oChatMessage.id,
                'message': message,
                'timestamp': datetime.toTimestamp(time_sent),
                'sentByMe' : False,
            }
        )
        await consumer.sendToOtherMe(
            wstype = 'update_chat',
            obj = {
                'userId': receiver_id,
                'messageId': oChatMessage.id,
                'message': message,
                'timestamp': datetime.toTimestamp(time_sent),
                'sentByMe' : True,
            }
        )
        return oChatMessage.id
    elif cmd == 'markread':
        oUserMessages = await messages_mark_read(consumer.scope['user'], request)
        
        for sender_id in oUserMessages:
            await consumer.sendToGroup(
                group = "userid_"+str(sender_id),
                wstype = 'chat_markedread',
                obj = oUserMessages[sender_id]
            )
        await consumer.sendToOtherMe(
            wstype = 'chat_markedread',
            obj = request
        )



@database_sync_to_async
def get_user_data(user_id):
    return get_user_model().objects.select_related('profile').get(id=user_id)

@database_sync_to_async
def save_message(sender_id, receiver_id, message, time_sent):
    oChatMessage = ChatMessage(
        sender_id=sender_id,
        receiver_id=receiver_id,
        message=message,
        time_sent=time_sent,
    )
    oChatMessage.save()
    return oChatMessage

@database_sync_to_async
def messages_mark_read(user, oMessageIds):
    oMessages = ChatMessage.objects.filter(receiver = user, id__in=oMessageIds)
    oMessagesList = list(oMessages)
    oMessages.update(
        receiver = user,
        time_read = datetime.now(),
    )
    oUserMessages = {}
    for oMessage in oMessagesList:
        if(oMessage.sender_id in oUserMessages):
            oUserMessages[oMessage.sender_id].append(oMessage.id)
        else:
            oUserMessages[oMessage.sender_id] = [oMessage.id]
    return oUserMessages
