<script>
    import { getContext } from 'svelte';

    const { close } = getContext('simple-modal');

    export let onBook=()=>null;
    export let event;

    function _onBook(){
        onBook();
        close();
    }


</script>

<div class="card text-center">
    <div class="card-header">
        Do you want to book the following lesson?
    </div>
    <div class="card-body">
        <div class="row">
            <div class="col-4">Date:</div>
            <div class="col-8">{event.start.toLocaleDateString()}</div>
        </div>
        <div class="row">
            <div class="col-4">Time:</div>
            <div class="col-8">{event.start.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</div>
        </div>
    </div>
    <div class="card-footer text-muted d-flex">
        <button type="button" class="btn btn-secondary" on:click={close}>Dont book!</button>
        <button type="button" class="btn btn-primary ml-auto" on:click={_onBook}>Book!</button>
    </div>
</div>