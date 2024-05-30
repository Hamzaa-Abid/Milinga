import {createOnlineStore} from 'store/onlineStore.js';

function createCreditsStore(){
    let fConvert = o=>({...o, date: new Date(o.date)});

    return createOnlineStore('credits', [], {
        onInit: content=>content.map(fConvert),
        onUpdate: (data, patch)=>[fConvert(patch), ...data],
        storeKeepAliveOnUnsubscribe: true,
        createChannel:false,
        authStore:true,
    });
}
export const credits = createCreditsStore();