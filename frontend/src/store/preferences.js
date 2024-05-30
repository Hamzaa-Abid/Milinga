// import {preferences} from 'store/preferences.js';
//
// preferences.set(key, value)
// preferences.setMultiple({
//     key: value,
//     key2: value2,
// })
//
// let value = $preferences.key

/*
import { writable } from 'svelte/store';

function createPreferences() {
	const { subscribe, update, set} = writable({languageCode: navigator.language.slice(0,2),});

	return {
		subscribe,
		set: (key, value) => {update((prefs)=>{
            prefs[key] = value;
            return prefs;
        })},
        setMultiple: (oKeyValueList) => {
            update((prefs)=>{
                for(let key in oKeyValueList){
                    prefs[key] = oKeyValueList[key];
                }
                return prefs;
            })
        },
        invalidate: ()=>set({languageCode: navigator.language.slice(0,2),}),
    };
}

export const preferences = createPreferences();
*/