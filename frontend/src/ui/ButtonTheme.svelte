<!--
import Button from 'ui/Button.svelte';

<Button on:click={onRegister} promise={oPromise} icon={faUserPlus} text="Anmeldung"/>
-->

<script>
    import {createEventDispatcher} from 'svelte'
    import Fa from 'svelte-fa';
    import { faExclamationTriangle } from '@fortawesome/free-solid-svg-icons';

    const dispatch = createEventDispatcher();
    
    export let promise, icon, text, fullWidth,buttonType = 'button';

    function onClick(event){
        event.preventDefault();
        dispatch('click');
    }
</script>

<style>
.theme-btn {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  border: none;
  display: inline-block;
  color: #ffffff;
  border-radius: 8px;
  padding: 0 3.75rem;
  font-size: 16px;
  background-color: #FF792E;
  height: 49px;
  line-height: 49px;
  position: relative;
  text-transform: capitalize;
}

.theme-btn:before {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  content: '';
  display: block;
  height: 30px;
  width: 75%;
  position: absolute;
  box-shadow: 0 12px 45px #FF792E;
  left: 0;
  right: 0;
  margin: auto;
  top: 13px;
}

.theme-btn:hover:before,
.theme-btn:focus:before {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  box-shadow: 0 12px 45px #FAB705;
}

.theme-btn:hover,
.theme-btn:focus {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  background-color: #FAB705;
  color: #fff;
}
</style>

<!-- <button class="btn btn-primary my-2 my-sm-0">Click here to resend the eMail!</button> -->
<button class="btn theme-btn mt-3" class:w-100={fullWidth} on:click={onClick} type={buttonType}>
    {#await promise}
        <div class="spinner-border" role="status"></div>
    {:then}
        <Fa icon={icon} />
    {:catch}
        <Fa icon={faExclamationTriangle} color="red" />
    {/await}
    {text}
</button>


