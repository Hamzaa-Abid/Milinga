<style>
    .custom-invalid-feedback {
        color: #FA5051;
    }
</style>
<script>
    export let error;
</script>

{#if error != undefined}
    {#if typeof error === 'object'}
        {#each error as _error}
            <div class="custom-invalid-feedback">{_error}</div>
        {/each}
    {:else}
        <div class="custom-invalid-feedback">{error}</div>
    {/if}
{/if}