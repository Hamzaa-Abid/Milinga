/***
 * THIS WEBSOCKET-JAVASCRIPT-FILE DOES NOT OPEN A REAL WEB SOCKET. IT IS JUST FOR DEVELOPMENT MODE
 * WITHOUT A WEBSOCKET. SO THIS FILE RETURNS PREDEFINED DATA INSTEAD OF DATA FROM A REAL WEBSOCKET.
 */
 import Event from 'js/Event.js';

 class WebSocketDevClass {
	 constructor() {
		 setTimeout(()=>{Event.dispatch('ws_preopen');},500);
	 }
 
	 open() {}
 
	 close() {}
 
	 refresh() {}
   
	 /**
	  * This function will receive data from a websocket.
	  * 
	  * @param {String} sId     The key, to which the function is listening.
	  * @param {Function} fCallback  The function, which will be called with the data from the websocket.
	  **/
	 onReceive(sId, fCallback) {
		 console.log("WS onReceive", sId);
		 switch(sId){
		 }
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
		 console.log('WS Request:', wstype, obj)
		 let oPromise = new Promise((resolve, reject)=>{
			 switch(wstype){
				 case 'auth_auth':
					 resolve({
						 "id": 2,
						 "name": "Martin S.",
						 "profilePic": "https://milinga-dev-files.s3.amazonaws.com/media/profilePics/2-4rxqu.jpg",
						 "country": "DE",
						 "isTeacher": true,
						 "description": [
						   "Hello, I am a good teacher! I teach English, Spanish and Greece. If you like to learn one of these languages, book a lesson with me!"
						 ],
						 "videoUrl": "https://www.youtube.com/watch?v=jVlNJOmYkr4",
						 "pricePerHour": "10.00",
						 "currency": "USD",
						 "acceptsBitcoins": false,
						 "acceptsFiat": true,
						 "email": "publinos+milingatest@gmail.com",
						 "emailVerified": true
					 })
					 break;
				 case 'getLang':
					 resolve([{"code": "af", "name_local": "Afrikaans"}, {"code": "ar", "name_local": "\u0627\u0644\u0639\u0631\u0628\u064a\u0651\u0629"}, {"code": "ast", "name_local": "asturianu"}, {"code": "az", "name_local": "Az\u0259rbaycanca"}, {"code": "bg", "name_local": "\u0431\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438"}, {"code": "be", "name_local": "\u0431\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0430\u044f"}, {"code": "bn", "name_local": "\u09ac\u09be\u0982\u09b2\u09be"}, {"code": "br", "name_local": "brezhoneg"}, {"code": "bs", "name_local": "bosanski"}, {"code": "ca", "name_local": "catal\u00e0"}, {"code": "cs", "name_local": "\u010desky"}, {"code": "cy", "name_local": "Cymraeg"}, {"code": "da", "name_local": "dansk"}, {"code": "de", "name_local": "Deutsch"}, {"code": "dsb", "name_local": "dolnoserbski"}, {"code": "el", "name_local": "\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac"}, {"code": "en", "name_local": "English"}, {"code": "en-au", "name_local": "Australian English"}, {"code": "en-gb", "name_local": "British English"}, {"code": "eo", "name_local": "Esperanto"}, {"code": "es", "name_local": "espa\u00f1ol"}, {"code": "es-ar", "name_local": "espa\u00f1ol de Argentina"}, {"code": "es-co", "name_local": "espa\u00f1ol de Colombia"}, {"code": "es-mx", "name_local": "espa\u00f1ol de Mexico"}, {"code": "es-ni", "name_local": "espa\u00f1ol de Nicaragua"}, {"code": "es-ve", "name_local": "espa\u00f1ol de Venezuela"}, {"code": "et", "name_local": "eesti"}, {"code": "eu", "name_local": "Basque"}, {"code": "fa", "name_local": "\u0641\u0627\u0631\u0633\u06cc"}, {"code": "fi", "name_local": "suomi"}, {"code": "fr", "name_local": "fran\u00e7ais"}, {"code": "fy", "name_local": "frysk"}, {"code": "ga", "name_local": "Gaeilge"}, {"code": "gd", "name_local": "G\u00e0idhlig"}, {"code": "gl", "name_local": "galego"}, {"code": "he", "name_local": "\u05e2\u05d1\u05e8\u05d9\u05ea"}, {"code": "hi", "name_local": "\u0939\u093f\u0902\u0926\u0940"}, {"code": "hr", "name_local": "Hrvatski"}, {"code": "hsb", "name_local": "hornjoserbsce"}, {"code": "hu", "name_local": "Magyar"}, {"code": "hy", "name_local": "\u0570\u0561\u0575\u0565\u0580\u0565\u0576"}, {"code": "ia", "name_local": "Interlingua"}, {"code": "id", "name_local": "Bahasa Indonesia"}, {"code": "io", "name_local": "ido"}, {"code": "is", "name_local": "\u00cdslenska"}, {"code": "it", "name_local": "italiano"}, {"code": "ja", "name_local": "\u65e5\u672c\u8a9e"}, {"code": "ka", "name_local": "\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8"}, {"code": "kab", "name_local": "taqbaylit"}, {"code": "kk", "name_local": "\u049a\u0430\u0437\u0430\u049b"}, {"code": "km", "name_local": "Khmer"}, {"code": "kn", "name_local": "Kannada"}, {"code": "ko", "name_local": "\ud55c\uad6d\uc5b4"}, {"code": "lb", "name_local": "L\u00ebtzebuergesch"}, {"code": "lt", "name_local": "Lietuvi\u0161kai"}, {"code": "lv", "name_local": "latvie\u0161u"}, {"code": "mk", "name_local": "\u041c\u0430\u043a\u0435\u0434\u043e\u043d\u0441\u043a\u0438"}, {"code": "ml", "name_local": "Malayalam"}, {"code": "mn", "name_local": "Mongolian"}, {"code": "mr", "name_local": "\u092e\u0930\u093e\u0920\u0940"}, {"code": "my", "name_local": "\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c"}, {"code": "nb", "name_local": "norsk (bokm\u00e5l)"}, {"code": "ne", "name_local": "\u0928\u0947\u092a\u093e\u0932\u0940"}, {"code": "nl", "name_local": "Nederlands"}, {"code": "nn", "name_local": "norsk (nynorsk)"}, {"code": "os", "name_local": "\u0418\u0440\u043e\u043d"}, {"code": "pa", "name_local": "Punjabi"}, {"code": "pl", "name_local": "polski"}, {"code": "pt", "name_local": "Portugu\u00eas"}, {"code": "pt-br", "name_local": "Portugu\u00eas Brasileiro"}, {"code": "ro", "name_local": "Rom\u00e2n\u0103"}, {"code": "ru", "name_local": "\u0420\u0443\u0441\u0441\u043a\u0438\u0439"}, {"code": "sk", "name_local": "Slovensky"}, {"code": "sl", "name_local": "Sloven\u0161\u010dina"}, {"code": "sq", "name_local": "shqip"}, {"code": "sr", "name_local": "\u0441\u0440\u043f\u0441\u043a\u0438"}, {"code": "sr-latn", "name_local": "srpski (latinica)"}, {"code": "sv", "name_local": "svenska"}, {"code": "sw", "name_local": "Kiswahili"}, {"code": "ta", "name_local": "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd"}, {"code": "te", "name_local": "\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41"}, {"code": "th", "name_local": "\u0e20\u0e32\u0e29\u0e32\u0e44\u0e17\u0e22"}, {"code": "tr", "name_local": "T\u00fcrk\u00e7e"}, {"code": "tt", "name_local": "\u0422\u0430\u0442\u0430\u0440\u0447\u0430"}, {"code": "udm", "name_local": "\u0423\u0434\u043c\u0443\u0440\u0442"}, {"code": "uk", "name_local": "\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430"}, {"code": "ur", "name_local": "\u0627\u0631\u062f\u0648"}, {"code": "uz", "name_local": "o\u02bbzbek tili"}, {"code": "vi", "name_local": "Ti\u00ea\u0301ng Vi\u00ea\u0323t"}, {"code": "zh-hans", "name_local": "\u7b80\u4f53\u4e2d\u6587"}, {"code": "zh-hant", "name_local": "\u7e41\u9ad4\u4e2d\u6587"}]);
					 break;
				 case 'profile_get':
					 resolve({
						 "first_name": "John",
						 "last_name": "Doe",
						 "country": "DE",
						 "timezone": "Europe/Berlin",
						 "isTeacher": true,
						 "description": "Hello, I am a good teacher! I teach English, Spanish and Greece. If you like to learn one of these languages, book a lesson with me!",
						 "pricePerHour": "10.00",
						 "currency": "USD",
						 "videoUrl": "https://www.youtube.com/watch?v=jVlNJOmYkr4",
						 "teaches": [
						 14,
						 17,
						 21
						 ]
					   })
					   break;
				 case 'profile_save':
					 setTimeout(resolve, 500);
					 break;
				 case 'subjects_getall':
					 resolve([{"id": 1, "subject": "Afrikaans"}, {"id": 2, "subject": "Arabisch"}, {"id": 3, "subject": "Asturisch"}, {"id": 4, "subject": "Aserbaidschanisch"}, {"id": 5, "subject": "Wei\u00dfrussisch"}, {"id": 6, "subject": "Bulgarisch"}, {"id": 43, "subject": "Ido"}, {"id": 7, "subject": "Bengali"}, {"id": 8, "subject": "Bretonisch"}, {"id": 9, "subject": "Bosnisch"}, {"id": 10, "subject": "Katalanisch"}, {"id": 11, "subject": "Tschechisch"}, {"id": 12, "subject": "Walisisch"}, {"id": 13, "subject": "D\u00e4nisch"}, {"id": 14, "subject": "Deutsch"}, {"id": 15, "subject": "Niedersorbisch"}, {"id": 16, "subject": "Griechisch"}, {"id": 17, "subject": "Englisch"}, {"id": 18, "subject": "Australisches Englisch"}, {"id": 27, "subject": "Estnisch"}, {"id": 19, "subject": "Britisches Englisch"}, {"id": 20, "subject": "Esperanto"}, {"id": 21, "subject": "Spanisch"}, {"id": 22, "subject": "Argentinisches Spanisch"}, {"id": 28, "subject": "Baskisch"}, {"id": 23, "subject": "Kolumbianisches Spanisch"}, {"id": 24, "subject": "Mexikanisches Spanisch"}, {"id": 25, "subject": "Nicaraguanisches Spanisch"}, {"id": 26, "subject": "Venezolanisches Spanisch"}, {"id": 29, "subject": "Persisch"}, {"id": 30, "subject": "Finnisch"}, {"id": 31, "subject": "Franz\u00f6sisch"}, {"id": 32, "subject": "Friesisch"}, {"id": 33, "subject": "Irisch"}, {"id": 34, "subject": "Schottisch-G\u00e4lisch"}, {"id": 35, "subject": "Galicisch"}, {"id": 36, "subject": "Hebr\u00e4isch"}, {"id": 37, "subject": "Hindi"}, {"id": 38, "subject": "Kroatisch"}, {"id": 39, "subject": "Obersorbisch"}, {"id": 40, "subject": "Ungarisch"}, {"id": 41, "subject": "Armenisch"}, {"id": 42, "subject": "Interlingua"}, {"id": 44, "subject": "Indonesisch"}, {"id": 45, "subject": "Isl\u00e4ndisch"}, {"id": 46, "subject": "Italienisch"}, {"id": 47, "subject": "Japanisch"}, {"id": 48, "subject": "Georgisch"}, {"id": 49, "subject": "Kabylisch"}, {"id": 50, "subject": "Kasachisch"}, {"id": 51, "subject": "Khmer"}, {"id": 52, "subject": "Kannada"}, {"id": 53, "subject": "Koreanisch"}, {"id": 54, "subject": "Luxemburgisch"}, {"id": 55, "subject": "Litauisch"}, {"id": 56, "subject": "Lettisch"}, {"id": 57, "subject": "Mazedonisch"}, {"id": 58, "subject": "Malayalam"}, {"id": 59, "subject": "Mongolisch"}, {"id": 60, "subject": "Marathi"}, {"id": 61, "subject": "Birmanisch"}, {"id": 62, "subject": "Norwegian Bokmal"}, {"id": 63, "subject": "Nepali"}, {"id": 64, "subject": "Niederl\u00e4ndisch"}, {"id": 65, "subject": "Norwegisch (Nynorsk)"}, {"id": 66, "subject": "Norwegian"}, {"id": 67, "subject": "Ossetisch"}, {"id": 68, "subject": "Panjabi"}, {"id": 69, "subject": "Polnisch"}, {"id": 70, "subject": "Portugiesisch"}, {"id": 71, "subject": "Brasilianisches Portugiesisch"}, {"id": 72, "subject": "Rum\u00e4nisch"}, {"id": 73, "subject": "Russisch"}, {"id": 74, "subject": "Slowakisch"}, {"id": 75, "subject": "Slowenisch"}, {"id": 76, "subject": "Albanisch"}, {"id": 77, "subject": "Serbisch"}, {"id": 78, "subject": "Serbisch (Latein)"}, {"id": 79, "subject": "Schwedisch"}, {"id": 80, "subject": "Swahili"}, {"id": 81, "subject": "Tamilisch"}, {"id": 82, "subject": "Telugisch"}, {"id": 83, "subject": "Thail\u00e4ndisch"}, {"id": 84, "subject": "T\u00fcrkisch"}, {"id": 85, "subject": "Tatarisch"}, {"id": 86, "subject": "Udmurtisch"}, {"id": 87, "subject": "Ukrainisch"}, {"id": 88, "subject": "Urdu"}, {"id": 89, "subject": "Usbekisch"}, {"id": 90, "subject": "Vietnamesisch"}, {"id": 91, "subject": "Vereinfachtes Chinesisch"}, {"id": 92, "subject": "Traditionelles Chinesisch"}])
					 break;
				 case 'teachers_list':
					 resolve([{"name": "Peter F.", "teaches": [14, 17], "country": "AD", "description": "Hi! I teach German, English and Spanish! I would be happy, if you book a lesson with me!", "videoUrl": "http://youtube.com/watch?v=hYA02UAvwUg", "profilePic": "https://milinga-dev-files.s3.amazonaws.com/media/profilePics/3-8nn93.jpg", "userId": 3, "price50m": "10.00", "currency": "USD", "rating": 4.2}, {"name": "aaa bbb", "teaches": [14, 17], "country": "DE", "description": "test test", "videoUrl": "http://www.youtube.de", "profilePic": "https://milinga-dev-files.s3.amazonaws.com/media/profilePics/6-69xdk.jpg", "userId": 6, "price50m": "15.00", "currency": "USD", "rating": 4.2}, {"name": "Martin S.", "teaches": [14, 17, 21], "country": "DE", "description": "Hello, I am a good teacher! I teach English, Spanish and Greece. If you like to learn one of these languages, book a lesson with me!", "videoUrl": "https://www.youtube.com/watch?v=jVlNJOmYkr4", "profilePic": "https://milinga-dev-files.s3.amazonaws.com/media/profilePics/2-4rxqu.jpg", "userId": 2, "price50m": "10.00", "currency": "USD", "rating": 4.2}]);
			 }
		 });
		 return oPromise;
	 }
	 
	 /**
	  * This function will send data back to all other opened browser windows of the same logged in person.
	  * 
	  * @param {*} wstype The id, to which the message will be sent.
	  * @param {*} obj The data to send.
	  */
	 sendToOtherMe(wstype, obj) {}
 
	 isOpen(){
		 return true;
	 }
 }
   
 export const websocket = new WebSocketDevClass();
 