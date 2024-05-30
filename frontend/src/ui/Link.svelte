<!--
import Link from 'ui/Link.svelte';

<Link to="/">...</Link>
-->

<script>
    import { navigate, Link } from "svelte-routing";
    import Clickable from 'ui/Clickable.svelte';

    export let to;
    export let blue;

    function onClick(){
        navigate(to, { replace: false });
    }
</script>

{#if blue}
    <Link {to} replace={false}>
        <slot />
    </Link>
{:else}
    <Clickable on:click={onClick}>
        <slot />
    </Clickable>
{/if}

<!--
<script>
    import { navigate } from "svelte-routing";

    export let to;
    export let setClass=undefined;

    function onClick(){
        navigate(to, { replace: false });
    }
</script>

<style>
div {
    cursor: pointer;
}
</style>

<div on:click={onClick} class={setClass}>
    <slot/>
</div>
-->