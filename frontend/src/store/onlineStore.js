// import {createOnlineStore} from 'store/onlineStore.js';
// createOnlineStore('credits', [], {
//     onUpdate: (data, patch)=>data=[...data, patch],
//     createChannel:false,
//     storeKeepAliveOnUnsubscribe: false,
//     reloadOnConnectionLoss:true,
//     authStore:false,
// });

import { writable, get } from 'svelte/store';
import { websocket } from 'js/websocket.js';
import {authenticated} from 'js/account.js';
import Event from 'js/Event.js';

function createOnlineStoreFactory(){

    let oStores={};
    
    return function createOnlineStore(sId='', initialData=[], {
            onInit=data=>data,
            onUpdate=(data, patch)=>{if(typeof data ==='object'){data.push(patch);return data;} else return patch },      //Update-Funktion
            createChannel=false,                //Extra Channel, oder werden Daten sowieso geschickt?
            storeKeepAliveOnUnsubscribe=false,
            reloadOnConnectionLoss=true,
            authStore=false,                    //Contains just data when authenticated
        }={}) {
            
        let oStore = oStores[sId];
        if(oStore === undefined){
            oStore = writable(initialData, function start(set) {
                set(initialData);
                if(storeKeepAliveOnUnsubscribe===true) oStore.subscribe(x=>null);

                let sIdSend = (createChannel===true?'subscribe_':'get_')+sId;
                let fetchData = ()=>{
                    if((authStore!=true || get(authenticated)===true)&&websocket.isOpen()===true){
                        websocket.send(sIdSend).then(content=>set(onInit(content, get(oStore))));
                    } else {
                        set(initialData);
                    }
                }
                
                let onStopHandlers=[];

                if(authStore===true){
                    onStopHandlers.push(Event.addEventListener('loggedIn', fetchData));
                    onStopHandlers.push(Event.addEventListener('loggedOut', ()=>set(initialData)));
                    fetchData();
                }
                fetchData();
                if(reloadOnConnectionLoss===true){
                    onStopHandlers.push(Event.addEventListener('ws_open', fetchData));
                }
                websocket.onReceive('update_'+sId, function(_patch){
                    if(typeof onUpdate === 'function') {
                        set(onUpdate(get(oStore), _patch));
                    } else {
                        set(_patch)
                    }
                });
            
                return function stop() {
                    if(createChannel===true){
                        websocket.send('unsubscribe_'+sId);
                    }
                    onStopHandlers.forEach(f=>f());
                    onStopHandlers=[];
                    delete(oStores[sId]);
                };
            });
            oStores[sId] = oStore;
        }
        return oStore;
    }
}

export const createOnlineStore = createOnlineStoreFactory();