<script>
	import Fa from 'svelte-fa';
    import { faUsers } from '@fortawesome/free-solid-svg-icons';

    export let animate=false;
</script>

<style>
    /* div :global(svg) {
        width:4rem;
        height:4rem;
        padding:10px;
    } */

	/* .bg{fill:#fff;cursor:pointer;}
	.fg {fill:#222;cursor:pointer;} */
	.animatefg {
		animation-name: changingfg;
		animation-duration: 0.3s;
		animation-direction: alternate;
		animation-timing-function: linear;
		animation-iteration-count: infinite;
        padding: 3px;
	}
	.animatebg {
		animation-name: changingbg;
		animation-duration: 0.6s;
		animation-direction: alternate;
		animation-timing-function: linear;
		animation-iteration-count: infinite;
        border-radius: 20px;
	}

	@keyframes changingbg {
		0% {
			background-color: #ccc;
		}
		100% {
			background-color: #999;
		}
	}
    @keyframes changingfg {
		0% {
			color: #000;
		}
		100% {
			color: #f00;
		}
	}

</style>

<div class:animatebg={animate}><div class:animatefg={animate}><Fa icon={faUsers} /></div></div>