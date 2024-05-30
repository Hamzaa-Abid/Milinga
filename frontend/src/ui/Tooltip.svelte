<!--
import Tooltip from 'ui/Tooltip.svelte';

<Tooltip text="">...</Tooltip>
-->

<!-- <style>
.ltooltip {
    position: relative;
    display: inline-block;
    /* border-bottom: 1px dotted black; */
}

.ltooltip .ltooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: #555;
    color: #fff;
    text-align: center;
    /* border-radius: 6px; */
    padding: 5px 0;
    position: absolute;
    z-index: 10;
    bottom: 125%;
    left: 50%;
    margin-left: -60px;
    opacity: 0;
    transition: opacity 0.3s;
}

.ltooltip .ltooltiptext::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #555 transparent transparent transparent;
}

.ltooltip:hover .ltooltiptext {
    visibility: visible;
    opacity: 1;
}
</style>

<script>
    export let text;
</script>

<div class:ltooltip={text!=undefined}>
    {#if text!=undefined}
        <span class="ltooltiptext">{text}</span>
    {/if}
    <slot/>
</div> -->


<!-- <script>
    import SvelteTooltip from 'svelte-tooltip';
    
    export let text;
    export let top,left,bottom,right;

    if(top==undefined && left==undefined && bottom==undefined && right==undefined){
        top = true;
    }
</script>

<SvelteTooltip tip={text} color="#EEEEEE" {top} {left} {bottom} {right} >
    <slot />
</SvelteTooltip> -->


<script>
    import tippy from "sveltejs-tippy";
    
    export let text;
    export let placement='top';
    // export let top,left,bottom,right;

    // let placement='top';
    // if(top) placement='top';
    // if(left) placement='left';
    // if(bottom) placement='bottom';
    // if(right) placement='right';

    let props = {
        content: text,
        placement: placement,
    }
</script>

<div class="d-flex justify-content-center" use:tippy={props}>
    <slot />
</div>