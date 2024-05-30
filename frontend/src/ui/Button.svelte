<!--
import Button from 'ui/Button.svelte';

<Button on:click={onRegister} promise={oPromise} icon={faUserPlus} text="Anmeldung"/>
-->

<script>
    import {createEventDispatcher} from 'svelte'
    import Fa from 'svelte-fa';
    import { faExclamationTriangle } from '@fortawesome/free-solid-svg-icons';

    const dispatch = createEventDispatcher();
    
    export let promise, icon, text, navButton=false;

    function onClick(event){
        event.preventDefault();
        dispatch('click');
    }
</script>

<style>
.btn-blue {
    background-color: #3c8dbc;
    border-color: #367fa9;
}
</style>

<!-- <button class="btn btn-primary my-2 my-sm-0">Click here to resend the eMail!</button> -->
<button class="btn btn-primary" class:btn-blue={!navButton} class:btn-lg={!navButton} class:btn-block={!navButton} on:click={onClick}>
    {#await promise}
        <div class="spinner-border" role="status"></div>
    {:then}
        <Fa icon={icon} />
    {:catch}
        <Fa icon={faExclamationTriangle} color="red" />
    {/await}
    {text}
</button>


