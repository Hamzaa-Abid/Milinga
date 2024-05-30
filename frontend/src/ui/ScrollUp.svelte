<style>
.gg-chevron-up {
    box-sizing: border-box;
    position: relative;
    display: block;
    transform: scale(var(--ggs, 1));
    width: 22px;
    height: 22px;
    border: 2px solid transparent;
    border-radius: 100px;
    margin: auto;
    padding: 14px 0px;
    line-height: 40px;
}

.gg-chevron-up::after {
    content: "";
    display: block;
    box-sizing: border-box;
    position: absolute;
    width: 10px;
    height: 10px;
    border-top: 2px solid;
    border-right: 2px solid;
    transform: rotate(-45deg);
    left: 4px;
    bottom: 2px
}

#scrollup {
    display: block;
    position: fixed;
    z-index: 2147483647;
    bottom: 30px;
    font-size: 1rem;
    right: 30px;
    width: 40px;
    height: 40px;
    color: #ffffff;
    text-align: center;
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.15);
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.15);
    -webkit-transition-duration: 500ms;
    transition-duration: 500ms;
    border-radius: 50%;
    background-color: #453264;
    cursor: pointer;
}

#scrollup:hover,
#scrollup:focus {
    background-color: #FAB705;
}

</style>

<svelte:window bind:scrollY={scrollY}/>

<script>
// scrollName: 'scrollUp',      // Element ID
// scrollDistance: 300,         // Distance from top/bottom before showing element (px)
// scrollFrom: 'top',           // 'top' or 'bottom'
// scrollSpeed: 1100,           // Speed back to top (ms)
// easingType: 'linear',        // Scroll to top easing (see http://easings.net/)
// animation: 'fade',           // Fade, slide, none
// animationSpeed: 200,         // Animation in speed (ms)
// scrollTrigger: false,        // Set a custom triggering element. Can be an HTML string or jQuery object
// scrollTarget: false,         // Set a custom target element for scrolling to. Can be element or number
// scrollText: '<i class="gg-chevron-up"></i>', // Text for element, can contain HTML
// scrollTitle: false,          // Set a custom <a> title if required. Defaults to scrollText
// scrollImg: false,            // Set true to use image
// activeOverlay: false,        // Set CSS color to display scrollUp active point, e.g '#00FFFF'
// zIndex: 2147483647           // Z-Index for the overlay
    import * as animateScroll from "svelte-scrollto";
    import { fade } from 'svelte/transition';

    let scrollY;
</script>

{#if scrollY>300}
    <div id="scrollup" in:fade out:fade on:click={()=>{animateScroll.scrollToTop({duration:1000})}}>
        <i class="gg-chevron-up"></i>
    </div>
{/if}