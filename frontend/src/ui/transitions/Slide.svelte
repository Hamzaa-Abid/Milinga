<!--
import Slide from 'transitions/Slide.svelte';

<Slide show={true}>
</Slide>
-->

<script>
	import { onMount } from 'svelte';

	export let show=true;

	let collapseEl;
	
	$: showCollapse(show);

	function showCollapse(bShow){
		if(!window.bootstrap || !collapseEl) return;
		let collapse = new bootstrap.Collapse(collapseEl);
		if(bShow) {
			collapse.show();
		} else {
			collapse.hide();
		}
	}
</script>

<div bind:this={collapseEl} class='collapse'>
	<slot/>
</div>

<!-- <script>
	export let show=true;
	let slideDiv;

	let slideUp = (target, duration=1000) => {
		target.style.transitionProperty = 'height, margin, padding';
		target.style.transitionDuration = duration + 'ms';
		target.style.boxSizing = 'border-box';
		target.style.height = target.offsetHeight + 'px';
		target.offsetHeight;
		target.style.overflow = 'hidden';
		target.style.height = 0;
		target.style.paddingTop = 0;
		target.style.paddingBottom = 0;
		target.style.marginTop = 0;
		target.style.marginBottom = 0;
		window.setTimeout( () => {
		target.style.display = 'none';
		target.style.removeProperty('height');
		target.style.removeProperty('padding-top');
		target.style.removeProperty('padding-bottom');
		target.style.removeProperty('margin-top');
		target.style.removeProperty('margin-bottom');
		target.style.removeProperty('overflow');
		target.style.removeProperty('transition-duration');
		target.style.removeProperty('transition-property');
		//alert("!");
		}, duration);
	}

	let slideDown = (target, duration=1000) => {
		target.style.removeProperty('display');
		let display = window.getComputedStyle(target).display;

		if (display === 'none')
			display = 'block';

		target.style.display = display;
		let height = target.offsetHeight;
		target.style.overflow = 'hidden';
		target.style.height = 0;
		target.style.paddingTop = 0;
		target.style.paddingBottom = 0;
		target.style.marginTop = 0;
		target.style.marginBottom = 0;
		target.offsetHeight;
		target.style.boxSizing = 'border-box';
		target.style.transitionProperty = "height, margin, padding";
		target.style.transitionDuration = duration + 'ms';
		target.style.height = height + 'px';
		target.style.removeProperty('padding-top');
		target.style.removeProperty('padding-bottom');
		target.style.removeProperty('margin-top');
		target.style.removeProperty('margin-bottom');
		window.setTimeout( () => {
			target.style.removeProperty('height');
			target.style.removeProperty('overflow');
			target.style.removeProperty('transition-duration');
			target.style.removeProperty('transition-property');
		}, duration);
	}

	// var slideToggle = (target, duration = 500) => {
	// 	if (window.getComputedStyle(target).display === 'none') {
	// 		return slideDown(target, duration);
	// 	} else {
	// 		return slideUp(target, duration);
	// 	}
	// }

	$: show, function(){
		if(slideDiv === undefined) return;
		if(show === true){
			slideDown(slideDiv);
		} else {
			slideUp(slideDiv);
		}
	}()
</script>

<div bind:this={slideDiv}>
	<slot />
</div> -->