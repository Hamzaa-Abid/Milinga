<style>
/* Header CSS */
.header-area {
	position: fixed;
	width: 100%;
	top: 0;
	left: 0;
	z-index: 1000;
	background-color: transparent;
}

.header-area .classy-nav-container {
 	 background-color: transparent;
}

.classy-navbar {
	height: 100px;
	-webkit-transition-duration: 500ms;
	transition-duration: 500ms;
}

@media only screen and (max-width: 767px) {
	.classy-navbar {
		height: 60px;
	}
}

.classy-navbar .classynav ul li a {
	padding: 0 1rem;
	height: auto;
	font-family: 'Linotte';
	font-size: 14px;
	color: #8C8989;
	letter-spacing: 0.75px;
	font-weight: 600;
}

.classynav ul {
	padding-left: 0;
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
	.classy-navbar .classynav ul li a {
		padding: 30px 15px;
	}
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
	.classy-navbar .classynav ul li a {
		padding: 15px;
		color: #1f0757;
	}
}

@media only screen and (max-width: 767px) {
	.classy-navbar .classynav ul li a {
		padding: 15px;
		color: #1f0757;
		line-height: 0;
		font-size: 1.15rem;
	}

	.breakpoint-on .classynav ul li {
		min-height: 60px;
	}
}

.classy-navbar .classynav ul li a:hover,
.classy-navbar .classynav ul li a:focus {
  	color: #ffffff;
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
	.classy-navbar .classynav ul li a:hover,
	.classy-navbar .classynav ul li a:focus {
		color: #FAB705;
	}
}

@media only screen and (max-width: 767px) {
	.classy-navbar .classynav ul li a:hover,
	.classy-navbar .classynav ul li a:focus {
		color: #FAB705;
	}
}

.classy-navbar .classynav>ul>li:hover>a {
 	 color: #fdd76e;
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
	.classy-navbar .classynav>ul>li:hover>a {
		color: #FAB705;
	}
}

@media only screen and (max-width: 767px) {
	.classy-navbar .classynav>ul>li:hover>a {
		color: #FAB705;
	}
}

.classy-navbar .classynav ul li li a {
	padding: 14px 28px;
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	color: #1f0757;
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
	.classy-navbar .classynav ul li li a {
		padding: 14px 18px;
	}
}

.classy-navbar .classynav ul li li a:hover,
.classy-navbar .classynav ul li li a:focus {
  	color: #FAB705;
}

.classy-navbar .classynav ul li li a span {
	display: block;
	color: #1f0757;
	-webkit-transition-duration: 400ms;
	transition-duration: 400ms;
}

.classy-navbar .classynav ul li li a span:hover,
.classy-navbar .classynav ul li li a span:focus {
 	 color: #FAB705;
}

.classy-navbar .classynav ul li li a span span {
	margin-top: 0.5rem;
	color: #8480ae;
	font-size: 13px;
	text-transform: initial;
}

.classy-navbar .classynav ul li li a span span:hover,
.classy-navbar .classynav ul li li a span span:focus {
 	 color: #8480ae;
}

.classy-navbar .classynav ul li .dropdown li a {
  	border-bottom: none;
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
	.classy-navbar .classynav ul li .dropdown li a {
		padding: 14px 30px;
	}
}

.header .classynav>ul>li:hover>a {
 	 color: #FAB705;
}

.header .classynav ul li a:hover,
.header .classynav ul li a:focus {
 	 color: #FAB705;
}

.header .classynav>ul>li>a::before {
  	background-color: #FAB705;
}

.classy-navbar-toggler {
	width: 30px;
	height: 30px;
	padding: 2px;
}

.classy-navbar-toggler .navbarToggler {
	position: relative;
	z-index: 1;
	width: 26px;
	height: 26px;
}

.classy-navbar-toggler .navbarToggler span {
	position: absolute;
	z-index: auto;
	width: 10px;
	border-radius: 50%;
	height: 10px;
	margin: 0;
}

.classy-navbar-toggler .navbarToggler span:first-child {
	top: 0;
	left: 0;
	background-color: #ffffff;
}

.classy-navbar-toggler .navbarToggler span:nth-child(2) {
	top: 0;
	right: 0;
	background-color: #fdd76e;
}

.classy-navbar-toggler .navbarToggler span:nth-child(3) {
	bottom: 0;
	left: 0;
	background-color: #fdd76e;
}

.classy-navbar-toggler .navbarToggler span:last-child {
	bottom: 0;
	right: 0;
	background-color: #ffffff;
}

.classy-navbar-toggler .navbarToggler.active span:first-child {
	top: 0;
	left: 0;
	border-radius: 50% 50% 0% 50%;
	-webkit-transform: rotate3d(0, 0, 1, 0deg);
	transform: rotate3d(0, 0, 1, 0deg);
}

.classy-navbar-toggler .navbarToggler.active span:nth-child(2) {
	top: 0;
	right: 0;
	opacity: 1;
	border-radius: 50% 50% 50% 0%;
}

.classy-navbar-toggler .navbarToggler.active span:nth-child(3) {
	bottom: 0;
	left: 0;
	top: auto;
	border-radius: 50% 0% 50% 50%;
	-webkit-transform: rotate3d(0, 0, 1, 0deg);
	transform: rotate3d(0, 0, 1, 0deg);
}

.classy-navbar-toggler .navbarToggler.active span:last-child {
	bottom: 0;
	right: 0;
	border-radius: 0% 50% 50% 50%;
}

.header .classy-navbar-toggler .navbarToggler span:first-child {
  	background-color: #453264;
}

.header .classy-navbar-toggler .navbarToggler span:nth-child(2) {
 	 background-color: #FF792E;
}

.header .classy-navbar-toggler .navbarToggler span:nth-child(3) {
  	background-color: #FF792E;
}

.header .classy-navbar-toggler .navbarToggler span:last-child {
  	background-color: #453264;
}

.classycloseIcon {
  	top: 26px;
}

.breakpoint-on .classy-navbar .classy-menu {
	-webkit-box-shadow: 0 5px 15px 0 rgb(250 183 5 / 10%);
	box-shadow: 0 5px 15px 0 rgb(250 183 5 / 10%);
}


.header-area.sticky {
	position: fixed;
	width: 100%;
	top: 0;
	left: 0;
	right: 0;
	z-index: 1001;
	background-color: #FAB705;
	-webkit-box-shadow: 0 5px 15px 0 rgb(250 183 5 / 10%);
	box-shadow: 0 5px 15px 0 rgb(250 183 5 / 10%);
}

.header-area.sticky .classy-navbar {
	height: 80px;
}

@media only screen and (max-width: 767px) {
	.header-area.sticky .classy-navbar {
		height: 80px;
	}
}

.header-area.header.sticky {
	background-color: #ffffff;
	-webkit-box-shadow: 0 5px 15px 0 rgb(250 183 5 / 10%);
	box-shadow: 0 5px 15px 0 rgb(250 183 5 / 10%);
}

@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
	.breakpoint-on .classy-navbar-toggler, .breakpoint-on .classycloseIcon {
		margin-left: auto;
	}
	.classy-navbar .classynav ul li a  {
		font-family: 'Linotte',sans-serif;
	}
}
</style>

<svelte:window bind:scrollY={scrollY} bind:innerWidth={innerWidth}/>

<script>
	import Fa from 'svelte-fa';
	import { faPencilAlt, faUserEdit, faCalendarAlt, faTools, faSignOutAlt, faChalkboardTeacher, faUserPlus, faSignInAlt, faLanguage, faCoins, faKey } from '@fortawesome/free-solid-svg-icons';
	import { createEventDispatcher } from 'svelte';

	// import Select from 'ui/Select.svelte';
	// import {languages, languageCode} from 'store/languages.js';
	import {authenticated} from 'js/account.js';

	// import Link from 'ui/Link.svelte';
	// import ErrorBar from 'ui_dyn/errorbar/ErrorBar.svelte';
	// import VideoConferenceJumbotron from 'ui_dyn/VideoConferenceJumbotron.svelte';

	import MilingaLogo from 'svg/milinga_logo.svelte';

	const dispatch = createEventDispatcher();

	// let dropdownSettingsIsOpen = false;
	let dropdownSettings;
	import { navigate, Link } from "svelte-routing";

	let scrollY, innerWidth;

	$: classyNavbarMaximized = innerWidth > 991;
	let classyNavbarOpen = false;

	function navigateTo(sPage){
		navigate(sPage, {replace:false});
		classyNavbarOpen = false;
	}
	function logout(){
		dispatch('logout');
		classyNavbarOpen = false;
	}
</script>

<header class="header-area header" class:sticky={scrollY>0}>
	<div class="container">
		<div class="classy-nav-container" class:breakpoint-on={!classyNavbarMaximized} class:breakpoint-off={classyNavbarMaximized}>
			<nav class="classy-navbar navbar2 justify-content-between">
				<!-- Logo--><a class="nav-brand mr-5" href="javascript:void(0)" on:click={()=>{navigateTo("/");}}><img src="{document.body.dataset.staticurl}img/milinga-logo.svg" alt=""></a>
				<!-- Navbar Toggler-->
				<div class="classy-navbar-toggler">
					<span class="navbarToggler" class:active={classyNavbarOpen} on:click={()=>{classyNavbarOpen=!classyNavbarOpen}}><span></span><span></span><span></span><span></span></span>
				</div>
				<!-- Menu-->
				<div class="classy-menu" class:menu-on={classyNavbarOpen}>
					<!-- close btn-->
					<div class="classycloseIcon" on:click={()=>{classyNavbarOpen=false}}>
						<div class="cross-wrap"><span class="top"></span><span class="bottom"></span></div>
					</div>
					<!-- Nav Start-->
					<div class="classynav">
						<ul id="corenav">
							<!-- {#if $preferences.isTeacher == false} -->
							<li><a href="javascript:void(0)" on:click={()=>{navigateTo("/teachers/")}}>Find a Teacher</a></li>
							<!-- {/if} -->
							{#if $authenticated}
								<li><Fa icon={faTools}/> Settings</li>
								<li><a href="javascript:void(0)" on:click={()=>{navigateTo("/profile/")}}><Fa icon={faUserEdit}/> Profile</a></li>
								<li><a href="javascript:void(0)" on:click={()=>{navigateTo("/calendar/")}}><Fa icon={faCalendarAlt}/> Calendar</a></li>
								<li><a href="javascript:void(0)" on:click={()=>{navigateTo("/payments/")}}><Fa icon={faCoins}/> Payments</a></li>
								<li><a href="javascript:void(0)" on:click={()=>{navigateTo("/passwordchange/")}}><Fa icon={faKey}/> Change Password</a></li>
								<li><a href="javascript:void(0)" on:click={logout}><Fa icon={faSignOutAlt}/> Logout</a></li>
							{:else}
								<li><a href="javascript:void(0)">Why Milinga</a></li>
								<li><a href="javascript:void(0)" on:click={()=>{navigateTo("/login/")}}>Login</a></li>
								<li><a href="javascript:void(0)" on:click={()=>{navigateTo("/register/")}}>Create Account</a></li>
							{/if}
						</ul>
					</div>
				</div>
			</nav>
		</div>
	</div>
</header>