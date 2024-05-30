from channels.db import database_sync_to_async
from django.db.models import Q
from .models import Profile
from django.contrib.auth import get_user_model
from teachers.models import Teacher, TeacherTeaches
from djmoney.money import Money

async def handleWSRequest(consumer, cmd, request, tempfile):
    if cmd == 'get':
        return await get_profile(consumer, request)
    elif cmd == 'save':
        return await save_profile(consumer, request)
    elif cmd == 'profilepic':
        return await change_profilepic(consumer, request, tempfile)


@database_sync_to_async
def get_profile(consumer, request):
    user = consumer.scope['user']
    oRtn = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'country': user.profile.country,
        'timezone': user.profile.timezone.zone,
        'isTeacher': user.profile.isTeacher,
    }
    teacher = getattr(user, 'teacher', None)
    if(teacher != None):
        oRtn['description'] = str(user.teacher.description)
        oRtn['pricePerHour'] = str(user.teacher.pricePerHour.amount)
        oRtn['currency'] = str(user.teacher.pricePerHour.currency)
        oRtn['videoUrl'] = user.teacher.videoUrl
        oRtn['teaches'] = [teacherTeaches.subject_id for teacherTeaches in TeacherTeaches.objects.filter(teacher=user.teacher)]
    return oRtn


@database_sync_to_async
def save_profile(consumer, request):
    #Speichere User
    user = consumer.scope['user']
    user.first_name = request['first_name']
    user.last_name = request['last_name']
    user.save()

    #Speichere Profil
    user.profile.country = request['country']
    user.profile.timezone = request['timezone']
    user.profile.isTeacher = request['isTeacher']
    user.profile.full_clean()
    user.profile.save()

    if(request['isTeacher'] == True):
        #Teacher-Profil speichern
        Teacher.objects.update_or_create(
            user = user,
            defaults = {
                'description' : request['description'],
                'pricePerHour' : Money(request['pricePerHour'], request['currency']),
                'videoUrl' : request['videoUrl'],
            }
        )

        #Teacher-Unterrichtsfächer speichern
        TeacherTeaches.objects.filter(teacher=user.teacher).delete()
        oBulkTeacherTeaches = []
        for subject_id in request['teaches']:
            oBulkTeacherTeaches.append(TeacherTeaches(
                teacher=user.teacher,
                subject_id=subject_id
            ))
        if (len(oBulkTeacherTeaches) > 0):
            TeacherTeaches.objects.bulk_create(oBulkTeacherTeaches)

    return True

@database_sync_to_async
def change_profilepic(consumer, request, tempfile):
    oProfile = consumer.scope['user'].profile
    oProfile.profilePic.save('', tempfile, save=True)
    return oProfile.profilePic.url

