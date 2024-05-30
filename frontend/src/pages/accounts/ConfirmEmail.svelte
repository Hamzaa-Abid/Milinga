<script>
    // import { navigate } from "svelte-routing";
    // import { createEventDispatcher } from 'svelte';

    // import TextField from 'ui/TextField.svelte';
    // import CheckBox from 'ui/CheckBox.svelte';
    // import Button from 'ui/Button.svelte';
    // import Error from 'ui/Error.svelte';
    import Link from 'ui/Link.svelte';

    // // import {websocket} from 'js/websocket.js';
    // // import {preferences} from 'store/preferences.js';
    // // import {users} from 'store/users.js';
    import {confirm_email} from 'js/account.js';

    // // const dispatch = createEventDispatcher();
    
    // let eMail, password, rememberMe;

    // eMail='masrlinu+milinga@gmail.com';
    // password='crashdown';

    // let error = {};

    // function onLogin(){
    //     login({
    //         email: eMail,
    //         password: password,
    //         rememberMe: rememberMe,
    //     }).then(()=>{
    //         // dispatch('loggedIn');
    //         navigate('/', {replace:false});
    //     }).catch(function(_error) {
    //         error = _error
    //     });
    // }

    export let key;

    const status = {
        confirming: 1,
        confirmed: 2,
        error: 3,
    }
    let eMailConfirmed = status.confirming;
    let error={};

    confirm_email({
        key: key,
    }).then((a)=>{
        eMailConfirmed = status.confirmed;
    }).catch(_error=>{
        error = _error.detail;
        eMailConfirmed = status.error;
    });

    let eMailConfirmedText='';
    $: switch(eMailConfirmed){
        case status.confirming:
            eMailConfirmedText = 'eMail confirming...';
            break;
        case status.confirmed:
            eMailConfirmedText = 'eMail confirmed';
            break;
        case status.error:
            eMailConfirmedText = 'eMail not confirmed';
            break;
    }
</script>

<style>
.page-header {
    margin: 10px 0 20px 0;
    font-size: 22px;
}
</style>

<div class="container align-items-center justify-content-center my-4">
    <div class="row">
        <div class="col-lg-4 offset-lg-4 col-md-6 offset-md-3 col-sm-8 offset-sm-2 col-12">
            <div class="page-header">
                <h1 class="text-wrap text-sm-nowrap text-md-nowrap text-lg-nowrap">{eMailConfirmedText}</h1>
            </div>

            {#if eMailConfirmed === status.confirmed}
                <!-- Now you can <Link to='/profile/' blue>edit your profile!</Link> -->
            {:else if eMailConfirmed === status.error}
                Error: {error}
            {/if}
        </div>
    </div>
</div>