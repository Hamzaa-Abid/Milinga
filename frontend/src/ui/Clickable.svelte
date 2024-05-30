<!--
import Clickable from 'ui/Clickable.svelte';

<Clickable on:click={}>...</Clickable>
-->

<style>
div {
    cursor: pointer;
}
</style>

<script>
    import Tooltip from 'ui/Tooltip.svelte';

    export let tooltip=undefined;
    export let tooltipPlacement='top';
</script>

<!-- <div on:click|stopPropagation> -->
<div on:click>
    {#if tooltip != undefined}
        <Tooltip text={tooltip} placement={tooltipPlacement}>
            <slot/>
        </Tooltip>
    {:else}
        <slot/>
    {/if}
</div>
