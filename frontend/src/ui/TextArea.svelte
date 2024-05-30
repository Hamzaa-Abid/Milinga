<!--
import TextArea from 'ui/TextArea.svelte';
<TextArea
    label='Short description'
    required={true}
    bind:value={last_name} />
-->

<script>
    export let label;
    export let required=false;
    export let value;
    export let cols=40;
    export let rows=4;
</script>

<style>
</style>


<div class="mb-3">
    <label class:requiredField={required}>
        {label}{#if required}<span class="asteriskField">*</span>{/if}
    </label>
    <textarea
        class="textarea form-control"
        {cols}
        {rows}
        {required}
        bind:value />
</div>