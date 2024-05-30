from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

#create profile picture file name
import random
def idGenerator(size=5, chars="abcdefghijklmnopqrstuvwxyz0123456789"):
    return ''.join(random.choice(chars) for x in range(size))
def generate_profilePic_filename(instance, filename):
    return 'profilePics/%s-%s.jpg' % (instance.pk, idGenerator())

#Profile-Model
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import pytz
from timezone_field import TimeZoneField
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profilePic = ProcessedImageField(
        upload_to=generate_profilePic_filename,
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    country = models.TextField(max_length=2, blank=True)
    timezone = TimeZoneField(default='UTC', choices=[(pytz.timezone(tz), tz.replace('_', ' ')) for tz in pytz.all_timezones])
    
    isTeacher = models.BooleanField(default=False, help_text=_('I am a teacher'), db_index=True)

    objects=models.Manager()
    #languagesTaught
    #languagesSpoken


#Signals
from django.dispatch import receiver


#copy profile picture from social networks
# from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from allauth.account.signals import user_signed_up
@receiver(user_signed_up)
def on_user_signed_up(sender, request, *args, **kwargs):
    sociallogin = kwargs.get('sociallogin')
    if sociallogin:
        copy_profile_pic(request, sociallogin.account.user, sociallogin.account)
def copy_profile_pic(request, user, account):
    url = account.get_avatar_url()
    if url:
        profile = Profile(user=user)
        try:
            img_temp = NamedTemporaryFile(delete=True)
            content = urlopen(url).read()
            img_temp.write(content)
            img_temp.flush()
            profile.profilePic.save('', img_temp)
        except IOError:
            pass



#create Profile on User Creation
from django.db.models.signals import post_save
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()

#autodelete profilePic if deleted or changed
@receiver(models.signals.post_delete, sender=Profile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.profilePic:
        instance.profilePic.delete(save=False)
@receiver(models.signals.pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        profilePicOld = Profile.objects.get(pk=instance.pk).profilePic
    except Profile.DoesNotExist:
        return False
    profilePicNew = instance.profilePic
    if( not profilePicOld == profilePicNew and profilePicOld ):
        profilePicOld.delete(save=False)
