<!--
import Contact from 'ui/Contact.svelte';

<Contact {profilePic} {name} />
oder
<Contact {...person} />
-->

<style>
	img {
		border-radius: 50%;
		width: 40px;
		height: 40px;
	}
	span {
		margin-left: 15px;
		font-weight: 600;
    }
    
    div {
        display: flex;
        flex-wrap: wrap;
        /*justify-content: center;*/ /* ADJUSTMENT */
        align-items:center;
    }
    div::content {
        margin: 15px;
    }
</style>

<script>
    export let profilePic;
    export let name;
</script>

<div>
    <img src={profilePic} alt="profilePic">
    <span style="white-space: nowrap;">{name}</span>
</div>