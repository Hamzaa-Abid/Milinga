<!--
import CheckBox from 'ui/CheckBox.svelte';

<CheckBox
    label='Angemeldet bleiben'
    bind:value={stayLoggedIn} />
-->

<script>
    import {createEventDispatcher} from 'svelte';

    export let label;
    export let value=false;

    const dispatch = createEventDispatcher();

    function onKeyDown(e){
        if(e.key === "Enter"){
            dispatch('enter');
            e.preventDefault();
        }
    }
</script>

<style>
    .pointer {
        cursor: pointer;
    }
</style>

<div class="mb-3 pointer">
    <div class="form-check pointer">
        <input type="checkbox" class="checkboxinput form-check-input pointer"
        checked={value}
        id="id_field"
        on:input={(event)=>{value=event.target.checked}}
        on:keydown={onKeyDown} />
        <label for="id_field" class="form-check-label pointer">
            {label}
        </label>
    </div>
</div>



