from channels.db import database_sync_to_async
from django.db import transaction

from django.db.models import Q

# from profiles.models import Profile
from teachers.models import Teacher as Teacher
# from teachers.models import TeacherTeaches as TeacherTeaches
# from teachers.forms import TeacherForm
from profiles import ProfileHelper

from subjects.models import Subject
from django.core.paginator import Paginator

async def handleWSRequest(consumer, cmd, request):
    if cmd == 'list':
        return await get_teachers(
            subject_id = request['subjectId'],
            page = request['page'],
        )

from allauth.account.admin import EmailAddress
@database_sync_to_async
def get_teachers(subject_id, page):
    try:
        Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        subject_id = Subject.objects.get(subject_en='English').id
    teachers = Teacher.objects.prefetch_related('teaches').select_related('user__profile').filter(teaches__subject_id=subject_id).filter(user__profile__isTeacher=True)
    # teacherprofiles = Profile.objects.filter(isTeacher=True).select_related('user__teacher__teaches__subject').filter(user__teacher__teaches__subject__subject='English')#.select_related('user__reviews')
    #import pdb;pdb.set_trace()
    teacher_data_list = []
    for teacher in teachers.iterator():
        if not EmailAddress.objects.filter(user=teacher.user, verified=True).exists():
            continue
        teacher_data = {}
        teacher_data['name'] = teacher.user.first_name + ' ' + teacher.user.last_name
        teacher_data['teaches'] = []
        for teacherteaches in teacher.teaches.iterator():
            teacher_data['teaches'].append(teacherteaches.subject_id)
        teacher_data['country'] = teacher.user.profile.country
        teacher_data['description'] = teacher.description
        teacher_data['videoUrl'] = teacher.videoUrl
        teacher_data['profilePic'] = ProfileHelper.getProfilePicUrl(teacher.user.profile.profilePic)
        teacher_data['userId'] = teacher.user.id
        teacher_data['pricePerHour'] = str(teacher.pricePerHour.amount)
        teacher_data['currency'] = teacher.pricePerHour.currency.code
        reviews = teacher.user.reviews.all()
        if len(reviews) > 0:
            teacher_data['rating'] = sum(item.rating for item in reviews) / len(reviews)
        else:
            teacher_data['rating'] = -1
        
        #star-rating:
        # teacher_data['rating'] = round(rating*2, 0)/2
        teacher_data['rating'] = round(4.2*10, 0)/10
        # teacher_data['rating_full_count'] = range(int(teacher_data['rating']))
        # teacher_data['rating_half_bool'] = teacher_data['rating'] % 1 == 0.5

        teacher_data_list.append(teacher_data)


    # paginator = Paginator(teacher_data_list, 10) # Show 25 contacts per page

    # teachers = paginator.get_page(page)

    # return teachers
    return teacher_data_list
