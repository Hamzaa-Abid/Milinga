



export const isValidEmail = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}


export const togglePasswordVisibility = (id) => {
    let passwordInput = document.querySelector(id);
    if(passwordInput.type === 'password'){
      passwordInput.type = 'text';
    }else{
      passwordInput.type = 'password';
    }
}