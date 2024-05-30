from . import Calendar
from channels.db import database_sync_to_async
from .models import Lesson, WorkingTime
from milinga import datetime, EMail
from django.db import transaction
from profiles import ProfileHelper

from django.db.models import Q

import random
import string

async def handleWSRequest(consumer, cmd, request):
    if cmd == 'book_lesson':
        # await database_sync_to_async(CalEvent(
        #     teacher_id = request['event']['teacher'],
        #     student = consumer.scope['user'],
        #     title = 'irgendwas',#oEvent.title,
        #     time_start = datetime.fromTimestamp(request['event']['start']),
        #     time_end = datetime.fromTimestamp(request['event']['end']),
        #     studentConfirmed = True,
        #     teacherConfirmed = False,
        # ))
        oEvent = {
            'start': request['start'],
            'end': request['end'],
        }
        oLesson = await bookLessonFromTimestamps(
            user = consumer.scope['user'],
            teacher_id = request['teacher'],
            event = oEvent
        )
        oLessonJson = {
                'eventId': oLesson.id,
                # 'title': oLesson.title,
                'start': datetime.toTimestamp(oLesson.time_start),
                'end': datetime.toTimestamp(oLesson.time_end),
                'studentConfirmed': True,
                'teacherConfirmed': False,
                'studentId': consumer.scope['user'].id,
                'teacherId': request['teacher'],
        }
        await consumer.sendToGroup(
            group = "userid_"+str(request['teacher']),
            wstype = 'update_cal_myEvents',
            obj = oLessonJson
        )
        await consumer.sendToOtherMe('update_cal_myEvents',oLessonJson)
        await EMail.sendLessonBooked(oLesson)
        return {
            'eventId' : oLesson.id,
        }

    elif cmd == 'accept_lesson':
        oLesson = await acceptOrRejectEvent(accept = True, teacher=consumer.scope['user'], eventId=request['eventId'])
        oLessonJson={
            'eventId': request['eventId'],
            'teacherConfirmed': True,
        }
        await consumer.sendToGroup("userid_"+str(oLesson.student_id),'update_cal_myEvents',oLessonJson)
        await consumer.sendToGroup("userid_"+str(oLesson.teacher_id),'update_cal_myEvents',oLessonJson)
        await EMail.sendLessonConfirmation(oLesson)

    elif cmd == 'reject_lesson':
        oLesson = await acceptOrRejectEvent(accept = False, teacher=consumer.scope['user'], eventId=request['eventId'])
        oLessonJson={
            'eventId': request['eventId'],
            'rejected': True,
        }
        await consumer.sendToGroup("userid_"+str(oLesson.student_id),'update_cal_myEvents',oLessonJson)
        await consumer.sendToGroup("userid_"+str(oLesson.teacher_id),'update_cal_myEvents',oLessonJson)
        await EMail.sendLessonRejected(oLesson)

    elif cmd == 'changeworkingtimes':
        await consumer.sendToOtherMe('workingtimes_update', {
            'create': request.get('create', []),
            'delete': request.get('delete', []),
        })
        return await updateWorkingTimes(
            teacher = consumer.scope['user'],
            create = request.get('create', []),
            delete = request.get('delete', []),
        )
    elif cmd == 'workingtimes_get':
        teacherId = consumer.scope['user'].id
        if request != None and 'teacherId' in request:
            teacherId = request['teacherId']
        return await getWorkingTimes(teacherId)
    elif cmd == 'myEvents_get': #'getMyEvents':
        return await getMyEvents(consumer.scope['user'].id)
    elif cmd == 'getTeacherCalendar':
        teacherId = consumer.scope['user'].id
        return await getTeacherCalendar(teacherId)
    elif cmd == 'getTeacherAvailablilty':
        teacherId = request['teacherId']
        studentId = consumer.scope['user'].id
        return await getTeacherAvailabliltyForStudent(teacherId=teacherId, studentId=studentId)


@database_sync_to_async
def getWorkingTimes(user_id):
    return list(Calendar.getWorkingTimes(teacher=user_id))

@database_sync_to_async
def getMyEvents(user_id):
    return list(Calendar.getMyEvents(user_id))

@database_sync_to_async
def getTeacherCalendar(user_id):
    return list(Calendar.getTeacherCalendar(teacher_id=user_id))

@database_sync_to_async
def getTeacherAvailabliltyForStudent(teacherId, studentId):
    return Calendar.getTeacherAvailabilityForStudent(studentId=studentId, teacherId=teacherId)

@database_sync_to_async
@transaction.atomic
def bookLessonFromTimestamps(user, teacher_id, event):
    oLesson = Lesson(
        teacher_id = teacher_id,
        student = user,
        title = 'irgendwas',#oEvent.title,
        time_start = datetime.fromTimestamp(event['start']),
        time_end = datetime.fromTimestamp(event['end']),
        studentConfirmed = True,
        teacherConfirmed = False,
        videoConferenceId = randomStringDigits(20)
    )
    oLesson.save()
    return oLesson
def randomStringDigits(stringLength=20):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

@database_sync_to_async
def acceptOrRejectEvent(accept, teacher, eventId):
    oLesson = Lesson.objects.get(teacher = teacher, id=eventId)
    if accept == True:
        oLesson.teacherConfirmed = True
        oLesson.save()
    else:
        oLesson.delete()
    return oLesson

@database_sync_to_async
@transaction.atomic
def updateWorkingTimes(teacher, create, delete):
    if(len(delete)>0):
        q_objects = Q()
        for d in delete:
            q_objects |= Q(working_from = datetime.fromTimestamp(d['start']), working_till = datetime.fromTimestamp(d['end']))
        WorkingTime.objects.filter(q_objects).delete()

    oCreateWorkingTimes = []
    for c in create:
        oCreateWorkingTimes.append(WorkingTime(
            teacher=teacher,
            working_from = datetime.fromTimestamp(c['start']),
            working_till = datetime.fromTimestamp(c['end']),
        ))
    WorkingTime.objects.bulk_create(oCreateWorkingTimes)
