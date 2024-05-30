<script>
	import ChatMessage from 'ui_dyn/chat/ui/ChatMessage.svelte';
	import ContactsIcon from 'ui_dyn/chat/ui/ContactsIcon.svelte';
	import { createEventDispatcher } from 'svelte';
	import Fa from 'svelte-fa';
	import { faWindowMinimize, faComments, faEnvelope } from '@fortawesome/free-solid-svg-icons';
	import Clickable from 'ui/Clickable.svelte';

	import { tick } from 'svelte';

	const dispatch = createEventDispatcher();

	export let nameMe;
	export let profilePicMe;

	export let nameChatPartner;
	export let profilePicChatPartner;

	export let idChatPartner;

	export let isOnline = false;
	
	export let messages;
	export let showUnreadMessageAlert=false;
	

	let wChatWindow;
	let input_field;

	$: messages, scrollChatDown();
	$: nameChatPartner, focusInputField();

	function scrollChatDown(){
		tick().then(()=>{
			wChatWindow.scrollTo(0, wChatWindow.scrollHeight);
		})
	};

	let sMessage='';

	function sendMessage(){
		let sMessageTrim = sMessage.trim();
		sMessage="";
		focusInputField();
		if (sMessageTrim.length === 0) return;

		dispatch('sendMessage', sMessageTrim);
	}

	function onContactClicked(){
		dispatch('contactClicked', idChatPartner)
	}

	function focusInputField(){
		tick().then(()=>{input_field.focus();});
	}

	focusInputField();
	
	
   /*‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
  | Date Divider */
	$: messages, updateDividers();

	let currentMsgDate, previousMsgDate = -100;
	const today = new Date().getDate();
	let dividers = [];
	
	function updateDividers(){
		for(let i = dividers.length; i<messages.length; i++){
			let d = new Date(messages[i].timestamp)
			currentMsgDate = d.getDate();
			if(currentMsgDate != previousMsgDate){
				let obj = {};
				if(currentMsgDate == today)
					obj.date = "Today"
				else
					obj.date = d.toLocaleDateString()
				dividers.push(obj);
			}
			else{
				dividers.push(0);
			}
			previousMsgDate = currentMsgDate;
		}
	}
/*|                                                                                                            |
   \_________________________________________________________________________________________________________*/
</script>

<style>
	.direct-chat .card-body {
		overflow-x: hidden;
		padding: 0;
		position: relative;
	}

	.direct-chat-messages {
		-webkit-transform: translate(0, 0);
		transform: translate(0, 0);
		height: 250px;
		overflow: auto;
		padding: 10px;
		transition: -webkit-transform .5s ease-in-out;
		transition: transform .5s ease-in-out;
		transition: transform .5s ease-in-out, -webkit-transform .5s ease-in-out;
	}

	.contacts-img {
		border-radius: 50%;
		width: 40px;
		height: 40px;
	}
	.contacts-name {
		margin-left: 15px;
		font-weight: 600;
	}
	
	.date-divider {
		display: flex; 
    flex-direction: row; 
	}
	.date-divider:before, 
	.date-divider:after { 
		content: ""; 
		flex: 1 1; 
		border-bottom: 1px solid #ccc; 
		margin: auto; 
	} 
	
	.avatar {
		position: relative;
		display: inline;
	}
	.avatar:before {
		content: '';
		position: absolute;
		bottom: 0;
		right: 1px;
		width: 10px;
		height: 10px;
		border-radius: 100%;
	}
	.avatar.online:before {
		background-color: lime;
	}
</style>

<div class="card card-danger direct-chat direct-chat-danger">
    <div class="card-header">
        <div class="card-tools d-flex">
			<Clickable on:click={onContactClicked}>
				<div class="avatar" class:online={isOnline}>
					<img class="contacts-img" src={profilePicChatPartner} alt="profilePic" />
				</div>
				<span class="contacts-name">{nameChatPartner}</span>
			</Clickable>
            <span class="mr-auto"></span>
            <button type="button" class="btn btn-tool" title="Contacts" on:click={() => dispatch('showContacts')}><ContactsIcon animate={showUnreadMessageAlert} /></button>
            <button type="button" class="btn btn-tool" on:click={(event) => {dispatch('minimize')}} title="minimize"><Fa icon={faWindowMinimize} /></button>
        </div>
    </div>
    <div class="card-body">
        <div class="direct-chat-messages" bind:this={wChatWindow}>
            {#each messages as message,i}
				{#if dividers[i] != 0}
					<h6 class="date-divider"><span style="padding:10px">{dividers[i].date}</span></h6> 
				{/if}
                <ChatMessage
                    nameMe = {nameMe}
                    profilePicMe = {profilePicMe}
                    nameChatPartner = {nameChatPartner}
                    profilePicChatPartner = {profilePicChatPartner}
					{...message} />					
            {/each}
        </div>
    </div>
    <div class="card-footer">
        <div class="input-group">
            <input bind:this={input_field} type="text" placeholder="Type Message ..." class="form-control" on:keydown={(event) => {if (event.key === 'Enter') sendMessage(); }} bind:value={sMessage}>
            <span class="input-group-append">
                <button type="button" class="btn btn-primary" on:click={sendMessage}>Send</button>
            </span>
        </div>
    </div>
</div>