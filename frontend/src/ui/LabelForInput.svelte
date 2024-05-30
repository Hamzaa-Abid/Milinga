<script>
    export let label;
    export let required;
</script>

<div class="mb-3">
    <label class:requiredField={required}>
        {label}{#if required}<span class="asteriskField">*</span>{/if}
    </label>
    <slot/>
</div>