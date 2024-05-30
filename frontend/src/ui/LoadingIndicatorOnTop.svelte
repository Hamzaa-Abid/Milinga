<script>
    import FloatCenterOnTop from 'ui/FloatCenterOnTop.svelte';

    export let loading = false;
    export let size = 'big'; //small
</script>

<FloatCenterOnTop>
    <div slot="bg">
        <slot />
    </div>
    <div slot="fg">
        {#if loading===true}
            <div class="spinner-border" class:spinner-border-sm={size=='small'} role="status" />
        {/if}
    </div>
</FloatCenterOnTop>
