<script>
    import { getContext } from 'svelte';

    const { close } = getContext('simple-modal');

    export let onAccept=()=>null;
    export let onReject=()=>null;
    export let event;

    function _onAccept(){
        onAccept();
        close();
    }

    function _onReject(){
        onReject();
        close();
    }
</script>

<div class="card text-center">
    <div class="card-header">
        Do you want to accept this booking?
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
        <button type="button" class="btn btn-secondary" on:click={_onReject}>Reject!</button>
        <button type="button" class="btn btn-primary ml-auto" on:click={_onAccept}>Accept!</button>
    </div>
</div>