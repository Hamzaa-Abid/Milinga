## How to install all packages for the website

First we need to install python, pipenv, npm and redis. Redis is for the websocket.

**in the backend-folder:**

`cp .envToCopy .env`

`cp db.sqlite.empty db.sqlite`

`pipenv install`

**in the frontend-folder:**

`npm install`

## How to start the website after installing

After installing everything, we need to start redis for the websocket and then we need to start the django-backend in the backend-folder with:

`pipenv run python ./manage.py runserver`

From this time on, you reach the website at

http://localhost:8000/

If we want to be able to perform background tasks, for example sending eMails, we need to start the workers in the backend-folder with

`pipenv run python ./manage.py run_huey`

If we change the Svelte-code, to test it, we need to run this in the frontend-folder:

`npm run dev`

Later for production, we need to build the optimized and minimized bundle with

`npm run build`

## How the website works

If you build the svelte bundle, it gets copied to the backend/milinga/static - Folder and you will be able to see the updates at http://localhost:8000/ .

All comunication between svelte and django is through a websocket. In svelte, you can make a request by first importing

`import {websocket} from 'js/websocket.js';`

and then for example send something to the server by
```
websocket.send('auth_auth', {
    key: token,
}).then(function(oUser){
    ...
}).catch((e)=>{
    // console.log(e);
    ...
})
```
This will make a websocket request to the backend. 'auth_auth' is the function auth (second auth) with the prefix auth.

In backend/milinga/consumers.py, first the prefix gets extracted in
```
    [wstype_prefix, wstype_command] = wstype_split
```    
and then the function auth (second auth in 'auth_auth') is called in the corresponding consumer.py-file in the function `handleWSRequest`.

The answer in the consumer.py will then be sent back to the javascript-function and will be passed as a result to the promise in 
```
then(function(oUser){...})
```

An error can be cached with
```
catch((e)=>{...})
```


If you have multiple browser windows open and want to send something from one window to all others, where you are logged in, you can use the function 
```
websocket.sendToOtherMe
```

The first parameter is a keyword and the second the data to send.

If you want to listen to a websocket-message, which is not an answer to the websocket.send-function, you can use the function websocket.onReceive.
The first parameter is again the keyword, to which the function is listening, and the second parameter is a function, which will be called with the submitted data.


Here is an example for sending the number 12345 to all other browser windows of the same logged in person:
```
websocket.sendToOtherMe('piep', 12345);
```

If you send it to id 'piep', then you also have to fetch it as id 'piep' in all other browser windows like this:

```
websocket.onReceive('piep', function(i){
	console.log(i);
})
```
