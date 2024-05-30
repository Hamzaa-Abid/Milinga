<script>
    import Fa from 'svelte-fa';
    import { faUsers, faWindowMinimize, faComments, faEnvelope } from '@fortawesome/free-solid-svg-icons';

	import { flip } from 'svelte/animate';
	import { quintOut } from 'svelte/easing';

	import ChatContact from 'ui_dyn/chat/ui/ChatContact.svelte';
	import {users} from 'store/users.js';
	import {chat} from 'store/chat.js';

    import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

    let oChatContacts=[];

    $: updateChatContactList($chat);
    
    function updateChatContactList(oChats){
        //Kontakt-Liste erstellen
		var oChatContactsTmp=[];
		let oIdsUnreadMessages = chat.getUnreadMessagesIds();
        for (let chatContactId in oChats) {
			if(oChats[chatContactId].messages.length>0) {
				let oLastMessage = {
					message: '',
					timestamp: 0,
				};
				if (oChats[chatContactId].messages.length > 0) {
					oLastMessage = oChats[chatContactId].messages[oChats[chatContactId].messages.length-1];
				}
				oChatContactsTmp.push({
					"id": chatContactId,
					"lastMessage": oLastMessage.message,
					"lastMessageTimestamp": oLastMessage.timestamp,
					"unreadMessages": (oIdsUnreadMessages.includes(chatContactId)),
				})
			}
        }

        //sortieren nach Message-Datum
        oChatContacts = oChatContactsTmp.sort((a,b)=>{
            return b.lastMessageTimestamp - a.lastMessageTimestamp;
        });
    }
</script>

<style>
	.direct-chat .card-body {
		overflow-x: hidden;
		padding: 0;
		position: relative;
	}

	.direct-chat-contacts {
		transition: -webkit-transform .5s ease-in-out;
		transition: transform .5s ease-in-out;
		transition: transform .5s ease-in-out, -webkit-transform .5s ease-in-out;
		-webkit-transform: translate(0, 0);
		transform: translate(0, 0);
		height: 250px;
		overflow: auto;
		width: 100%;
	}

	.contacts-list {
		padding-left: 0;
		list-style: none;
	}

	li {
		border-bottom: 1px solid rgba(0, 0, 0, 0.2);
		margin: 0;
		padding: 10px;
		cursor: pointer;
	}

	li::after {
		display: block;
		clear: both;
		content: "";
	}

	li:last-of-type {
		border-bottom: 0;
	}

</style>

<div class="card card-danger direct-chat direct-chat-danger">
    <div class="card-header">
        <div class="card-tools d-flex">
            <span>Contacts-List</span>
            <span class="mr-auto"></span>
            <button type="button" class="btn btn-tool" on:click={(event) => {dispatch('minimize')}} title="minimize"><Fa icon={faWindowMinimize} /></button>
        </div>
    </div>
    <div class="card-body">
        <div class="direct-chat-contacts">
            <ul class="contacts-list">
    	        {#each oChatContacts as contact (contact.id)}
					<li animate:flip = {{delay: 0, duration: 1000, easing: quintOut}}>
						<ChatContact
							name = {$users[contact.id].name}
							profilePic = {$users[contact.id].profilePic}
							lastMessage = {contact.lastMessage}
							lastMessageTimestamp = {contact.lastMessageTimestamp}
							unreadMessages = {contact.unreadMessages}
							isOnline = {contact.isOnline}
							on:click={(event) => {dispatch('contactClicked', contact.id)}} />
					</li>
	            {/each}
            </ul>
        </div>
    </div>
</div>