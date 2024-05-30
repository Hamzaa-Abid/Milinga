from django.views.generic.base import RedirectView
from . import VideoConference
class VideoConferenceRedirectView(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        return VideoConference.getVideoConferenceUrl(kwargs['video_id'])