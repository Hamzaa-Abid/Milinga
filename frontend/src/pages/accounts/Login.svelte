<style>
input:required,
textarea:required {
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
}

input:invalid,
textarea:invalid {
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
}

@media only screen and (max-width: 576px) {

  .row>* {
    padding-right: calc(var(--bs-gutter-x)/ 1);
    padding-left: calc(var(--bs-gutter-x)/ 1);
  }
}

.border-b-orange {
  border-bottom: 4px solid #FAB705;
}

.bg-old-lace {
  background: #FFF6E9;
}

.title-divider {
  background: #FFBD94;
  height: 2px !important;
  opacity: 1;
  border: none;
}

.form-control,
.form-select {
  display: block;
  width: 100%;
  min-height: calc(1.5em + 1rem + 2px);
  padding: .375rem .75rem .25rem .75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #453264;
  background-color: #fff;
  background-clip: padding-box;
  border: 2px solid #ced4da;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: .5rem;
}

.form-control::placeholder,
.form-select::placeholder {
  color: #D3D3D3;
}

.form-control:focus,
.form-select:focus,
.form-select.is-valid:focus,
.was-validated .form-select:valid:focus,
.form-select.is-invalid:focus,
.was-validated .form-select:invalid:focus {
  border-color: #8480ae;
  box-shadow: none;
}

.form-check-input {
  width: 20px;
  height: 20px;
  margin-top: .25em;
  vertical-align: top;
  background-color: #fff;
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  border: 2px solid #FAB705;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
  box-shadow: 0 7px 15px rgba(0, 0, 0, 0.1);
  -webkit-transition: background-color .15s ease-in-out, background-position .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
  transition: background-color .15s ease-in-out, background-position .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
  transition: background-color .15s ease-in-out, background-position .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
  transition: background-color .15s ease-in-out, background-position .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
}

.form-check-input:focus {
  border-color: #FAB705;
  outline: 0;
  box-shadow: 0 7px 15px rgba(0, 0, 0, 0.1);
}

.form-check-input:checked[type=checkbox] {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%231f0757' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10l3 3l6-6'/%3e%3c/svg%3e");
  background-color: transparent;
  border-color: #FAB705;
}

.form-check label {
  top: 3px;
}

.cursor-pointer {
  cursor: pointer;
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

.account-cta a {
  color: #FF792E;
  text-decoration: underline;
}

.account-cta a:hover {
  color: #1f0757;
}

.forgot-password-link {
  font-size: 14px;
  margin-top: 7px;
  display: block;
  text-align: right;
  color: #FF792E;
  text-decoration: underline;
}

.forgot-password-link:hover {
  text-decoration: underline;
}

section {
	padding-top: 150px;
	padding-bottom: 90px;
}

.custom-invalid-feedback {
  color: #FA5051;
}
</style>

<script>
    import { navigate } from "svelte-routing";
    import TextField from 'ui/TextField.svelte';
    import PasswordField from 'ui/PasswordField.svelte';
    import ButtonTheme from 'ui/ButtonTheme.svelte';
    import Error from 'ui/Error.svelte';
    import {login} from 'js/account.js';
    import {isValidEmail} from 'js/utils.js';
    
    let eMail, password, rememberMe=false;
    let emailClass='', passwordClass='';

    let oPromise;
    let error = {};

    // This function will be called when the email is being entered.
    const handleEmail = () => {
        if(!isValidEmail(eMail)) {
            error.email = 'Enter a valid email address';
        } else {
            emailClass = 'is-valid';
            error.email = '';
        }
    }

    // This function will be called when the password is being entered.
    const handlePassword = () => {
      if(!password.length || password.length < 8) {
        error.password = 'Password must be at least 8 characters long';
      } else {
        passwordClass = 'is-valid';
        error.password = '';
      }
    }

    // This will run whenever an error is encountered.
    $:{
      if(error.email){
        emailClass = 'is-invalid';
      }
      if(error.password){
        passwordClass = 'is-invalid';
      }
    }

    function onLogin(){
          // check if fields are filled or not
          if(!eMail){
            error.email = 'Email is Required';
            emailClass = 'is-invalid';
            return
          }
          if(!password){
            error.password = 'Password is Required';
            passwordClass = 'is-invalid';
            return
          }
        oPromise = login({
            email: eMail,
            password: password,
            rememberMe: rememberMe,
        });
        oPromise.then(()=>{
            // dispatch('loggedIn');
            navigate('/', {replace:false});
        }).catch(function(_error) {
            error = _error
        });
    }
</script>

<!-- Login -->
<section class="login section-padding-150-90 bg-old-lace border-b-orange">

    <div class="container">
        <div class="row">
        <!-- Page Title -->
        <div class="col-12 pt-2 mt-2 pt-md-3 mt-md-5 mb-4 col-md-10 col-lg-8 offset-lg-2 text-center offset-md-1">
            <h2 class="d-inline-block">Login
            <hr class="title-divider" />
            </h2>
        </div>
        </div>

        <!-- Login Form -->
        <form class="needs-validation" novalidate>
        <div class="container">
            <div class="row">
            <div class="col-12 col-md-6 col-lg-4 offset-lg-4 offset-md-3">
                <div class="white-card px-2 px-md-4 py-4 mt-3">
                <div class="row g-3">
					<!-- Email -->
					<div class="col-md-12">
            <TextField
							type='email'
							label='Email'
							placeholder='Johndoe@milinga.com'
							required={true}
							bind:value={eMail}
							error={error.email}
							on:enter={onLogin} 
              on:input={handleEmail}
              customClass={emailClass}
              />
              
              <div class="custom-invalid-feedback">
                {error?.email ? error.email : ''}
                </div>
              </div>
            
                    <!-- Password -->
                    <div class="col-md-12">
						<PasswordField bind:password={password} forgotLink on:input={handlePassword} customClass={passwordClass}/>
              <div class="custom-invalid-feedback">
              {error?.password ? error.password : ''}
              </div>
              <Error error={error.non_field_errors} />
                    </div>

                    <!-- Remember me -->
                    <div class="col-md-12">
                    <div class="mb-0 form-check">
                        <input type="checkbox" class="form-check-input cursor-pointer" bind:checked={rememberMe}>
                        <label class="form-check-label ml-2 cursor-pointer position-relative" for="remember-me">Remember
                        me</label>
                    </div>
                    </div>
                </div>
                </div>
                <!-- Login Button -->
                <div class="row">
                <div class="col-12 mt-4 mb-4">
                    <ButtonTheme fullWidth on:click={onLogin} text="Login" />
                </div>
                </div>
            </div>
            </div>

        </div>
        </form>

        <!-- Account CTA -->
        <div class="row">
        <div class="col-12 col-md-10 text-center col-lg-8 mt-5 offset-lg-2 offset-md-1">
            <p class="account-cta">Don't have account? <a href="javascript:void(0)" on:click={()=>{navigate("/register/")}}>Create new account</a></p>
        </div>
        </div>

    </div>

</section>