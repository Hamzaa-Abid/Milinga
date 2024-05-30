<script>
    import { navigate } from "svelte-routing";
</script>

<style>
@media only screen and (max-width: 576px) {

  .row>* {
    padding-right: calc(var(--bs-gutter-x)/ 1);
    padding-left: calc(var(--bs-gutter-x)/ 1);
  }
}

.text-summer-sky {
  color: #27AAE1;
}

.text-yellow-green {
  color: #80C43B;
}

.border-b-orange {
  border-bottom: 4px solid #FAB705;
}

.title-divider {
  background: #FFBD94;
  height: 2px !important;
  opacity: 1;
  border: none;
}

@-webkit-keyframes rotateAnimation {
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes rotateAnimation {
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@media all and (-ms-high-contrast: none),
(-ms-high-contrast: active) {
  .row>* {
    padding: 0 15px;
    margin-top: 35px;
  }
}

.white-card {
  background-color: #fff;
  box-shadow: 0 20px 35px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
}

@media only screen and (max-width: 767px) {
  .create-account-divider {
    height: 2px !important;
    width: 90% !important;
    right: 0 !important;
    top: 85px !important;
    left: 0 !important;
    margin: auto;
  }
}

.create-account h3 a:hover {
  color: #FF792E;
}

.account-cta a {
  color: #FF792E;
  text-decoration: underline;
}

.account-cta a:hover {
  color: #1f0757;
}

.create-account-divider {
  height: 100%;
  background: #E3E3E3;
  width: 3px;
  border-radius: 10px;
  position: absolute;
  right: 5px;
  top: 0;
}

section {
	padding-top: 150px;
	padding-bottom: 90px;
}
</style>


<!-- Create Account -->
<section class="create-account section-padding-150-90 bg-old-lace border-b-orange">

    <div class="container">
        <div class="row">

            <!-- Page Title -->
        <div class="col-12 pt-2 mt-2 pt-md-3 mt-md-5 mb-4 col-md-10 col-lg-8 offset-lg-2 text-center offset-md-1">
            <h2 class="d-inline-block">Create Account
            <hr class="title-divider" />
            </h2>
        </div>
        </div>

        <div class="row">
        <div class="col-12 col-md-10 col-lg-8 offset-lg-2 offset-md-1">
            <div class="white-card px-2 px-md-4 py-4 mt-3">
            <div class="row g-3">
                <!-- As a Student -->
                <div class="col-md-6 py-4 position-relative">
                <h3 class="text-center mb-0"><a href="javascript:void(0)" class="text-summer-sky" on:click={()=>{navigate("/register/student/")}}>As a Student</a></h3>
                <span class="create-account-divider"></span>
                </div>
                <!-- Become a Teacher -->
                <div class="col-md-6 py-4">
                <h3 class="text-center mb-0"><a href="javascript:void(0)" class="text-yellow-green" on:click={()=>{navigate("/register/teacher/")}}>Become a Teacher</a></h3>
                </div>
            </div>
            </div>
        </div>
        </div>

        <!-- Login Button -->
        <div class="row">
        <div class="col-12 col-md-10 text-center col-lg-8 mt-5 offset-lg-2 offset-md-1">
            <p class="account-cta">Do you already have an account with us? <a href="javascript:void(0)" on:click={()=>{navigate("/login/")}}>Login</a></p>
        </div>
        </div>
    </div>

</section>