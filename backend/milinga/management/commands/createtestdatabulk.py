from django.core.management.base import BaseCommand, CommandError

from django.conf import settings
import json

from django.contrib.auth import get_user_model
User = get_user_model()

from profiles.models import Profile
from teachers.models import Teacher
from reviews.models import Review

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

    @transaction.atomic
    def handle(self, *args, **options):
        oTestdatas = getTestData()
        oBulkUser = []
        oBulkProfile = []
        oBulkTeacher = []
        oBulkReview = []

        for oTestdata in oTestdatas:
            [first_name, last_name] = oTestdata['name'].split(' ', 1)
            email = first_name + '_' + randomString() + '@test.de'
            user = User(
                username=email,
                first_name = first_name,
                last_name = last_name,
                email=email,
                password='test'
            )
            oBulkUser.append(user)
            oBulkProfile.append(Profile(
                user = user,
                #profilePic = ...
                description_short = oTestdata['description_title'],
                description = oTestdata['description_short'],
                isTeacher = True
            ))
            oBulkTeacher.append(Teacher(
                user = user,
                videoUrl = oTestdata['video_url'],
                acceptsBitcoins = True,
                acceptsFiat = True
            ))
            oBulkReview.append(Review(
                reviewer = user,
                reviewed = user,
                rating = oTestdata['rating'],
                review = 'test'
            ))
        
        User.objects.bulk_create(oBulkUser)
        Profile.objects.bulk_create(oBulkProfile)
        Teacher.objects.bulk_create(oBulkTeacher)
        Review.objects.bulk_create(oBulkReview)
