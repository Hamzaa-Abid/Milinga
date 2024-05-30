from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class RedirectWWWMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        host = request.get_host()
        if host and host.count('.') == 1:   #keine Subdomain
            redirect_url = 'https://www.%s%s' % (
                host, request.get_full_path()
            )
            return HttpResponsePermanentRedirect(redirect_url)

        return self.get_response(request)