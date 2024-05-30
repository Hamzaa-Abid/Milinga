// import {subjects} from 'store/subjects.js';
// $subjects.subject / $subjects.id

// #import {createOnlineStore} from './onlineStore.js';
// #export const subjects = createOnlineStore('subjects', [], {storeKeepAliveOnUnsubscribe: true, reloadOnConnectionLoss:false});

import { readable } from 'svelte/store';
import { websocket } from 'js/websocket.js';
import {languageCode} from 'store/languages.js';
// import { preferences } from 'store/preferences.js';
// import { createOnlineStore } from './onlineStore';

function createSubjectsStore(){
	var langCode;
	var oSubjects=[];
	
	return readable(oSubjects, function start(set) {
		let unsubscribeLanguageCode = languageCode.subscribe((_langCode)=>{
			if(langCode != _langCode) {
				langCode=_langCode;
				let _langCodeRequest = _langCode;
				websocket.send('subjects_getall', {lang: _langCodeRequest, }, {noDoubeRequest: true,}).then(function(_oSubjects){
					if(langCode === _langCodeRequest){
						set(_oSubjects);
						oSubjects = _oSubjects;
					}
				})
			}
		});
		return function stop() {
			unsubscribeLanguageCode();
		};
	});
}

export const subjects = createSubjectsStore();