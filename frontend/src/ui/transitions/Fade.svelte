<!--
import Fade from 'transitions/Fade.svelte';

<Fade show={true}>
</Fade>
-->

<script>

	export let show=true;
</script>

<Fade isOpen={show}><!-- TODO: Fade mit Bootstrap v5 korrigieren, Beispiel in Slide.svelte! -->
	<slot/>
</Fade>