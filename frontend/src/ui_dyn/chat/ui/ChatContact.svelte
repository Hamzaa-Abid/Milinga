<!-- 
<script context="module">
	export const cOnlineStatus = {
		online: 0,
		away: 1,
		offline:2,
	};
</script>
 -->

<script>
	export let name;
	export let profilePic;
	export let lastMessage;
	export let lastMessageTimestamp;
	export let unreadMessages = false;
	export let isOnline = false;

   /*‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
  | Time formatting */
	const d = new Date(lastMessageTimestamp);
	const now = Date.now();
	const monthsName = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
	let timeString = "";
	if(now - lastMessageTimestamp < 86400000)
		timeString = d.getHours() + ":" + (d.getMinutes()>9?d.getMinutes():"0"+d.getMinutes());
	else
		timeString = monthsName[d.getMonth()] + " " + d.getDate();
/*|                                                                                                            |
   \_________________________________________________________________________________________________________*/
</script>

<style>
	img {
		border-radius: 50%;
		width: 40px;
		height: 40px;
	}

	.contacts-list-info {
		color: #000000;
		margin-left: 45px;
	}

	.contacts-list-name {
		display: block;
		font-weight: 600;
	}

	.contacts-list-date {
		color: #ced4da;
		font-weight: normal;
	}

	.contacts-list-msg {
		display: block;
		color: #b1bbc4;
	}
	
	.highlight-time{
		color: blue
	}
	
	.highlight-msg{
		font-weight: bold
	}
	
	.dot{
		color: blue;
	}
	
	.avatar {
		float: left;
		position: relative;
		/* display: inline; */
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
<div on:click>
	<div class="avatar" class:online={isOnline}>
		<img class="rounded-circle" src={profilePic} alt="pic" />
	</div>

	<div class="contacts-list-info">
		<span class="contacts-list-name">
			{name}
			{#if lastMessageTimestamp > 0}
				<small class="contacts-list-date float-right {unreadMessages?' highlight-time ':' '}">{ timeString }</small>
			{/if}
		</span>
		<span class="contacts-list-msg" class:highlight-msg={unreadMessages}>
			{lastMessage}
			{#if unreadMessages}
				<small class="float-right dot">&#9679; &nbsp;</small>
			{/if}
		</span>
	</div>
</div>