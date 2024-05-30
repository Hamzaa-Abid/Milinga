<script>
    import { getContext } from 'svelte';

    import {users} from 'store/users.js';

    import Contact from 'ui/Contact.svelte';

    const { close } = getContext('simple-modal');

    export let event;

    $: oTeacher = $users[event.extendedProps.teacherId];
</script>

<div class="card text-center">
    <div class="card-header">
        Lesson-Info
    </div>
    <div class="card-body d-flex flex-row">
        <img src={oTeacher.profilePic} alt="profile pic" />
        <div class="d-flex flex-column ml-auto mr-auto">
            <h3>{oTeacher.name}</h3>
            <div class="mt-auto mb-auto">
                <div class="row">
                    <div class="col-4">Date:</div>
                    <div class="col-8">{event.start.toLocaleDateString()}</div>
                </div>
                <div class="row">
                    <div class="col-4">Time:</div>
                    <div class="col-8">{event.start.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</div>
                </div>
            </div>
        </div>
    </div>
    <!-- <div class="card-footer text-muted d-flex">
        <button type="button" class="btn btn-secondary" on:click={_onReject}>Reject!</button>
        <button type="button" class="btn btn-primary ml-auto" on:click={_onAccept}>Accept!</button>
    </div> -->
</div>