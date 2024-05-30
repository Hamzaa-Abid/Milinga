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
        let oData = data;
        
        let oHeaders = {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        };
        let token = ajaxGetToken();
        if (token && sendToken===true){
            oHeaders['Authorization'] = "Token " + token;
        }

        // Default options are marked with *
        return new Promise((resolve, reject)=>{
            fetch(document.location.origin + '/' + url, {
                method: method, // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: oHeaders,
                redirect: 'follow', // manual, *follow, error
                referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                body: JSON.stringify(oData), // body data type must match "Content-Type" header
            }).then(function(response) {
                response.json().then(responseJson=>{
                    if (!response.ok) {
                        reject(responseJson);
                    } else {
                        resolve(responseJson);
                    }
                });
            }).catch(e=>reject({connection:'no connection'}));
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