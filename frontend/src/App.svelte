<svelte:head>
	<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha512-weZatQD41YXNCVn3Bvl2y1iAZqtH/Y+MlAQUwovog1iwj8cbSEpQMeErMnDp9CBlqIo0oxOcOF8GUEoOZYD4Zg==" crossorigin="anonymous" />
	<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.0.0-alpha1/js/bootstrap.bundle.min.js" integrity="sha512-UzofO1xJCmOl9xNdbqkMIaaW5raQxAE8WyMa977+mY2fT001KydNwvqSTJlHy70edjCN0nb20BXIgBgO/oj6MQ==" crossorigin="anonymous"></script> -->
</svelte:head>

<script>
	import Header from "~/pages/ui/Header.svelte";
	import Footer from "~/pages/ui/Footer.svelte";
	import Chat from "ui_dyn/chat/Chat.svelte";

	import Home from "~/pages/Home.svelte";
	import TeacherList from "~/pages/TeacherList.svelte";
	import TeacherDetail from "~/pages/TeacherDetail.svelte";
	import Profile from "~/pages/Profile.svelte";
	import MyCalendar from "~/pages/MyCalendar.svelte";
	import Login from "~/pages/accounts/Login.svelte";
	import Register from "~/pages/accounts/Register.svelte";
	import RegisterTeacher from "~/pages/accounts/RegisterAsATeacher.svelte";
	import RegisterStudent from "~/pages/accounts/RegisterAsAStudent.svelte";
	import ConfirmEmail from "~/pages/accounts/ConfirmEmail.svelte";
	import PasswordReset from "~/pages/accounts/PasswordReset.svelte";
	import PasswordResetConfirm from "~/pages/accounts/PasswordResetConfirm.svelte";
	import PasswordChange from '~/pages/accounts/PasswordChange.svelte';
	import Credits from "~/pages/Credits.svelte";

	import Modal from 'svelte-simple-modal';

	import {fade} from "svelte/transition"
	import { Router, Route, navigate } from 'svelte-routing';
	import Link from 'ui/Link.svelte';
	import { onMount } from 'svelte';
	// import Debug from '~/Debug.svelte';

	import {websocket} from 'js/websocket.js';
	import {users} from 'store/users.js';
	import {logout, authenticated} from 'js/account.js';

	let params = {
		id:0,
	};

	// function getToken(){
	// 	let token = localStorage.getItem('token');
	// 	if(!token) {
	// 		token = sessionStorage.getItem('token');
	// 	}
	// 	return token;
	// }

	// websocket.addEventListener('ws_open', function(){
	// 	let token = getToken();
	// 	if(token){
	// 		authenticated=true;
	// 		websocket.send('auth_jwt', {
	// 			token: token,
	// 		}).then(function(bAuthenticated){
	// 			authenticated = bAuthenticated;
	// 		})
	// 	}
	// });

	// function logout(){
	// 	// websocket.send('auth_logout', null, {answer:false});
	// }
	// websocket.sendToOtherMe('piep', 12345);
	// websocket.onReceive('piep', function(i){
	// 	console.log(i);
	// })

	function onLogout(){
		navigate('/', { replace: false });
		logout();
	}

	function showProfile(userId){
		if($users[userId].isTeacher === true){
			navigate("/teacher/"+event.detail+'/', { replace: false })
		} else {
			// navigate("/student/"+event.detail+'/', { replace: false }) //TODO: Student Profile!
		}
	}

	let openChat = ()=>{};

	let preloaderVisible=true;	
	onMount(async () => {
		preloaderVisible = false;
	});
</script>

<style>
/* Preloader CSS */
.preloader {
	position: fixed;
	width: 100%;
	height: 100%;
	z-index: 9999999;
	top: 0;
	left: 0;
	background-color: #FAB705;
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	justify-content: center;
	overflow: hidden;
}
</style>

<!-- Preloader-->
{#if preloaderVisible}
	<div class="preloader" out:fade="{{ duration: 500 }}">
		<div class="spinner-grow text-light" role="status"></div>
	</div>
{/if}

<!-- <div transition:fade intro:true> -->
<!-- <Debug /> -->
<!-- <Modal> -->
<Router>
	<Header on:logout={onLogout}/>
	<Route path=""><Home/></Route>
	<Route path="/login/"><Login/></Route>
	<Route path="/register/"><Register/></Route>
	<Route path="/register/teacher/"><RegisterTeacher/></Route>
	<Route path="/register/student/"><RegisterStudent/></Route>
	<Route path="/rest-auth/registration/account-confirm-email/:key/" let:params><ConfirmEmail key={params.key}/></Route>
	<Route path="/passwordreset/"><PasswordReset/></Route>
	<Route path="/password-reset/:uid/:token/" let:params><PasswordResetConfirm {...params}/></Route>
	<Route path="/passwordchange/"><PasswordChange/></Route>


	<Route path="/teacher/:id/" let:params><TeacherDetail teacherId={params.id} on:openchat={(event)=>{openChat(event.detail.userId)}}/></Route>
	<Route path="/teachers/"><TeacherList on:openchat={(event)=>{openChat(event.detail.userId)}}/></Route>
	<Route path="/profile/"><Profile/></Route>
	<Route path="/calendar/"><MyCalendar /></Route>
	<Route path="/payments/"><Credits/></Route>

	<Footer/>

	<!-- {#if $authenticated}
		<Chat {openChat} on:contactClicked={(event)=>{showProfile(event.detail)}}></Chat>
	{/if} -->

</Router>
<!-- </Modal> -->