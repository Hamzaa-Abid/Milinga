import jwt
from django.contrib.auth import get_user_model

def tokenLogin(token):
    oAuth = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    if(oAuth != None):
        User = get_user_model()
        user = User.objects.get(id=oAuth['user_id'])
        login(consumer.scope, user, backend='allauth.account.auth_backends.AuthenticationBackend')
        return user
    else:
        raise NameError('token not valid')


