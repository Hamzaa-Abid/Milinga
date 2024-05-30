//import {userMe} from 'js/account.js';
//$userMe.id !== undefined => logged in

import {websocket} from 'js/websocket.js';
import {writable} from 'svelte/store';
import {ajax, ajaxGetToken, ajaxSetToken, ajaxRemoveToken} from 'js/ajax.js';
import Event from 'js/Event.js';

function createAccountFunctions(){
    let userMe = writable({});

    let authenticated = writable(false);

    Event.addEventListener('ws_preopen', websocketLogin);

    function websocketLogin(){
		let token = ajaxGetToken();
		if(token) {
			websocket.send('auth_auth', {
				key: token,
			}).then(function(oUser){
                userMe.set(oUser);
                authenticated.set(true);
                Event.dispatch('ws_open');
                Event.dispatch('loggedIn');
			}).catch((e)=>{
                // console.log(e);
                authenticated.set(false);
                Event.dispatch('ws_open');
            })
		}
    };
    function websocketLogout(){
        websocket.send('auth_logout');
        // websocket.refresh();
        Event.dispatch('loggedOut');
    }

    return {
        login: ({email, password, rememberMe}) => {
            let oPromise = ajax('rest-auth/login/', {
                'email': email,
                'password': password,
            }, {
                sendToken: false,
            });
            oPromise.then(data=>{
                ajaxSetToken(data.key, rememberMe);
                authenticated.set(true);
                websocketLogin();
                // websocket.refresh();
            }).catch();
            return oPromise;
        },
        register: ({email, password1, password2})=>{
            let oPromise = ajax('rest-auth/registration/', {
                'email': email,
                'password1': password1,
                'password2': password2,
            }, {
                sendToken: false,
            });
            oPromise.then(data=>{
                ajaxSetToken(data.key, false);//rememberMe);
                authenticated.set(true);
                websocketLogin();
                // websocket.refresh();
            }).catch();
            return oPromise;
        },
        confirm_email: ({key})=>{
            let oPromise = ajax('rest-auth/registration/verify-email/', {
                'key': key,
            }, {
                sendToken: false,
            });
            oPromise.then(()=>{
                userMe.update(_user=>({..._user, emailVerified: true,}))
            }).catch();
            return oPromise;
        },
        password_reset:({email})=>{
            let oPromise = ajax('rest-auth/password/reset/', {
                'email': email,
            }, {
                sendToken: false,
            });
            return oPromise;
        },
        password_reset_confirm:({uid, token, new_password1, new_password2,})=>{
            let oPromise = ajax('rest-auth/password/reset/confirm/', {
                'uid': uid,
                'token': token,
                'new_password1': new_password1,
                'new_password2': new_password2,
            }, {
                sendToken: false,
            });
            return oPromise;
        },
        password_change:({new_password1, new_password2, old_password,})=>{
            let oPromise = ajax('rest-auth/password/change/', {
                'new_password1': new_password1,
                'new_password2': new_password2,
                'old_password': old_password,
            });
            return oPromise;
        },
        logout: ()=>{
            ajax('rest-auth/logout/');
            ajaxRemoveToken();
            authenticated.set(false);
            userMe.set({});
            websocketLogout();
            // websocket.refresh();
        },
        passwordReset: ()=>{},
        userMe: userMe,
        authenticated: authenticated,
    }
}

export const {
    login,
    register,
    confirm_email,
    logout,
    password_reset,
    password_reset_confirm,
    password_change,
    userMe,
    authenticated
} = createAccountFunctions();