from django import template
from calendarapp import Calendar
from videoconference import VideoConference
from milinga import datetime

register = template.Library()

@register.inclusion_tag('videoconference/videoconference_countdown.html')
def show_next_videoconference(user):
    oCalEvent = Calendar.getNextVideoConference(user.id)
    if oCalEvent == None:
        oNextVc = None
    else:
        oNextVc = {
            'timestamp': datetime.toTimestamp(oCalEvent.time_start),
            'link': VideoConference.getVideoConferenceUrl(oCalEvent.videoConferenceId),
        }
    return {
        'next_vc' : oNextVc,
    }
