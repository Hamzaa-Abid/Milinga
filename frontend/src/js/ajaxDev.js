function createAjax(){
    let getCookie = function(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    /**
     * 
     * @param {string} url URL to be called
     * @param {Object} data Data to be passed
     * @param {Object} params more parameters like method and sendToken
     * @param {string} params.method Method, for example 'POST'
     * @param {Boolean} params.sendToken If true, the token of the logged in account will also be passed.
     */
    function ajax(url = '', data = {}, {method='POST', sendToken=true,}={}) {
        console.log('AJAX call: ', url, data);
        let oData = data;

        return new Promise((resolve, reject)=>{
            let oRtn = {};
            switch(url){
                case 'rest-auth/login/':
                    oRtn={key:'asdf'};
                    break;
                case 'rest-auth/registration/':
                    oRtn={key:'asdf'};
                    break;
            }
            resolve(oRtn);
        })
    }

    /**
     * Saves the login-token in the localStorage or sessionStorage
     * 
     * @param {string} sToken The token to be saved
     * @param {Boolean} bRememberMe If true, the token will be saved in localStorage, otherwise in sessionStorage.
     */
    function ajaxSetToken(sToken, bRememberMe){
        ajaxRemoveToken();
        if(bRememberMe === true) {
            localStorage.setItem('token', sToken);
        } else {
            sessionStorage.setItem('token', sToken);
        }
    }

    /**
     * All login-tokens will be removed.
     */
    function ajaxRemoveToken(){
        localStorage.removeItem('token');
		sessionStorage.removeItem('token');
    }

    /**
     * Get the login-token
     * 
     * @returns {string} Login-token
     */
    function ajaxGetToken(){
        let sToken = localStorage.getItem("token");
        if(sToken == null) {
            sToken = sessionStorage.getItem("token");
        }
        return sToken;
    }

    return {
        ajax,
        ajaxGetToken,
        ajaxSetToken,
        ajaxRemoveToken,
    }
}

export const {ajax, ajaxGetToken, ajaxSetToken, ajaxRemoveToken} = createAjax();