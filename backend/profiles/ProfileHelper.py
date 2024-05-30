from django.templatetags.static import static
from channels.db import database_sync_to_async
from .models import Profile

def getProfilePicUrl(oProcessedImageField):
    if oProcessedImageField:
        return oProcessedImageField.url
    else:
        return static('img/noprofilepic.png')


@database_sync_to_async
def getUserData(user):
    oProfile = Profile.objects.get(user=user)
    return {
        'name': oProfile.user.first_name + ' ' + oProfile.user.last_name,
        'profilePic': getProfilePicUrl(oProfile.profilePic),
    }
