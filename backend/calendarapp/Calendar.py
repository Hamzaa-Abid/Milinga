from .models import WorkingTime, Lesson
from teachers.models import Teacher
from django.contrib.auth import get_user_model
from milinga import datetime
from django.db import transaction
from django.db.models import Q

User = get_user_model()

def getWorkingTimes(teacher=None):
    if(isinstance(teacher, User)):
        oUser = teacher
    else:
        oUser = User.objects.get(id=teacher)
    return [{
        'start': datetime.toTimestamp(oWorkingTime.working_from),
        'end': datetime.toTimestamp(oWorkingTime.working_till),
        'eventId': oWorkingTime.id,
    } for oWorkingTime in oUser.working_times.all()]

# def getMyLessonsWithTeacher(user, teacher):
#     return [{
#         'title': myEvent.title,
#         'from': datetime.toTimestamp(myEvent.time_start),
#         'till': datetime.toTimestamp(myEvent.time_end),
#         'teacherConfirmed': myEvent.teacherConfirmed,
#         'studentConfirmed': myEvent.studentConfirmed,
#     } for myEvent in Lesson.objects.filter(student=user, teacher=User.objects.get(id=teacher))]

# def getTeacherEvents(teacher):
#     return [{
#         'id': oLesson.id,
#         'title': oLesson.title,
#         'from': datetime.toTimestamp(oLesson.time_start),
#         'till': datetime.toTimestamp(oLesson.time_end),
#         'teacherConfirmed': oLesson.teacherConfirmed,
#         'studentConfirmed': oLesson.studentConfirmed,
#     } for oLesson in Lesson.objects.filter(teacher=teacher)]

def getTeacherAvailabilityForStudent(teacherId, studentId):
    oTeacherLessons = list(Lesson.objects.filter(teacher=teacherId))
    return {
        'workingTimes': getWorkingTimes(teacher=teacherId),
        'busy': [{
            'eventId': oEvent.id,
            'title': oEvent.title,
            'start': datetime.toTimestamp(oEvent.time_start),
            'end': datetime.toTimestamp(oEvent.time_end),
        } for oEvent in oTeacherLessons if oEvent.student_id != studentId],
    }

def getTeacherPublicCalendar(teacher_id):
    pass

def getMyEvents(user_id):
    return [{
        'eventId': oEvent.id,
        'title': oEvent.title,
        'start': datetime.toTimestamp(oEvent.time_start),
        'end': datetime.toTimestamp(oEvent.time_end),
        'studentConfirmed': oEvent.studentConfirmed,
        'teacherConfirmed': oEvent.teacherConfirmed,
        'teacherId': oEvent.teacher.id,
        'studentId': oEvent.student.id,
        'vcId': oEvent.videoConferenceId,#'https://meet.jit.si/milinga_'+oEvent.videoConferenceId+'#userInfo.displayName=%22'+oEvent.stude+'%22',
    } for oEvent in Lesson.objects.filter(Q(student_id=user_id)|Q(teacher_id=user_id))]

# def getNextVideoConference(user_id):
#     try:
#         return Lesson.objects.filter(Q(student_id=user_id)|Q(teacher_id=user_id)).filter(time_end__gt=datetime.datetime.now()).earliest('time_start')
#     except Lesson.DoesNotExist:
#         return None

