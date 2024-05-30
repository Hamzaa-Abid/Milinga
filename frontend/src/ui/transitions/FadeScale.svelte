<!--
import FadeScale from 'transitions/FadeScale.svelte';

<FadeScale show={...}>...</FadeScale>
-->

<script>
	import { fade } from 'svelte/transition';
	import { quintIn, quintOut } from 'svelte/easing';

	export let duration=250;
	export let show=true;
	export let fadeScaleIn=true;
	export let fadeScaleOut=true;


	function fadescaleIn(node){
		if(fadeScaleIn != true) {
			return;
		}
		return fadescale(node, {fadeScaleIn: true});
	}
	function fadescaleOut(node){
		if(fadeScaleOut != true){
			return;
		}
		return fadescale(node, {fadeScaleIn: false})
	}
	
	function fadescale(node, { fadeScaleIn }) {
		let ease = fadeScaleIn===true?quintOut:quintIn;
		return {
			duration,
			css: t => {
				const eased = ease(t);

				return `
					transform: scale(${eased});
					opacity: ${eased};`
			}
		};
	}
</script>

{#if show === true}
	<div class="centered" in:fadescaleIn|local out:fadescaleOut|local>
		<slot />
	</div>
{/if}