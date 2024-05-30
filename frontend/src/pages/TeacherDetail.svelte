<script>
    import { createEventDispatcher } from 'svelte';
    import Fa from 'svelte-fa';
    import { faComment } from '@fortawesome/free-solid-svg-icons';

    import Button from 'ui/Button.svelte';
    import CalStudentBookTeacher from 'ui_dyn/calendar/CalStudentBookTeacher.svelte';
    import Teacher from 'ui/Teacher.svelte';

    import {users} from 'store/users.js';
    import {creditsTotal} from 'store/creditsTotal.js';

	const dispatch = createEventDispatcher();

    export let teacherId;

</script>

<style>
</style>

<div class="container align-items-center justify-content-center my-4">
    <Teacher {...$users[teacherId]} />

    <div class="d-flex mx-2 my-2 justify-content-center">
        <h1>Your credits with teacher:</h1>
        <span class={`badge badge-${$creditsTotal.myCredits[teacherId]<0?'danger':'success'} badge-pill d-flex align-self-center`} style="font-size:1.4rem">{$creditsTotal.myCredits[teacherId] || 0}</span>
    </div>

    <CalStudentBookTeacher {teacherId} />

    <Button
        on:click={()=>{dispatch('openchat', {userId : teacherId})}}
        icon={faComment}
        text="Chat" />
</div>