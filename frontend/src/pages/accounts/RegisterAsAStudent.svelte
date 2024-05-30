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

/* Shortcodes CSS */

@media only screen and (max-width: 576px) {

  .row>* {
    padding-right: calc(var(--bs-gutter-x)/ 1);
    padding-left: calc(var(--bs-gutter-x)/ 1);
  }
}

.text-summer-sky {
  color: #27AAE1;
}

.border-b-orange {
  border-bottom: 4px solid #FAB705;
}

.text-radical-red {
  color: #FA5051;
}

.bg-old-lace {
  background: #FFF6E9;
}

.section-divider {
  background: #FFBD94;
  height: 2px !important;
  opacity: 1;
  width: 100%;
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

@media all and (-ms-high-contrast: none),
(-ms-high-contrast: active) {

  .row>* {
    padding: 0 15px;
    margin-top: 35px;
  }
}

.custom-invalid-feedback {
  color: #FA5051;
}

.is-invalid,
.was-validated .form-control:invalid,
.is-valid,
.was-validated .form-control:valid {
  background-image: none;
}

.is-valid,
.was-validated .form-control:valid,
.form-select.is-valid,
.was-validated .form-select:valid {
  border-color: #80C43B;
}

.is-invalid,
.was-validated .form-control:invalid,
.form-select.is-invalid,
.was-validated .form-select:invalid {
  border-color: #FA5051;
}

.form-select.is-valid,
.was-validated .form-select:valid,
.form-select.is-invalid,
.was-validated .form-select:invalid {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23343a40' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
}


.white-card {
  background-color: #fff;
  box-shadow: 0 20px 35px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
}

.currency-sign {
  position: absolute;
  top: 9px;
  left: 14px;
  border-right: 1px solid #ced4da;
  padding-right: 12px;
}

.currency-sign span {
  position: relative;
  top: 1px;
  color: #D3D3D3;
}

.password-eye {
  position: absolute;
  top: 8px;
  right: 14px;
  border-left: 1px solid #ced4da;
  padding-left: 12px;
  cursor: pointer;
}

.password-eye span {
  position: relative;
  top: 2px;
  color: #D3D3D3;
}

.registration-title span:before {
  content: "";
  position: absolute;
  display: block;
  height: 26px;
  background: #E3E3E3;
  width: 3px;
  border-radius: 10px;
  left: 20px;
  top: 3px;
}

@media only screen and (max-width: 767px) {
  .registration-title span:before {
    left: 9px;
  }
}

section {
	padding-top: 150px;
	padding-bottom: 90px;
}
</style>

<script>
    import { navigate } from "svelte-routing";
    import ButtonTheme from 'ui/ButtonTheme.svelte';
    import Error from 'ui/Error.svelte';
    import {isValidEmail,togglePasswordVisibility} from 'js/utils.js';
    import {register} from 'js/account.js';
 
    let eMail, password1, password2;
    let emailClass='', password1Class='', password2Class='';
    let error = {};
    let oPromise;

    // This function will be called when the email is being entered.
    const handleEmail = (e) => {
        let value = e.target.value;
        if(!isValidEmail(value)) {
            error.email = 'Enter a valid email address';
        } else {
            emailClass = 'is-valid';
            error.email = '';
        }
    }

    // This function will be called when the password1 is being entered.
    const handlePassword1 = (e) => {
      let value = e.target.value;
      if(!value.length || value.length < 8) {
        error.password1 = 'Password must be at least 8 characters long';
      } else {
        password1Class = 'is-valid';
        error.password1 = '';
      }
    }

    // This function will be called when the password2 is being entered.
    const handlePassword2 = (e) => {
      let value = e.target.value;
      if(!value.length || value !== password1) {
        error.password2 = 'Passwords don´t match!';
      } else {
        password2Class = 'is-valid';
        error.password2 = '';
      }
    }

    // This will run whenever an error is encountered.
    $:{
      if(error.email){
        emailClass = 'is-invalid';
      }
      if(error.password1){
        password1Class = 'is-invalid';
      }
      if(error.password2){
        password2Class = 'is-invalid';
      }
    }

    function onRegister(){
          // check if fields are filled or not
          if(!eMail){
            error.email = 'Email is Required';
            emailClass = 'is-invalid';
            return
          }
          if(!password1){
            error.password1 = 'Password is Required';
            password1Class = 'is-invalid';
            return
          }
          if(!password2){
            error.password2 = 'Confirm Password is Required';
            password2Class = 'is-invalid';
            return
          }

          oPromise = register({
            email: eMail,
            password1: password1,
            password2: password2,
          });
          oPromise.then(()=>{
            // dispatch('loggedIn');
            navigate('/profile', {replace:false});
          }).catch(function(_error) {
            error = _error
          });
    }
</script>

<!-- Student Registration -->
<section class="registration section-padding-150-90 bg-old-lace border-b-orange">
<!-- Student Registration Form -->
    <form class="needs-validation" novalidate>
        <div class="container">
        <div class="row">

            <!-- Page Title -->
            <div class="col-12 col-md-10 col-lg-8 offset-lg-2 offset-md-1">
            <h4 class="registration-title">Registration <span class="position-relative text-summer-sky pl-md-5 pl-4">As
                a Student</span>
            </h4>
            </div>
        </div>
        <!-- divider -->
        <div class="row">
            <div class="col-12 col-md-10 col-lg-8 my-4 offset-lg-2 offset-md-1">
            <hr class="section-divider" />
            </div>
        </div>

        <!-- Sub Heading -->
        <div class="row">
            <div class="col-12 col-md-6 col-lg-4 offset-lg-4 offset-md-3">
            <h5 class="mb-4">About</h5>
            </div>

            <div class="container align-items-center justify-content-center my-4">
              <div class="row">
            <div class="col-12 col-md-6 col-lg-4 offset-lg-4 offset-md-3">
            <div class="white-card px-2 px-md-4 py-4 mt-3">
                <div class="row  g-3">
                <!-- Email -->
                <div class="col-md-12">
                    <label class="form-label" for="email_validation">Email <span class="text-radical-red">*</span></label>
                    <input type="email" class="form-control {emailClass}" placeholder="Johndoe@milinga.de" id="email_validation"
                    required bind:value={eMail} on:input={handleEmail}>
                    
                    <div class="custom-invalid-feedback">
                    {error?.email ? error.email : ''}
                    </div>
                </div>
                <!-- Password -->
                <div class="col-md-12">
                    <label class="form-label" for="password_validation">Password <span
                        class="text-radical-red">*</span></label>
                    <div class="position-relative">
                    <input type="password" class="form-control pr-5 {password1Class}" bind:value={password1} on:input={handlePassword1} placeholder="••••••••••" id="password_validation1" required>
                    <div class="password-eye toggle-password" on:click={() => togglePasswordVisibility('#password_validation1')}><span><img src="{document.body.dataset.staticurl}img/eye.svg" alt="toggle"></span>
                    </div>
                    </div>

                    <div class="custom-invalid-feedback">
                    {error?.password1 ? error.password1 : ''}
                    </div>
                </div>

                <!-- Confirm Password -->
                <div class="col-md-12">
                  <label class="form-label" for="password_validation">Confirm Password<span
                      class="text-radical-red">*</span></label>
                  <div class="position-relative">
                  <input type="password" class="form-control pr-5 {password2Class}" bind:value={password2} on:input={handlePassword2} placeholder="••••••••••" id="password_validation2"
                      required>
                  <div class="password-eye toggle-password" on:click={() => togglePasswordVisibility('#password_validation2')}><span><img src="{document.body.dataset.staticurl}img/eye.svg" alt="toggle"></span>
                  </div>
                  </div>

                  <div class="custom-invalid-feedback">
                    {error?.password2 ? error.password2 : ''}
                  </div>
               </div>
               <Error error={error.non_field_errors} />

                </div>
            </div>
            <!-- Registration Button -->
        <div class="row">
          <div class="col-12 mt-4 mb-4">
            <ButtonTheme fullWidth on:click={onRegister} text="Register" type="submit" />
          </div>
      </div>
            </div>
        </div>
      </div>
    </div>
        
        </div>
    </form>
</section>