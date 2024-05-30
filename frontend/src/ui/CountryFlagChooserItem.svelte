<script>
    import CountryFlag from 'ui/CountryFlag.svelte';

    export let item = undefined;

    export let isFirst=undefined;
    export let isActive=undefined;
    export let isHover=undefined;
    export let filterText=undefined;
</script>

<style>
    div {
        display: flex;
        align-items: center;
        white-space: nowrap;
    }
</style>

<div>
    <CountryFlag flag={item.key}/> <span style="vertical-align:middle;margin-left:5px;">{item.value}</span>
</div>
