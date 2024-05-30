from django.core.management.base import BaseCommand, CommandError

from django.conf import settings
import json

from django.contrib.auth import get_user_model
User = get_user_model()

from profiles.models import Profile
from teachers.models import Teacher, TeacherTeaches
from reviews.models import Review
from subjects.models import Subject

import random
import string

from django.db import transaction

def getTestData():
    json_data = open(settings.STATIC_ROOT + '/testdata.json')   
    rtn = json.load(json_data)
    json_data.close()
    return rtn

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



class Command(BaseCommand):
    help = 'Create testdata'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        oTestdatas = getTestData()

        oTeachers = []
        for oTestdata in oTestdatas:
            with transaction.atomic():
                [first_name, last_name] = oTestdata['name'].split(' ', 1)
                email = first_name + '_' + randomString() + '@test.de'
                user = User(
                    username=email,
                    first_name = first_name,
                    last_name = last_name,
                    email=email,
                    password='test'
                )
                user.save()
                Profile(
                    user_id = user.id,
                    #profilePic = ...
                    description_short = oTestdata['description_title'],
                    description = oTestdata['description_short'],
                    isTeacher = True
                ).save()
                teacher = Teacher(
                    user_id = user.id,
                    videoUrl = oTestdata['video_url'],
                    acceptsBitcoins = True,
                    acceptsFiat = True
                )
                teacher.save()

                for i in range(0,3):
                    try:
                        TeacherTeaches(
                            teacher = teacher,
                            subject = Subject.objects.order_by("?").first()
                        ).save()
                    except:
                        pass

                Review(
                    reviewer_id = user.id,
                    reviewed_id = user.id,
                    rating = oTestdata['rating'],
                    review = 'test'
                ).save()
