<script>
    import Fa from 'svelte-fa';
    import { faUsers, faCompressArrowsAlt, faComments, faEnvelope } from '@fortawesome/free-solid-svg-icons';

	import { flip } from 'svelte/animate';
    import { quintOut } from 'svelte/easing';
    
    import ChatOnePerson from 'ui_dyn/chat/ui/ChatOnePerson.svelte';
	import ChatContacts from 'ui_dyn/chat/ui/ChatContacts.svelte';
	import {cSendStatus} from 'ui_dyn/chat/ui/ChatMessage.svelte';
	import ChatIcon from 'ui_dyn/chat/ui/ChatIcon.svelte';

    import {websocket} from 'js/websocket.js';
	import {users} from 'store/users.js';
	import {chat} from 'store/chat.js';
	import {userMe} from 'js/account.js';
	
    let iActiveChat=null;
    let bContactsOpen=false;
	let bShowChat=false;
	let bUnreadMessage=false;

	export const openChat = (sUserId)=>{
		if(! (sUserId in $chat)) {
			$chat[sUserId] = {
				messages : [],
			}
		}
		iActiveChat = sUserId;
		bContactsOpen = false;
		bShowChat = true;
		
   /*‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
  | Überprüfen, ob es noch andere ungelesene Nachrichten gibt, ausser im aktuellen Chat.
  | Wenn ja -> Anzeige! */
		let oIdsUnreadMessages = chat.getUnreadMessagesIds();
		let iChatsWithUnreadMessages = oIdsUnreadMessages.length;
		if(oIdsUnreadMessages.includes(sUserId)){
			iChatsWithUnreadMessages--;
		}
		bUnreadMessage = iChatsWithUnreadMessages>0;
	};
/*|                                                                                                            |
   \_________________________________________________________________________________________________________*/

	let audio_message;

    function sendMessage(event){
		let sMessage = event.detail;
		let _sChatId = iActiveChat;
		let sRandId = Math.random();

		let oPromise = websocket.send('chat_sendmsg', {
			to: _sChatId,
			msg: sMessage,
		});

		let timestampNow = new Date().getTime();
        $chat[_sChatId].messages = [...$chat[_sChatId].messages, {
            "message": sMessage,
            'timestamp': timestampNow,
			"sentByMe": true,
			"sendStatus": cSendStatus.notSent,
			"id": sRandId,
        }]
        $chat[_sChatId].lastMessage = sMessage;
        $chat[_sChatId].lastMessageTimestamp = timestampNow;

		oPromise.then(sId=>{
			let i = $chat[_sChatId].messages.findIndex(o=>o.id === sRandId);
			$chat[_sChatId].messages[i].id = sId;
			$chat[_sChatId].messages[i].sendStatus = cSendStatus.onServer;
		});
	}
	
	chat.setOnMessageReceivedHandler((oChatMessage)=>{
		if(oChatMessage.sentByMe === false){
			audio_message.currentTime = 0;
			audio_message.play();

			if(bShowChat==false) {
				openChat(oChatMessage.userId);
			} else {
				if(oChatMessage.userId != iActiveChat) {
					bUnreadMessage = true;
				}
			}

			markMessagesReadOnFocus();
		}
	})

	// websocket.onReceive('chat', function(oChatMessage){ //Message empfangen
    //     if(oChatMessage.sentByMe === false){
    //         audio_message.currentTime = 0;
    //         audio_message.play();
	// 	}
	// 	if(!$chat.hasOwnProperty(oChatMessage.id)) {
	// 		$chat[oChatMessage.id] = {
	// 			messages : [],
	// 		};
	// 	}
	// 	$chat[oChatMessage.id].messages = [...$chat[oChatMessage.id].messages,{
	// 		message: oChatMessage.message,
	// 		timestamp: oChatMessage.timestamp,
	// 		sentByMe: oChatMessage.sentByMe,
	// 	}];

    //     if(bShowChat===false){
    //         iActiveChat = oChatMessage.id;
	// 		bContactsOpen = false;
	// 		bShowChat = true;
    //     }
    // })

	$: bShowChat, $chat.length, function(){
		if(iActiveChat === null && bShowChat===true){
			for (var chatContactId in $chat) {
				iActiveChat = chatContactId;
				break;
			}
		}
	}()

	// Messages als gelesen markieren, wenn Fenster lang genug Focus hat und Chat aktiv
	import {onFocusTime} from 'js/focus.js';
	$: if(iActiveChat !== null) markMessagesReadOnFocus();

	let focusTimeStop=()=>{};
	function markMessagesReadOnFocus(){
		focusTimeStop();
		if(iActiveChat === null) return;
		focusTimeStop = onFocusTime(1000, function(){
			chat.markMessagesRead(iActiveChat);
		});
	}

	let bNewMessages=false;
</script>


<style>
	.chat-container {
		position: -webkit-fixed; /* Safari */
		position: fixed;
		bottom: 0;
		right: 0;
		z-index:999;
	}
	.chat-container-icon {
		bottom: 10px;
		right: 10px;
	}
	.chat-container-big {
		width: 380px;
		max-width: 100%;
		max-height: 100%;
	}
</style>

{#if Object.keys($chat).length > 0 && $userMe.emailVerified}
		{#if bShowChat == false}
			<div class="chat-container chat-container-icon d-flex justify-content-end">
				<!-- <button type="button" class="btn btn-tool" on:click={(event) => {bShowChat=true}} title="open chat"> -->
					<!-- <img src="{document.body.dataset.staticurl}img/chaticon18.gif" width="50" height="50" class="d-inline-block align-top" alt=""/>
					<img src="{document.body.dataset.staticurl}img/chaticon20.gif" width="50" height="50" class="d-inline-block align-top" alt=""/>
					<img src="{document.body.dataset.staticurl}img/chaticon.gif" width="50" height="50" class="d-inline-block align-top" alt=""/> -->
				<ChatIcon animate={bNewMessages}  on:click={(event) => {bShowChat=true}}/>
				<!-- </button> -->
			</div>
		{:else}
			<div class="chat-container chat-container-big">
				{#if bContactsOpen === false}
					<ChatOnePerson
						idChatPartner={iActiveChat}
						nameMe={$userMe.name}
						nameChatPartner={$users[iActiveChat].name}
						profilePicMe={$userMe.profilePic}
						profilePicChatPartner={$users[iActiveChat].profilePic}
						messages={$chat[iActiveChat].messages}
						showUnreadMessageAlert={bUnreadMessage}
						on:showContacts={(event)=>{bContactsOpen=true}}
						on:minimize={(event)=>{bShowChat=false}}
						on:sendMessage={sendMessage}
						on:contactClicked />
				{:else}
					<ChatContacts
						on:minimize={(event)=>{bShowChat=false}}
						on:contactClicked={(event)=>{openChat(event.detail)}} />
				{/if}
			</div>
	{/if}
{/if}

<audio bind:this={audio_message} src={document.body.dataset.staticurl + "sounds/incoming_message.wav"} />