<!-- 
import ChatMessage, {sendStatus} from 'ui_dyn/chat/ui/ChatMessage.svelte';
<ChatMessage
	sentByMe = {message.sentByMe}
	nameChatPartner = {nameChatPartner}
	profilePicChatPartner = {profilePicChatPartner}
	nameMe = {nameMe}
	profilePicMe = {profilePicMe}
	message = {message.message}
	sendStatus = {status.notSent}
	timestamp = {message.timestamp} />
 -->
<script context="module">
	export const cSendStatus = {
		notSent: 0,
		onServer: 1,
		read:2,
	};
</script>

<script>
	import Fa from 'svelte-fa';
	import { faCheck, faCheckDouble } from '@fortawesome/free-solid-svg-icons';

	import Tooltip from 'ui/Tooltip.svelte';

    export let sentByMe;
    export let nameChatPartner;
    export let profilePicChatPartner;
    export let nameMe;
    export let profilePicMe;
	export let message;
	export let sendStatus = cSendStatus.notSent;
	export let timeRead;
    export let timestamp;
</script>

<style>
.direct-chat-msg,
.direct-chat-text {
	display: block;
}
.direct-chat-msg {
	margin-bottom: 10px;
}
.direct-chat-msg:before,
.direct-chat-msg:after {
	content: " ";
	display: table;
}
.direct-chat-msg:after {
	clear: both;
}
.direct-chat-text {
	border-radius: 5px;
	position: relative;
	padding: 5px 10px;
	background: #d2d6de;
	border: 1px solid #d2d6de;
	margin: 5px 0 0 50px;
	color: #444;
}
.direct-chat-text:after,
.direct-chat-text:before {
	position: absolute;
	right: 100%;
	top: 15px;
	border: solid transparent;
	border-right-color: #d2d6de;
	content: ' ';
	height: 0;
	width: 0;
	pointer-events: none;
}
.direct-chat-text:after {
	border-width: 5px;
	margin-top: -5px;
}
.direct-chat-text:before {
	border-width: 6px;
	margin-top: -6px;
}
.right .direct-chat-text {
	margin-right: 50px;
	margin-left: 0;
}
.right .direct-chat-text:after,
.right .direct-chat-text:before {
	right: auto;
	left: 100%;
	border-right-color: transparent;
	border-left-color: #d2d6de;
}
img {
	border-radius: 50%;
	float: left;
	width: 40px;
	height: 40px;
}
.right img {
	float: right;
}
.direct-chat-name {
	font-weight: 600;
}
.direct-chat-timestamp {
	color: #999;
}
</style>

<div class="direct-chat-msg" class:right="{sentByMe}" class:left="{!sentByMe}">
    <div class="direct-chat-infos clearfix">
        <span class="direct-chat-name" class:float-right="{sentByMe}" class:float-left="{!sentByMe}">{sentByMe==true?nameMe:nameChatPartner}</span>
        <span class="direct-chat-timestamp" class:float-left={sentByMe} class:float-right={!sentByMe}>{new Date(timestamp).toLocaleString([], { hour: '2-digit', minute:'2-digit', hour12: false})}</span>
    </div>
    <img class="direct-chat-img" src="{sentByMe==true?profilePicMe:profilePicChatPartner}" alt="pic">
    <div class="direct-chat-text">
		<div class="d-flex">
			<span class="mr-auto">{message}</span>
			{#if sentByMe === true}
			<div class="mt-auto">
				{#if sendStatus === cSendStatus.notSent}
					<!-- <SvelteTooltip tip={"sending..."} color="#EEEEEE" left > -->
					<Tooltip text="sending..." placement="bottom-start">
						<div class="spinner-border spinner-border-sm"></div>
					</Tooltip>
					<!-- </SvelteTooltip> -->
				{:else if sendStatus === cSendStatus.onServer}
					<!-- <SvelteTooltip tip={"saved on server, not read"} color="#EEEEEE" left > -->
					<Tooltip text="saved on server, not read" placement="bottom-start">
						<Fa icon={faCheck} />
					</Tooltip>
					<!-- </SvelteTooltip> -->
				{:else if sendStatus === cSendStatus.read}
					<!-- <div style="color:#ffffff"> -->
					<!-- <SvelteTooltip tip={`Read on ${timeRead.toLocaleString()}`} color="#EEEEEE" left > -->
					<Tooltip text={`Read on ${timeRead.toLocaleString()}`} placement="bottom-start">
						<Fa icon={faCheckDouble} />
					</Tooltip>
					<!-- </SvelteTooltip> -->
					<!-- </div> -->
					<!-- <Tooltip text={`Read on ${timeRead.toLocaleString()}`}><Fa icon={faCheckDouble} /></Tooltip> -->
				{/if}
			</div>
			{/if}
		</div>
	</div>
</div>