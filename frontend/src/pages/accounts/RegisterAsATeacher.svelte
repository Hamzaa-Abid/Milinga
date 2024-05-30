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


.border-b-orange {
  border-bottom: 4px solid #FAB705;
}

.text-yellow-green {
  color: #80C43B;
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

.invalid-feedback {
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
    import { createEventDispatcher } from 'svelte';
    import { faUserPlus } from '@fortawesome/free-solid-svg-icons';

    import TextField from 'ui/TextField.svelte';
    import CheckBox from 'ui/CheckBox.svelte';
    //import Button from 'ui/Button.svelte';
    import ButtonTheme from 'ui/ButtonTheme.svelte';
    import Error from 'ui/Error.svelte';
    import Link from 'ui/Link.svelte';

    // import {websocket} from 'js/websocket.js';
    // import {preferences} from 'store/preferences.js';
    // import {users} from 'store/users.js';
    import {register} from 'js/account.js';

    // const dispatch = createEventDispatcher();
    
    let eMail, password1, password2;

    // eMail='masrlinu+milinga@gmail.com';
    // password1='crashdown';

    let error = {};

    let oPromise;

    function onRegister(){
        // if(password1 != password2){
        //     error = {password2: "Passwords don´t match!"};
        //     return;
        // }
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

  <!-- Teacher Registration -->
  <section class="registration section-padding-150-90 bg-old-lace border-b-orange">
    <!-- Teacher Registration Form -->
    <form class="needs-validation" novalidate>

      <div class="container">
        <div class="row">
          <!-- Page Title -->
          <div class="col-12 col-md-10 col-lg-8 offset-lg-2 offset-md-1">
            <h4 class="registration-title">Registration <span
                class="position-relative text-yellow-green pl-md-5 pl-4">Become a Teacher</span>
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
          <div class="col-12 col-md-10 col-lg-8 offset-lg-2 offset-md-1">
            <h5 class="mb-4">About</h5>
          </div>

          <div class="col-12 col-md-10 col-lg-8 offset-lg-2 offset-md-1">
            <div class="white-card px-2 px-md-4 py-4 mt-3">
              <div class="row g-3">
                <!-- First Name -->
                <div class="col-md-6">
                  <label class="form-label" for="fname_validation">First Name <span
                      class="text-radical-red">*</span></label>
                  <input type="text" class="form-control lg" placeholder="John" id="fname_validation" required>
                  <div class="invalid-feedback">
                    Please enter your first name here.
                  </div>
                </div>
                <!-- last Name -->
                <div class="col-md-6">
                  <label class="form-label" for="lname_validation">Last Name <span
                      class="text-radical-red">*</span></label>
                  <input type="text" class="form-control" placeholder="Doe" id="lname_validation" required>

                  <div class="invalid-feedback">
                    Please enter your last name here.
                  </div>
                </div>
                <!-- Email -->
                <div class="col-md-6">
                  <label class="form-label" for="email_validation">Email <span class="text-radical-red">*</span></label>
                  <input type="email" class="form-control" placeholder="Johndoe@milinga.de" id="email_validation"
                    required>

                  <div class="invalid-feedback">
                    Please enter correct email here.
                  </div>
                </div>
                <!-- Password -->
                <div class="col-md-6">
                  <label class="form-label" for="password_validation">Password <span
                      class="text-radical-red">*</span></label>

                  <div class="position-relative">
                    <input type="password" class="form-control pr-5" placeholder="••••••••••" id="password_validation"
                      required>
                    <div class="password-eye toggle-password"><span><img src="{document.body.dataset.staticurl}img/eye.svg"></span>
                    </div>
                  </div>

                  <div class="invalid-feedback">
                    Please enter password here.
                  </div>
                </div>
                <!-- Where Are you from -->
                <div class="col-md-6">
                  <label class="form-label" for="cont_validation">Where are you from <span
                      class="text-radical-red">*</span></label>
                  <select class="form-select" id="cont_validation" required>
                    <option selected disabled value="">Select Country</option>
                    <option>Germany</option>
                    <option>England</option>
                    <option>Russia</option>
                  </select>
                  <div class="invalid-feedback">
                    Please select a valid country.
                  </div>
                </div>
                <!-- Timezone -->
                <div class="col-md-6">
                  <label class="form-label" for="cont_timezone">Timezone<span class="text-radical-red">*</span></label>
                  <select class="form-select" id="cont_timezone" required>
                    <option selected disabled value="">(UTC + 05:00) Islamabad, Karachi</option>
                    <option>(UTC + 03:00) Islamabad, Karachi</option>
                    <option>(UTC + 04:00) Islamabad, Karachi</option>
                    <option>(UTC + 05:00) Islamabad, Karachi</option>
                  </select>
                  <div class="invalid-feedback">
                    Please select a valid country.
                  </div>
                </div>
                <!-- I teach -->
                <div class="col-md-6">
                  <label class="form-label" for="teach_validation">I teach <span
                      class="text-radical-red">*</span></label>
                  <input type="text" class="form-control lg" placeholder="German, English, Spanish"
                    id="teach_validation" required>
                  <div class="invalid-feedback">
                    Please write the language.
                  </div>
                </div>
                <!-- Also Speaks -->
                <div class="col-md-6">
                  <label class="form-label" for="speak_validation">I also speak</label>
                  <input type="text" class="form-control" placeholder="Russian" id="speak_validation" required>

                  <div class="invalid-feedback">
                    Please write the language.
                  </div>

                </div>
                <!-- Description -->
                <div class="col-md-12">
                  <label for="descrip_validation">Description<span class="text-radical-red">*</span></label>
                  <textarea class="form-control" rows="5" minlength="50" maxlength="200"
                    id="descrip_validation" required></textarea>
                  <div class="invalid-feedback">
                    Please fill the description here.
                  </div>
                </div>
                <!-- Video URL -->
                <div class="col-md-6">
                  <label class="form-label" for="video_validation">Video URL <span
                      class="text-radical-red">*</span></label>
                  <input type="url" class="form-control lg" placeholder="www.youtube.com/watch?v=yAoLSRbwxL8"
                    id="video_validation" required>
                  <div class="invalid-feedback">
                    Please enter correct URL.
                  </div>
                </div>
                <!-- Price -->
                <div class="col-md-6 ">
                  <label class="form-label" for="price_validation">Price in USD per hour <span
                      class="text-radical-red">*</span></label>
                  <div class="position-relative">
                    <div class="currency-sign"><span>$</span></div>
                    <input type="text" class="form-control pl-5" id="price_validation" placeholder="18" required>
                  </div>
                  <div class="invalid-feedback">
                    Please enter price here.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Registration Button -->
        <div class="row">
			<div class="col-12 col-md-10 text-md-right text-center col-lg-8 mt-5 offset-lg-2 offset-md-1">
				<ButtonTheme on:click={onRegister} text="Register" />
			</div>
        </div>

      </div>

    </form>

  </section>

<!-- <div class="container align-items-center justify-content-center my-4">
    <div class="row">
        <div class="col-lg-4 offset-lg-4 col-md-6 offset-md-3 col-sm-8 offset-sm-2 col-12">
            <div class="page-header">
                <h1 class="text-wrap text-sm-nowrap text-md-nowrap text-lg-nowrap">Registrieren</h1>
            </div>
            <p>Du hast bereits ein Konto bei uns? Dann bitte <Link to="/login/" blue>hier entlang</Link>.</p>
    
            <div class="mb-3">
                <TextField
                    type='email'
                    label='E-Mail'
                    placeholder='E-Mail-Adresse'
                    required={true}
                    bind:value={eMail}
                    error={error.email}
                    on:enter={onRegister} />
                
                <TextField
                    type='password'
                    label='Passwort'
                    placeholder='Passwort'
                    required={true}
                    bind:value={password1}
                    error={error.password1}
                    on:enter={onRegister} />
                
                <TextField
                    type='password'
                    label='Passwort (wiederholen)'
                    placeholder='Passwort'
                    required={true}
                    bind:value={password2}
                    error={error.password2}
                    on:enter={onRegister} />

                <Error error={error.non_field_errors} />
                <Error error={error.connection} />
                <Button on:click={onRegister} promise={oPromise} icon={faUserPlus} text="Registrieren"/>
            </div>
        </div>
    </div>
</div> -->