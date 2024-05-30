/**
 * Call a function, if the window has the focus for more than the specified milliseconds. A chatmessage can be marked as read with this function for example.
 */
function createOnFocusTime(){
    let id=0;
    let oCallbacks = [];

    function _setFocusTimeout(oCallback){
        oCallback.timeout = setTimeout(()=>{
            oCallback.callback();
            if(oCallback.repeat != true){
                oCallbacks = oCallbacks.filter(o=>o.id != oCallback.id);
            }
        }, oCallback.seconds);
    }

    function _clearFocusTimeout(oCallback){
        clearTimeout(oCallback.timeout);
    }

    function _onFocus(){
        oCallbacks.forEach(o=>_setFocusTimeout(o));
    }

    function _onBlur(){
        oCallbacks.forEach(_clearFocusTimeout);
    }

    window.addEventListener("focus", () => _onFocus());
    window.addEventListener("blur", () => _onBlur());

    if(document.hasFocus()===true){
        _onFocus();
    }

    return {
        /**
         * This function measures, how long this website has the focus. If it has the focus for more than iFocusMilliSeconds seconds, it calls the function fCallback.
         * With the help of this function, you for example are able to mark a new chat message as read, if this website has the focus for a long enough time.
         * 
         * @param {seconds} iFocusMilliSeconds Number of milliseconds, this website should have the focus, before fCallback gets called.
         * @param {Function} fCallback The callback-function, which gets called.
         * @param {Boolean} bRepeat If true, fCallback gets called again, if this website loses focus and gets focus again for more than iFocusMilliSeconds seconds.
         * 
         * @returns {Function} If you call this function, the submitted fCallback will not be called.
         * 
         * @example
         * // makes an alert, everytime, the window focus is lost and the window gets the focus for more than 1 second
         * import {onFocusTime, focusTimeDestroy} from 'store/focus.js';
         * let stop = onFocusTime(1000, function(){
         *  alert('focus länger als 1 Sekunde!');
         * }, true)
         * stop();  //stops the focus manually
         * onDestroy(focusTimeDestroy); //stops all timers on svelte component destroy
         */
        onFocusTime: (iFocusMilliSeconds, fCallback, bRepeat)=>{
            let oCallback = {
                id: id++,
                seconds: iFocusMilliSeconds,
                callback: fCallback,
                repeat: bRepeat,
            }
            if(document.hasFocus()===true) {
                _setFocusTimeout(oCallback)
            }
            oCallbacks.push(oCallback);
            return ()=>{
                _clearFocusTimeout(oCallback);
                oCallbacks = oCallbacks.filter(o=>o.id != oCallback.id);
            }
        },

        /**
         * This function stopps all callbacks from getting called.
         */
        focusTimeDestroy: ()=>{
            oCallbacks.forEach(_clearFocusTimeout);
            oCallbacks=[];
        },
    };
}

export const {onFocusTime, focusTimeDestroy} = createOnFocusTime();