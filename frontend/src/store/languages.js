// import {languages} from 'store/languages.js';
// $languages.languageCode / $languages.name_local

import { readable, writable } from 'svelte/store';
import { websocket } from 'js/websocket.js';

function createLanguageStore(){
	var oLanguages=[];

	let languages = readable(oLanguages, function start(set) {
		if(oLanguages.length === 0){
			websocket.send('getLang').then(function(_oLanguages){
				set(_oLanguages);
				oLanguages = _oLanguages;
			})
		}
		return function stop() {};
	});
	let languageCode = writable(navigator.language.slice(0,2));

	return {languages, languageCode};
}

export const {languages, languageCode} = createLanguageStore();