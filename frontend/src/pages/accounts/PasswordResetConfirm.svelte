<script>
    import { navigate } from "svelte-routing";
    import { createEventDispatcher } from 'svelte';
    import { faUserPlus } from '@fortawesome/free-solid-svg-icons';

    import TextField from 'ui/TextField.svelte';
    import CheckBox from 'ui/CheckBox.svelte';
    import Button from 'ui/Button.svelte';
    import Error from 'ui/Error.svelte';
    import Link from 'ui/Link.svelte';

    import {password_reset_confirm, userMe} from 'js/account.js';

    export let uid, token;
    let new_password1, new_password2;

    let error = {};

    let oPromise;

    function onPasswordResetConfirm(){
        oPromise = password_reset_confirm({uid, token, new_password1, new_password2,});
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
                <h1 class="text-wrap text-sm-nowrap text-md-nowrap text-lg-nowrap">
                    {#if error.token == "Invalid value"}
                        Falsches Token
                    {:else}
                        Passwort ändern
                    {/if}
                </h1>
            </div>

            {#if error.token == "Invalid value"}
                 <p>Der Link zum Zurücksetzen des Passworts war ungültig, womöglich wurde dieser Link bereits benutzt. Bitte lass dein Passwort noch mal <Link to="/passwordreset/" blue>zurücksetzen</Link>.</p>
            {:else}
                <div class="mb-3">
                    <TextField
                        type='password'
                        label='Neues Passwort'
                        placeholder='Neues Passwort'
                        required={true}
                        bind:value={new_password1}
                        error={error.new_password1}
                        on:enter={onPasswordResetConfirm} />

                    <TextField
                        type='password'
                        label='Neues Passwort (Wiederholung)'
                        placeholder='Neues Passwort (Wiederholung)'
                        required={true}
                        bind:value={new_password2}
                        error={error.new_password2}
                        on:enter={onPasswordResetConfirm} />

                    <Error error={error.non_field_errors} />
                    <Error error={error.connection} />
                    <Button on:click={onPasswordResetConfirm} promise={oPromise} icon={faUserPlus} text="Passwort ändern"/>
                </div>
            {/if}
        </div>
    </div>
</div>