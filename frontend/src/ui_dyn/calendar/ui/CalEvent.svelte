<script>
    import {users} from 'store/users.js';
    import {userMe} from 'js/account.js';

    import LoadingIndicatorOnTop from 'ui/LoadingIndicatorOnTop.svelte';

    // Parameters: https://fullcalendar.io/docs/eventRender
    export let event,   //Event Object - https://fullcalendar.io/docs/event-object
        isMirror,
        isStart,        //true if the element being rendered is the starting slice of the event’s range. false otherwise.
        isEnd,          //true if the element being rendered is the ending slice of the event’s range. false otherwise.
        view;

    let sUserId;
    if(event.extendedProps.studentId === $userMe.id){
        sUserId = event.extendedProps.teacherId;
    } else {
        sUserId = event.extendedProps.studentId;
    }
    $: oUser = sUserId!=undefined?$users[sUserId]:{};
</script>

<style>
	img {
		border-radius: 90%;
		width: 35px;
		height: 35px;
	}
    span { 
        display:block;
        width:60%;
        word-wrap:break-word;
    }
    .loading {
        opacity: 0.4;
    }
</style>

{#if !isMirror && event.rendering != 'background'}
    <LoadingIndicatorOnTop size="small" loading={!!event.extendedProps.loading}>
        <div class="fc-content" class:loading={!!(event.extendedProps.loading)}>
            <div class="d-flex">
                <img src={oUser.profilePic} alt="profilePic">
                <span class="ml-auto">{oUser.name}</span>
            </div>
        </div>
    </LoadingIndicatorOnTop>
{/if}