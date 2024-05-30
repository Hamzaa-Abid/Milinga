from channels.db import database_sync_to_async

# from django.core.mail import send_mail
from django.utils.formats import localize
import pytz

# from .tasks import send_mail
from milinga import tasks

@database_sync_to_async
def sendLessonConfirmation(oLesson):
    sLessonTimeLocal = localize(oLesson.time_start.astimezone(oLesson.student.profile.timezone)) + " (Timezone: " + oLesson.student.profile.timezone.zone + ")"
    tasks.send_mail(
        'The teacher confirmed your booked lesson',
        'Hi!\n\nThe teacher ' + oLesson.teacher.first_name + ' ' + oLesson.teacher.last_name + ' confirmed your booking on ' + sLessonTimeLocal + ".\n\nYour Milinga-Team",
        oLesson.student.email
    )

@database_sync_to_async
def sendLessonRejected(oLesson):
    sLessonTimeLocal = localize(oLesson.time_start.astimezone(oLesson.student.profile.timezone)) + " (Timezone: " + oLesson.student.profile.timezone.zone + ")"
    tasks.send_mail(
        'The teacher rejected your lesson',
        'Hi!\n\nThe teacher ' + oLesson.teacher.first_name + ' ' + oLesson.teacher.last_name + ' rejected your booking on ' + sLessonTimeLocal + ".\n\nYour Milinga-Team",
        oLesson.student.email
    )

@database_sync_to_async
def sendLessonBooked(oLesson):
    sLessonTimeLocal = localize(oLesson.time_start.astimezone(oLesson.teacher.profile.timezone)) + " (Timezone: " + oLesson.teacher.profile.timezone.zone + ")"
    tasks.send_mail(
        'Lesson booked',
        'Hi!\n\nThe student ' + oLesson.student.first_name + ' ' + oLesson.student.last_name + ' booked a lesson with you on ' + sLessonTimeLocal + ".\n\nYour Milinga-Team",
        oLesson.teacher.email
    )

def notify_unread_chat_message(oReceiver):
    tasks.send_mail(
        'Unread Chat Messages',
        'Hi!\n\nYou have unread Chat messages! Please check your chat at milinga.com!\n\nYour Milinga-Team',
        oReceiver.email
    )