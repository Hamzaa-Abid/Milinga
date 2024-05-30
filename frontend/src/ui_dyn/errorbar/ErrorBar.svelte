<script>
    import { getContext } from 'svelte';
    const { open } = getContext('simple-modal');

    import {userMe} from 'js/account.js';
    import {ajax} from 'js/ajax.js';

    import Button from 'ui/Button.svelte';
    import ModalResendVerifyEmail from './ModalResendVerifyEmail.svelte';

    $: bEMailToVerify = $userMe.emailVerified===false;

    let oResendVerifEmailPromise;

    let bVerifEMailSent = false;
    function onResendVerifyEMail(){
        open(ModalResendVerifyEmail, {
            onResendVerifyEMail: ()=>{
                oResendVerifEmailPromise = ajax('/rest-auth/resend-verification-email/', {
                    'email': $userMe.email,
                }, {
                    sendToken: false,
                });
                oResendVerifEmailPromise.then(()=>bVerifEMailSent=true).catch();
            },
        });

    }
</script>

<!-- {#if errors.length>0} -->
{#if bEMailToVerify===true}
    <nav class="navbar navbar-light" style="background-color: #ff0000;">
        <div class="navbar-expand">
            <ul class="navbar-nav">
                {#if bEMailToVerify}
                    <li class="nav-item">
                        Please verify your eMail-Address to have full access to this website!
                        <Button text={!bVerifEMailSent?"Click here to resend the verification email!":"Verification email sent! Refresh this page, if you verified your eMail!"} on:click={onResendVerifyEMail} promise={oResendVerifEmailPromise} navButton/>
                        <!-- <button class="btn btn-primary my-2 my-sm-0">Click here to resend the eMail!</button> -->
                    </li>
                {/if}
            </ul>
        </div>
    </nav>
{/if}