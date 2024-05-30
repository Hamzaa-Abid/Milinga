<script>
    import { navigate } from "svelte-routing";
    import { createEventDispatcher } from 'svelte';
    import { faUserPlus } from '@fortawesome/free-solid-svg-icons';

    import TextField from 'ui/TextField.svelte';
    import CheckBox from 'ui/CheckBox.svelte';
    import Button from 'ui/Button.svelte';
    import Error from 'ui/Error.svelte';

    import {password_reset, userMe} from 'js/account.js';

    let email;

    let error = {};

    let oPromise;
    let bPasswordSent = false;

    function onPasswordReset(){
        oPromise = password_reset({email,});
        oPromise.then(()=>{
            bPasswordSent = true;
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
                <h1 class="text-wrap text-sm-nowrap text-md-nowrap text-lg-nowrap">Passwort zurücksetzen</h1>
            </div>

            {#if 'id' in $userMe}
                <p><strong>Anmerkung:</strong> Du bist bereits als {$userMe.email} angemeldet.</p>
            {/if}

            {#if bPasswordSent === true}
                <p>Wir haben Dir eine E-Mail geschickt. Bitte kontaktiere uns, wenn du sie nicht in ein paar Minuten erhalten hast.</p>
            {:else}
                <p>Passwort vergessen? Gib deine E-Mail-Adresse unten ein, dann schicken wir dir einen Link, unter dem du dein Passwort zurücksetzen kannst.</p>

                <div class="mb-3">
                    <TextField
                        type='email'
                        label='E-Mail'
                        placeholder='E-Mail-Adresse'
                        required={true}
                        bind:value={email}
                        error={error.email}
                        on:enter={onPasswordReset} />

                    <Error error={error.non_field_errors} />
                    <Error error={error.connection} />
                    <Button on:click={onPasswordReset} promise={oPromise} icon={faUserPlus} text="Passwort zurücksetzen"/>
                </div>

                <p>Bitte kontaktiere uns, wenn das Zurücksetzen des Passworts nicht klappt.</p>
            {/if}
        </div>
    </div>
</div>