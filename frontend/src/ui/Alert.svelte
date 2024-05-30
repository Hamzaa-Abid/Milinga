<!-- 
import Alert from 'ui/Alert.svelte';

<Alert type="success" show={true} closable={true} autoClose={false}>Profil wurde aktualisiert!</Alert>
<Alert type="error" show={true} closable={true} autoClose={true}>Fehler!</Alert>
 -->

<script>
    import Slide from 'ui/transitions/Slide.svelte';

    export let type='success';
    export let closable=false;
    export let show=false;
    export let autoClose=false;

    let color=type;

    $: type, function(){
        color = 'alert-'+type;
        if(type === 'error') {
            color = 'alert-danger';
        }
    }()

    let timeout;
    $: show, function(){
        if(autoClose===true && show===true){
            timeout = setTimeout(function(){
                show=false;
            }, 10000);
        } else if (timeout){
            clearTimeout(timeout);
        }
    }()

    if(autoClose===true){
        closable=true;
    }
</script>

<Slide {show}>
    <div class={`alert alert-dismissible fade show ${color}`} role="alert">
        <slot/>
        {#if closable===true}
            <button on:click={()=>show=false} type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        {/if}
    </div>
</Slide>
