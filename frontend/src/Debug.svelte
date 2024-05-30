<script>
    import {websocket} from 'js/websocket.js';
    import TextField from 'ui/TextField.svelte';
    import TextArea from 'ui/TextArea.svelte';
    import Button from 'ui/Button.svelte';

	// websocket on/off debug
	let websocketOpened = true;
	function websocketOpenCloseToggle(){
		websocketOpened=!websocket.isOpen();
		if(websocket.isOpen()===true){
			websocket.close();
		} else {
			websocket.open();
		}
    }
    
    let wsMethod = 'getCSRFToken';
    let wsObject = '';
    let wsAnswer = '';

    function send(){
        websocket.send(wsMethod, wsObject.trim()!=''?JSON.parse(wsObject):null).then(o=>wsAnswer=JSON.stringify(o));
    }
</script>

<div class="d-flex align-items-center"><button on:click={websocketOpenCloseToggle}>{websocketOpened === true?'close':'open'} websocket</button></div>

<TextField
    type='text'
    label='websocket method'
    placeholder='getToken'
    required={true}
    bind:value={wsMethod} />

<TextArea
    label='Object'
    required={true}
    bind:value={wsObject} />

<Button on:click={send} text="send" />

<TextArea
    label='Answer'
    required={false}
    bind:value={wsAnswer} />
