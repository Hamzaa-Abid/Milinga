#from profiles import ProfileHelper
#from .models import ChatMessage
#from django.db.models import Q
from .models import Subject as SubjectModel

from channels.db import database_sync_to_async
#from django.contrib.auth import get_user_model
from django.utils.translation import activate

async def handleWSRequest(consumer, cmd, request):
    if cmd == 'getall':
        oSubjects = await get_subjects(languageCode=request['lang'])
        return [{
            'id': oSubject.id,
            'subject': oSubject.subject,
        } for oSubject in oSubjects]# if oEvent.student_id != studentId]

@database_sync_to_async
def get_subjects(languageCode):
    activate(languageCode)
    return list(SubjectModel.objects.all())

#@database_sync_to_async
#def save_message(sender_id, receiver_id, message, time_sent):
#    ChatMessage(
#        sender_id=sender_id,
#        receiver_id=receiver_id,
#        message=message,
#        time_sent=time_sent,
#    ).save()
