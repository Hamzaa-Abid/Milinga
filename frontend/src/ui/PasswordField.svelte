<style>
label {
    width: 100%
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
</style>

<script>
    import {createEventDispatcher} from 'svelte';

    import Error from 'ui/Error.svelte';

    const dispatch = createEventDispatcher();

	let passwordType = 'password';

  const handleInput = () => {
    dispatch('input');
  }

	export let forgotLink=false;
    export let required=false;
    export let password='';
    export let error;
    export let customClass='';
</script>

<label class="form-label" for="password_validation">Password {#if required}<span class="text-radical-red">*</span>{/if}</label>
<div class="position-relative">
	{#if passwordType=='password'}
		<input type="password" bind:value={password} on:input={handleInput} class="form-control pr-5 {customClass}" placeholder="••••••••••" required>
	{:else}
		<input type="text" bind:value={password} on:input={handleInput} class="form-control pr-5 {customClass}" placeholder="••••••••••" required>
	{/if}
	<div class="password-eye" on:click={()=>{passwordType = passwordType=='password'?'text':'password'}}><span><img src="{document.body.dataset.staticurl}img/eye.svg"></span>
	</div>

	<!-- Forgot Password Link -->
	{#if forgotLink == true}
	<a href="forgot-password.html" class="forgot-password-link">Forgot password?</a>
	{/if}
</div>
<div class="invalid-feedback">
	{error}
</div>