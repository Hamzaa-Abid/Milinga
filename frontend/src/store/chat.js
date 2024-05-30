// import {chat} from 'store/chat.js';
//
// $chat = {
// 	'1' : {
// 		name: "Ma2 U"
// 		profilePic: "/static/img/noprofilepic.png",
// 		messages: [{
// 			message: "test",
// 			timestamp: 1582070042,
//          sendStatus: ...,
//          timeRead: ...,
//          id: ..., (MessageId)
// 			sentByMe: true,
//          "sentPromise": oPromise,
// 		},]
// 	},
// }

import {createOnlineStore} from 'store/onlineStore.js';
import {cSendStatus} from 'ui_dyn/chat/ui/ChatMessage.svelte';
import {get} from 'svelte/store';
import {websocket} from 'js/websocket.js';

function createChatStore(){
    let convertChatMessage = oChatMessage=>({
        ...oChatMessage,
        sendStatus: oChatMessage.timeRead!=null?cSendStatus.read:cSendStatus.onServer,
        timeRead: oChatMessage.timeRead!=null?new Date(oChatMessage.timeRead):null,
        id: oChatMessage.messageId,
    });

    function mergeMessages(chatServer, chatLocal){
        let chatTotal = {};
        Object.keys(chatServer).forEach(sChatId=>{
            chatTotal[sChatId] = {
                ...chatServer[sChatId],
                messages: chatServer[sChatId].messages.map(convertChatMessage),
            };
        });

        Object.keys(chatLocal).forEach(sChatId=>{
            if(sChatId in chatLocal){
                //first, Messages on Server and Local,
                //then messages Local (still not submitted to server)
                //then new server messages

                //find last same element
                let cSMessages = chatServer[sChatId].messages;
                let cLMessages = chatLocal[sChatId].messages;
                let iSM=cSMessages.length-1;
                let iLM=cLMessages.length-1;
                while (iSM>=0 && iLM >= 0){
                    if(cSMessages[iSM].timestamp > cLMessages[iLM].timestamp){
                        iSM--;
                        continue;
                    }
                    if (cSMessages[iSM].timestamp < cLMessages[iLM].timestamp){
                        iLM--;
                        continue;
                    }
                    if(cSMessages[iSM].message === cLMessages[iLM].message && cSMessages[iSM].sentByMe === cLMessages[iLM].sentByMe){
                        break;
                    }
                }
                chatTotal[sChatId].messages.splice(iSM+1, 0, ...cLMessages.slice(iLM+1));
            } else {
                chatTotal[sChatId] = chatLocal[sChatId];
            }
        })
        return chatTotal;
    }

    let onMessageReceivedHandler=()=>{};
    let { set, update, subscribe} =  createOnlineStore('chat', {}, {
        onInit: mergeMessages,
        onUpdate: (oChat, oChatMessage)=>{
            if(!oChat.hasOwnProperty(oChatMessage.userId)) {
                oChat[oChatMessage.userId] = {
                    messages : [],
                };
            }
            oChat[oChatMessage.userId].messages = [...oChat[oChatMessage.userId].messages,convertChatMessage(oChatMessage),];

            onMessageReceivedHandler(oChatMessage);
            return oChat;
        },
        storeKeepAliveOnUnsubscribe: true,
        authStore:true,
    });

    let fUpdateLocalMessagesRead = oIds => update(oChats=>{
        Object.keys(oChats).forEach(sChatId=>oChats[sChatId].messages.forEach(oMessage=>{
            if(oIds.includes(oMessage.id)){
                oMessage.sendStatus = cSendStatus.read;
                oMessage.timeRead = new Date();
            }
        }));
        return oChats;
    })

    websocket.onReceive('chat_markedread', fUpdateLocalMessagesRead);

    return {
        set,
        update,
        subscribe,
        setOnMessageReceivedHandler: fCallback=>onMessageReceivedHandler=fCallback,
        markMessagesRead: (sChatId)=>{
            let oChats = get({subscribe});
            let oMessagesToMark = oChats[sChatId].messages.filter(oMessage=>oMessage.sentByMe === false && oMessage.sendStatus === cSendStatus.onServer);
            if(oMessagesToMark.length>0){
                let oIdsRead = oMessagesToMark.map(o=>o.id);
                websocket.send('chat_markread', oIdsRead, {answer:false});
                fUpdateLocalMessagesRead(oIdsRead);
            }
        },
        getUnreadMessagesIds: ()=>{
            /*
            *   Gibt die IDs von den Chatpartnern mit von mir ungelesenen Nachrichten zurück.
            */
            let oIdsUnreadMessages = [];
            let oChats = get({subscribe});
            Object.keys(oChats).forEach(sChatId=>{
                let oChatMessages = oChats[sChatId].messages;
                let i = oChatMessages.length;
                while (i>0) {
                    i--;
                    if(oChatMessages[i].sentByMe === false){
                        if(oChatMessages[i].sendStatus !== cSendStatus.read){
                            oIdsUnreadMessages.push(sChatId);
                        }
                        break;
                    }
                }
            });
            return oIdsUnreadMessages;
        },
    }
}

export const chat = createChatStore();
