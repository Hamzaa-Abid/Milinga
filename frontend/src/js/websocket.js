// import {websocket} from 'js/websocket.js';
// websocket.send('auth_logout', null, {answer:false});
// websocket.sendToOtherMe('piep', 12345);
// websocket.onReceive('piep', function(i){
// 	console.log(i);
// })

import {ReconnectingWebSocket} from 'js/reconnecting-websocket.js';
import {arrayBufferToBlob} from 'js/blob-util.js';
import Event from 'js/Event.js';

class WebSocketClass {
    constructor() {
        this._wsUri = (window.location.protocol=='https:'?'wss':'ws')+"://"+window.location.host+"/ws/";
        // this._wsUri = (window.location.protocol=='https:'?'wss':'ws')+"://www.milinga.com/ws/";
        // this._wsUri = document.body.dataset.wsurl;
        // this._wsUri = "wss://"+window.location.host+"/ws/";
        this._onReceive_received_msgs_before_callback_register = [];
        this._send_msgs_after_connected_cache = []
        this._onReceive_callbacks = {};
        this._send_answer_promises = {};
        this._send_answer_callback_next_id = 1;
        // this._onOpen_callback=[];
        this._init();
    }

    open() {
        this._websocket.open(this._wsUri, null, {binaryType: 'blob'});
    }

    close() {
        this._websocket.close();
    }

    refresh() {
        this._websocket.refresh();
    }
  
    _init() {
        this._websocket = new ReconnectingWebSocket(this._wsUri, null, {binaryType: 'blob'});//, {maxReconnectAttempts:100, maxReconnectInterval:600000, reconnectDecay:5});
        
        this._websocket.onopen = function(evt) {
            Event.dispatch('ws_preopen');
    
            //send cached messages
            for(let i=0; i<this._send_msgs_after_connected_cache.length; i++){
                this._websocket.send(this._send_msgs_after_connected_cache[i]);
            }
            this._send_msgs_after_connected_cache = [];
        }.bind(this);
        
        // this._websocket.onclose = function(evt) { ... }.bind(this);
        
        this._websocket.onmessage = function(evt) {
            let oMessage = JSON.parse(evt.data);
            // if(oMessage == 'stop'){
            //   this._websocket.close();
            // }
            if(oMessage.e){
                console.error(oMessage.t, oMessage.e);
            }
            if(oMessage.f){
                let oPromise = this._send_answer_promises[oMessage.f];
                if(oPromise){
                    if(oMessage.e){
                        oPromise.reject(oMessage.e);
                    } else {
                        oPromise.resolve(oMessage.o);
                    }
                    delete this._send_answer_promises[oMessage.f];
                    return;
                }
            }
    
            let fCallback = this._onReceive_callbacks[oMessage.t];
            if (typeof fCallback === "function"){
                fCallback(oMessage.o);
            } else {
            this._onReceive_received_msgs_before_callback_register.push({
                't' : oMessage.t,
                'o' : oMessage.o,
            })
            }
        }.bind(this);
        this._websocket.onerror = function(evt) { console.error(evt) };
    }
  
    /**
     * This function will receive data from a websocket.
     * 
     * @param {String} sId     The key, to which the function is listening.
     * @param {Function} fCallback  The function, which will be called with the data from the websocket.
     **/
    onReceive(sId, fCallback) {
        for(let i=0; i<this._onReceive_received_msgs_before_callback_register.length; i++){
            if (sId === this._onReceive_received_msgs_before_callback_register[i].key){
            fCallback(this._onReceive_received_msgs_before_callback_register[i].obj);
            }
        }
        this._onReceive_received_msgs_before_callback_register = this._onReceive_received_msgs_before_callback_register.filter(function(oObj){
            return oObj.key !== sId;
        });
        this._onReceive_callbacks[sId] = fCallback;
    }
  
    /**
     * This function sends data to the backend through the websocket.
     * 
     * @param {String} wstype   This is a string like 'chat_sendmsg'. Everything before '_' is the prefix.
     * In this example, 'chat' is the prefix. So in the backend in backend/milinga/consumers.py, the prefix is splitted from the rest by
     * [wstype_prefix, wstype_command] = wstype_split
     * and the corresponding function 'sendmsg' is called in the ChatConsumer.handleWSRequest-Function.
     * @param {Object} obj  This is the object, which will be sent to the backend.
     * @param {Object} last-parameter   If you write {answer = false}, the backend will not send an answer back to the frontend.
     **/
    send(wstype, obj=null, {answer= true, file= undefined} = {}){
        // oObject = {
        //     answer: true,
        //     file: file,
        // }
        let oPromise = undefined;
        let oObject = {
            't':wstype,
            'o':obj,
        };
        if(!(answer === false)){
            let sAnswerPromiseId = this._send_answer_callback_next_id++;
            oObject['f'] = sAnswerPromiseId;
            oPromise = new Promise((resolve, reject)=>{
                this._send_answer_promises[sAnswerPromiseId] = {
                    resolve: resolve,
                    reject: reject,
                }
            });
        }

        let sObj = JSON.stringify(oObject);
        if(file === undefined){
            this._sendRaw(sObj);
        } else {
            this._convertFileToBlob(file)
                .then((fileBlob)=>new Blob([sObj, fileBlob], {type:'application/octed-stream'}))
                .then(this._sendRaw.bind(this));
        }
        
        return oPromise;
    }
    
    /**
     * This function will send data back to all other opened browser windows of the same logged in person.
     * 
     * @param {*} wstype The id, to which the message will be sent.
     * @param {*} obj The data to send.
     */
    sendToOtherMe(wstype, obj) {
        let oObject = {
            't':wstype,
            'o':obj,
            'm':true,
        };
        let sMessage = JSON.stringify(oObject);
        if(this.isOpen() === true) {
            this._websocket.send(sMessage);
        } else {
            this._send_msgs_after_connected_cache.push(sMessage)
        }
    }

    isOpen(){
        return this._websocket.readyState === WebSocket.OPEN;
    }

    _sendRaw(raw){
        if(this.isOpen() == true) {
            this._websocket.send(raw);
        } else {
            this._send_msgs_after_connected_cache.push(raw)
        }
    }

    _convertFileToBlob(file){
        return new Promise((resolve, reject)=>{
            let reader = new FileReader();
            reader.onload = function (evt) {
                var arrayBuffer = evt.target.result;
                let blob = arrayBufferToBlob(arrayBuffer, 'application/octed-stream')
                resolve(blob);
            }.bind(this)
            reader.onerror = function (evt) {
                reject("error reading file");
            }
            reader.readAsArrayBuffer(file);
        })
    }
}
  
export const websocket = new WebSocketClass();
