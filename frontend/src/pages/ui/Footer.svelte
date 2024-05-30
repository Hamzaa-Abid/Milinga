<style>
/* Footer CSS */
.footer-area {
  position: relative;
  padding-top: 40px;
  background-color: #F8F8F8;
  padding-bottom: 40px;
}

.footer-area .newsletter-form {
  position: relative;
  z-index: 1;
  display: block;
  margin-bottom: 30px;
}

.footer-area .newsletter-form .form-control {
  border: none;
  border-bottom: 1px solid #eeeeee;
  border-radius: 0;
  padding-left: 5px;
  background-color: #ffffff;
  font-size: 14px;
}

.footer-area .newsletter-form .form-control:focus {
  border-bottom-color: #FAB705;
  background-color: #ffffff;
}

.footer-area .footer-widget-area {
  position: relative;
  z-index: 1;
}

.footer-area .footer-widget-area .widget-title {
  margin-bottom: 20px;
}


.footer-area .footer-widget-area ul {
  padding-left: 0;
}

.footer-area .footer-widget-area ul li a {
  display: block;
  color: #8480ae;
  margin-bottom: 0.75rem;
  font-size: 15px;
}

@media only screen and (min-width: 576px) and (max-width: 767px) {
  .footer-area .footer-widget-area ul li a {
    font-size: 14px;
  }
}

.footer-area .footer-widget-area ul li a:hover,
.footer-area .footer-widget-area ul li a:focus {
  color: #FAB705;
}

.footer-area .footer-widget-area ul li:last-child a {
  margin-bottom: 0;
}

.footer-area .footer-social-icon a {
  margin-right: 1.25rem;
  font-size: 1.25rem;
  color: #8C8989;
}

.footer-area .footer-social-icon a:hover,
.footer-area .footer-social-icon a:focus {
  margin-right: 1.25rem;
  font-size: 1.25rem;
  color: #27AAE1;
}

@media only screen and (max-width: 767px) {
  .footer-area .footer--content-text {
    text-align: center;
    margin-bottom: 0;
  }
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .footer-area .footer--content-text p {
    font-size: 14px;
  }
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .footer-area .footer--content-text p {
    font-size: 14px;
  }
}

@media only screen and (max-width: 767px) {
  .footer-area .footer--content-text p {
    font-size: 14px;
  }
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .footer-area .footer--content-text a {
    font-size: 14px;
  }
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .footer-area .footer--content-text a {
    font-size: 14px;
  }
}

@media only screen and (max-width: 767px) {
  .footer-area .footer--content-text a {
    font-size: 14px;
  }
}

@media only screen and (max-width: 576px) {

  .footer-social-icon {
    justify-content: center;
  }

  .footer-area .footer--content-text {
    margin-top: 40px;
  }

  .footer-area .footer-nav ul {
    flex-flow: wrap;
    line-height: 40px;
  }

  .section-padding-0-30 {
    padding-top: 0px;
    padding-bottom: 20px;
  }

}

.footer--content-text p {
  color: #8C8989;
}

.footer-area .footer--content-text a:hover,
.footer-area .footer--content-text a:focus {
  color: #27AAE1;
}

.footer-area .footer-nav ul {
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  padding-left: 0;
}

.footer-area .footer-nav ul li a {
  color: #8C8989;
  margin: 0 15px;
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .footer-area .footer-nav ul li a {
    margin: 0 12px;
    font-size: 14px;
  }
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .footer-area .footer-nav ul li a {
    margin: 0 6px;
    font-size: 14px;
  }
}

@media only screen and (max-width: 767px) {
  .footer-area .footer-nav ul li a {
    margin: 0 6px;
    font-size: 14px;
  }
}

.footer-area .footer-nav ul li a:hover,
.footer-area .footer-nav ul li a:focus {
  color: #FAB705;
}

.footer-area .footer-nav ul li:first-child a {
  margin-left: 0;
}

.footer-area .footer-nav ul li:last-child a {
  margin-right: 0;
}

.footer-area .language-dropdown {
  position: relative;
  z-index: 1;
}

@media only screen and (min-width: 576px) and (max-width: 767px) {
  .footer-area .language-dropdown {
    margin-bottom: 15px;
  }
}

.footer-area .language-dropdown .dropdown-menu {
  padding: 1rem 0;
  border: 1px solid #eeeeee;
  border-radius: 0.75rem;
  -webkit-box-shadow: 0 5px 15px 0 rgb(250 183 5 / 10%);
  box-shadow: 0 5px 15px 0 rgb(250 183 5 / 10%);
}

.footer-area .language-dropdown .btn-group.dropup {
  background: #fff;
  height: 40px;
  width: 160px;
  border-radius: 6px;
  box-shadow: 0 10px 40px rgb(51 51 51 / 13%);
}

.footer-area .language-dropdown .btn-group.dropup .btn {
  color: #8C8989;
}

.footer-area .language-dropdown .btn-group.dropup .btn:hover,
.footer-area .language-dropdown .btn-group.dropup .btn:focus {
  color: #453264;
}

.dropup .dropdown-toggle::after {
  margin-left: 3.255em;
  vertical-align: middle;
}

.footer-area .language-dropdown .dropdown-menu .dropdown-item {
  color: #8C8989;
  font-size: 14px;
}

.footer-area .language-dropdown .dropdown-menu .dropdown-item:hover,
.footer-area .language-dropdown .dropdown-menu .dropdown-item:focus {
  color: #8C8989;
  background-color: #f4f4ff;
}
</style>

<script>
  	import {languages, languageCode} from 'store/languages.js';
</script>

<!-- Footer Area-->
<footer class="footer-area">
	<div class="container border-bottom section-padding-0-30 mb-30">
		<div class="row justify-content-between align-items-center">
		<!-- Footer Widget Area-->
		<div class="col-12 d-lg-flex d-none col-sm-10 col-lg-3">
			<div class="footer-widget-area"><a class="d-block" href="index.html"><img src="{document.body.dataset.staticurl}img/milinga-logo.svg" alt=""></a>
			</div>
		</div>
		<div class="col-12 col-md-12 col-lg-9 justify-content-lg-end justify-content-md-center d-flex">
			<!-- Footer Nav-->
			<div class="footer-nav">
			<ul class="d-flex">
				<li><a href="javascript:void(0)">Become a Teacher</a></li>
				<li><a href="javascript:void(0)">Company</a></li>
				<li><a href="javascript:void(0)">Support</a></li>
				<li><a href="javascript:void(0)">Legal</a></li>
				<li><a href="javascript:void(0)">Privacy</a></li>
				<li><a href="javascript:void(0)">Contact</a></li>
			</ul>
			</div>
		</div>
		</div>
	</div>
	<div class="container">
		<div class="row align-items-center">
		<div class="col-12 col-sm-6 col-md-6 col-lg-5">
			<div class="footer-social-icon d-flex align-items-center">
			<a href="javascript:void(0)" data-toggle="tooltip" data-placement="top" title="Facbook">
				<i class="lni-facebook-filled"></i>
			</a>
			<a href="javascript:void(0)" data-toggle="tooltip" data-placement="top" title="Twitter">
				<i class="lni-twitter-filled"></i>
			</a>
			<a href="javascript:void(0)" data-toggle="tooltip" data-placement="top" title="Instagram">
				<i class="lni-instagram-original"></i>
			</a>
			<a href="javascript:void(0)" data-toggle="tooltip" data-placement="top" title="Youtube">
				<i class="lni-youtube"></i>
			</a>
			</div>
		</div>
		<div class="col-12 mt-sm-4 mt-lg-0 order-one col-sm-12 col-lg-5 col-md-12 text-center text-lg-left">
			<!-- Copywrite Text-->
			<div class="footer--content-text">
			<p class="mb-0">©2020 milinga all rights reserved</p>
			</div>
		</div>
		<div class="col-12 order-two col-sm-6 col-md-6 col-lg-2">
			<!-- Default dropup button-->
			<div class="language-dropdown text-sm-right text-center text-lg-right mt-4 mt-lg-0">
			<div class="btn-group dropup">
				<button class="btn dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true"
				aria-expanded="false">Language</button>
				<div class="dropdown-menu dropdown-menu-right">
				{#each $languages as language}
					<a class="dropdown-item" href="javascript:void(0)" on:click={()=>{$languageCode=language.code}}><span class="mr-2 flag-icon flag-icon-{language.code}"></span>{language.name_local}</a>
				{/each}
			</div>
			</div>
		</div>
		</div>
	</div>
</footer>