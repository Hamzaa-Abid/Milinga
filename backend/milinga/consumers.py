import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.files.base import ContentFile
from tempfile import NamedTemporaryFile

# from asgiref.sync import sync_to_async


"""
// JS:
send('..._...', {}, function(oObject){...})
onReceive('...', function(oObject){})
sendToOtherMe('...', {});


// Python:
await consumer.sendToOtherMe('chat', {})
await consumer.sendToGroup("userid_"+user_id, 'chat',{})
"""

from chat import consumer as ChatConsumer
from calendarapp import consumer as CalendarConsumer
from milinga import consumer as MilingaConsumer
from teachers import consumer as TeacherConsumer
from profiles import consumer as ProfileConsumer
from subjects import consumer as SubjectConsumer
from credits import consumer as CreditsConsumer

#Beispiel: https://github.com/andrewgodwin/channels-examples/blob/master/multichat/chat/consumers.py
class Consumer(AsyncWebsocketConsumer):
    async def handleRequest(self, wstype, obj, tempfile):
        wstype_split = str(wstype).split('_', 1)

        if ( wstype_split[0] == 'subscribe' or wstype_split[0] == 'get' ) and len(wstype_split) > 1:
            if wstype_split[0] == 'subscribe':
                await self.group_add("update_"+wstype_split[1])
            wstype_split = str(wstype_split[1]).split('_', 1)
            if len(wstype_split)==1:
                wstype_split.append('get')
            else:
                wstype_split[1] += '_get'

        if(len(wstype_split) == 1):
            return await MilingaConsumer.handleWSRequest(self, wstype, obj)

        [wstype_prefix, wstype_command] = wstype_split
        if wstype_prefix == 'chat':
            return await ChatConsumer.handleWSRequest(self, wstype_command, obj)
        elif wstype_prefix == 'cal':
            return await CalendarConsumer.handleWSRequest(self, wstype_command, obj)
        elif wstype_prefix == 'auth':
            return await MilingaConsumer.handleWSRequest(self, wstype_command, obj)
        elif wstype_prefix == 'teachers':
            return await TeacherConsumer.handleWSRequest(self, wstype_command, obj)
        elif wstype_prefix == 'user' or wstype_prefix == 'profile':
            return await ProfileConsumer.handleWSRequest(self, wstype_command, obj, tempfile)
        elif wstype_prefix == 'subjects':
            return await SubjectConsumer.handleWSRequest(self, wstype_command, obj)
        elif wstype_prefix == 'credits':
            return await CreditsConsumer.handleWSRequest(self, wstype_command, obj)
        else:
            raise NameError('no function found')

    # async def updateSubscription(self, wstype, obj):
    #     self.sendToGroup('update_'+wstype, obj)

    async def sendToGroup(self, group, wstype, obj):
        await self.channel_layer.group_send(group, {
            "type": "forward.group",
            "wstype": wstype,
            "obj": obj,
        })
        # }, immediately=True)

    async def sendToOtherMe(self, wstype, obj):
        """
        Send JSON to all other windows which I have open
        """
        await self.channel_layer.group_send("userid_"+str(self.scope['user'].id), {
            "type": "forward.me",
            "wstype": wstype,
            "obj": obj,
            "sender": self.channel_name,
        })
        # }, immediately=True)

    """
    This consumer handles websocket connections for clients.
    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """

    async def group_add(self, groupName):
        if(not (groupName in self.groups)):
            await self.channel_layer.group_add(
                groupName,
                self.channel_name
            )
            self.groups.append(groupName)

    async def discardAllGroups(self):
        for group in self.groups:
            self.channel_layer.group_discard(group, self.channel_name)

    ##### WebSocket event handlers

    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        # Are they logged in?
        # if self.scope["user"].is_anonymous:
        #     # Reject the connection
        #     await self.accept()
        #     await self.send_json('stop')
        #     await self.close()  #unauthorized
        # else:
        # Accept the connection
        await self.accept()

        if not self.scope["user"].is_anonymous:
            await self.group_add("userid_"+str(self.scope["user"].id))

    # async def disconnect(self, close_code):
    #     await sync_to_async(self.scope['session'].save)()
    #     print("Session gespeichert")

    async def splitJsonBytes(self, dBytes):
        i=0
        while i<250:
            j = dBytes[i:].find(b'}')
            if j == -1:
                break
            i += j+1
            try:
                oJson = json.loads(dBytes[:i])
                dBytes = dBytes[i:]
                return oJson, dBytes
            except:
                pass

    async def receive(self, text_data=None, bytes_data=None):
        content = None
        tempfile = None
        if(text_data != None):
            content = json.loads(text_data)
        else:
            content, dBytes = await self.splitJsonBytes(bytes_data)
            # try:
            tempfile = NamedTemporaryFile(delete=True)
            tempfile.write(dBytes)
            tempfile.flush()
            # oProfile = consumer.scope['user'].profile
            # oProfile.profilePic.save('', tempfile, save=True)
            # return oProfile.profilePic.url
            # except IOError:
            #     pass


        if content.get('m') == True:
            await self.sendToOtherMe(
                wstype = content.get('t'),
                obj = content.get('o')
            )
            return

        oRtn = {}
        errorMsg = None
        try:
            oRtn = await self.handleRequest(
                wstype = content.get('t'),
                obj = content.get('o'),
                tempfile = tempfile
            )
        except Exception as e:
            errorMsg = str(e)


        sCallbackId = content.get('f')
        if sCallbackId is not None:
            oToSend = {
                't': content.get('t'),
                'o': oRtn,
                'f': sCallbackId,
                # 'e': errorMsg if errorMsg else None
            }
            if(errorMsg != None):
                oToSend['e'] = errorMsg
            await self.send_json(oToSend)

    async def send_json(self, oJson):
        await self.send(text_data=json.dumps(oJson))

    async def disconnect(self, code):
    #     """
    #     Called when the WebSocket closes for any reason.
    #     """
        await self.discardAllGroups()

    async def forward_group(self, event):
        """
        Called when a group message was received.
        """
        # Send a message down to the client
        # print({
        #     't': event['wstype'],
        #     'o': event['obj'],
        # })
        await self.send_json({
            't': event['wstype'],
            'o': event['obj'],
        })

    async def forward_me(self, event):
        """
        Called when a group message was received, which is for my other windows
        """
        if event['sender'] != self.channel_name:
            await self.send_json({
                't': event['wstype'],
                'o': event['obj'],
            })
