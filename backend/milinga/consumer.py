from django.contrib.auth import authenticate
from channels.auth import login, logout
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

from django.conf import settings
# import jwt
from django.contrib.auth import get_user_model

# from django.db import transaction

# from django.db.models import Q

# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.conf import settings
from django.utils import translation
# from django.conf.locale import LANG_INFO

# from django.middleware.csrf import get_token

from rest_framework.authtoken.models import Token

async def handleWSRequest(consumer, cmd, request):
    # if cmd == 'login':
    #     user = await database_sync_to_async(authenticate)(consumer.scope, email=request['eMail'], password=request['pass'])
    #     if user is not None:
    #         # login the user to this session.
    #         await login(consumer.scope, user, backend='allauth.account.auth_backends.AuthenticationBackend')
    #         # save the session (if the session backend does not access the db you can use `sync_to_async`)
    #         # consumer.scope['session'].modified = True
    #         # await database_sync_to_async(consumer.scope['session'].save)()
    #         # await sync_to_async(consumer.scope['session'].save)()
    #         await consumer.group_add("userid_"+str(consumer.scope["user"].id))

    #         jwt_token = jwt.encode({
    #             'user_id': user.id,
    #         }, settings.SECRET_KEY, algorithm='HS256').decode('UTF-8')
    #         return {
    #             'loggedIn': True,
    #             'token' : jwt_token,
    #         }
    #     else:
    #         return {
    #             'loggedIn': False,
    #         }
    #     # return await consumer_login(
    #     #     consumer = consumer,
    #     #     email = request['eMail'],
    #     #     password = request['pass'],
    #     #     stayloggedin = request['stayLoggedIn'],
    #     # )
    if cmd == 'auth':
        oUser = await get_user_by_tokenkey(
            request['key'],
        )
        if oUser != None:
            await login(consumer.scope, oUser, backend='allauth.account.auth_backends.AuthenticationBackend')
            await consumer.group_add("userid_"+str(consumer.scope["user"].id))
            return await get_user(
                user_id = consumer.scope["user"].id,
                bGetPrivateData = True,
            )        
        else:
            return None
    elif cmd == 'logout':
        await consumer.discardAllGroups()
        # consumer.channel_layer.group_discard(
        #     "userid_"+str(consumer.scope["user"].id),
        #     consumer.channel_name
        # )
        await logout(consumer.scope)
        return
    # elif cmd == 'jwt':
    #     oAuth = jwt.decode(request['token'], settings.SECRET_KEY, algorithms=['HS256'])
    #     if(oAuth != None):
    #         User = get_user_model()
    #         user = await database_sync_to_async(User.objects.get)(id=oAuth['user_id'])
    #         await login(consumer.scope, user, backend='allauth.account.auth_backends.AuthenticationBackend')
    #         await consumer.group_add("userid_"+str(consumer.scope["user"].id))
    #         return await get_user(
    #             user_id = consumer.scope["user"].id,
    #         )
    #     else:
    #         return None
    # elif cmd == 'getCSRFToken':
    #     # oRequest = {}
    #     # oRequest.META = {}
    #     class requestForToken:
    #         META = {}
    #     sToken = get_token(requestForToken)
    #     return sToken
    elif cmd == 'getLang':
        langInfos = [translation.get_language_info(k) for k, v in settings.LANGUAGES]
        rtn = [{
            'code': langInfo['code'],
            'name_local': langInfo['name_local'],
        } for langInfo in langInfos]
        return rtn
    elif cmd == 'getUser':
        sUserId = request['userId']
        if sUserId == None or sUserId == 'me':
            sUserId = consumer.scope['user'].id

        oUser = await get_user(
            user_id = sUserId,
            bGetPrivateData = False,
        )
        if sUserId == consumer.scope['user'].id:
            oUser['id'] = sUserId
        
        return oUser

from profiles import ProfileHelper
from allauth.account.models import EmailAddress
@database_sync_to_async
def get_user(user_id, bGetPrivateData):
    User = get_user_model()
    oUser = User.objects.select_related('profile').get(id=user_id)

    oRtn = {
        'id': oUser.id,
        'name': oUser.first_name + ' ' + oUser.last_name,
        'profilePic': ProfileHelper.getProfilePicUrl(oUser.profile.profilePic),
        'country': oUser.profile.country,
        'isTeacher': oUser.profile.isTeacher,
    }
    if(oUser.profile.isTeacher == True):
        oRtn['description'] = oUser.teacher.description,
        oRtn['videoUrl'] = oUser.teacher.videoUrl
        oRtn['pricePerHour'] = str(oUser.teacher.pricePerHour.amount)
        oRtn['currency'] = oUser.teacher.pricePerHour.currency.code
        oRtn['acceptsBitcoins'] = oUser.teacher.acceptsBitcoins
        oRtn['acceptsFiat'] = oUser.teacher.acceptsFiat
    if(bGetPrivateData == True):
        oRtn['email'] = oUser.email
        oRtn['emailVerified'] = EmailAddress.objects.filter(email__exact=oUser.email, verified=True).exists()
    return oRtn

@database_sync_to_async
def get_user_by_tokenkey(key):
    oToken = Token.objects.get(key=key)
    if(oToken.user_id):
        return get_user_model().objects.get(id = oToken.user_id)



# @database_sync_to_async
# def consumer_login(consumer, email, password, stayloggedin):
#     user = authenticate(consumer.scope, username=email, password=password)
#     if user is not None:
#         # login the user to this session.
#         login(consumer.scope, user)
#         # save the session (if the session backend does not access the db you can use `sync_to_async`)
#         consumer.scope["session"].save()
#         await consumer.group_add("userid_"+str(consumer.scope["user"].id))

#         return True
#     else:
#         return False