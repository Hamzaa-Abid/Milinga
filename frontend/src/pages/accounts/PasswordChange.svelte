<script>
    import { navigate } from "svelte-routing";
    import { createEventDispatcher } from 'svelte';
    import { faUserPlus } from '@fortawesome/free-solid-svg-icons';

    import TextField from 'ui/TextField.svelte';
    import CheckBox from 'ui/CheckBox.svelte';
    import Button from 'ui/Button.svelte';
    import Error from 'ui/Error.svelte';

    import {password_change} from 'js/account.js';

    let new_password1, new_password2, old_password;

    let error = {};

    let oPromise;

    function onPasswordChanged(){
        oPromise = password_change({new_password1, new_password2, old_password,});
        oPromise.then(()=>{
            navigate('/', {replace:false});
        }).catch(function(_error) {
            error = _error
        });
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
                <h1 class="text-wrap text-sm-nowrap text-md-nowrap text-lg-nowrap">Passwort ändern</h1>
            </div>

            <div class="mb-3">
                <TextField
                    type='password'
                    label='Aktuelles Passwort'
                    placeholder='Aktuelles Passwort'
                    required={true}
                    bind:value={old_password}
                    error={error.old_password}
                    on:enter={onPasswordChanged} />

                <TextField
                    type='password'
                    label='Neues Passwort'
                    placeholder='Neues Passwort'
                    required={true}
                    bind:value={new_password1}
                    error={error.new_password1}
                    on:enter={onPasswordChanged} />

                <TextField
                    type='password'
                    label='Neues Passwort (Wiederholung)'
                    placeholder='Neues Passwort (Wiederholung)'
                    required={true}
                    bind:value={new_password2}
                    error={error.new_password2}
                    on:enter={onPasswordChanged} />


                <Error error={error.non_field_errors} />
                <Error error={error.connection} />
                <Button on:click={onPasswordChanged} promise={oPromise} icon={faUserPlus} text="Passwort zurücksetzen"/>
            </div>
        </div>
    </div>
</div>