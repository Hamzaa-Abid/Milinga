<script>
    import {get} from 'svelte/store';
    import { createCrossfade } from 'transitions/crossfade.js';
    import {tick} from 'svelte';

    import { flip } from 'svelte/animate';
	import { quintOut } from 'svelte/easing';

    import Fa from 'svelte-fa';
    import {faPlus, faMinus, faCheck, faTrashAlt} from '@fortawesome/free-solid-svg-icons';

    import {users} from 'store/users.js';
    import {credits} from 'store/credits.js';
    import {websocket} from 'js/websocket.js';
    import {creditsTotal} from 'store/creditsTotal.js';
    // import {connectedPeople} from 'store/connectedPeople.js';
    import {userMe} from 'js/account.js';

    import Clickable from 'ui/Clickable.svelte';
    import Contact from 'ui/Contact.svelte';
    import NumberInput from 'ui/NumberInput.svelte';

    let {send, receive} = createCrossfade({duration: 300});

    function addCredits(oCredits){
        let oPromise=websocket.send('credits_give', {
            to: oCredits.userId,
            credits: oCredits.add,
        })

        $credits = [{
            id: oCredits.id,
            date: new Date(),
            credits: oCredits.add,
            teacherId: $userMe.id,
            ownerId: oCredits.userId,
            sentPromise: oPromise,
        }, ...$credits];

        oCredits.add=0;
        oCredits.id=Math.random();
    }

    function deleteCredits(oCredits){
        addCredits({
            ...oCredits,
            userId: oCredits.ownerId,
            add: -oCredits.credits,
            id: Math.random(),
        })
    }

    let oCreditsTotal = [];
    $: $userMe.isTeacher, $creditsTotal, updateCreditsTotal();
    function updateCreditsTotal(){
        let sAttr = $userMe.isTeacher===true? 'myStudentCreditsArray' : 'myCreditsArray';
        $creditsTotal[sAttr].filter(oNew=>{
            let i = oCreditsTotal.findIndex(oOld=>oOld.userId==oNew.userId);
            if(i==-1){
                oCreditsTotal = [...oCreditsTotal, {...oNew, add: 0, id: Math.random(),},];
            } else {
                oCreditsTotal[i] = {...oCreditsTotal[i], credits: oNew.credits,};
            }
        });
    };

    let oCredits = [];
    $: $userMe.isTeacher, $credits, updateCredits();
    function updateCredits(){
        let sUserAttr = $userMe.isTeacher===true? 'teacherId' : 'ownerId';
        oCredits = $credits.filter(o=>o[sUserAttr] === $userMe.id);
    };
</script>

<style>
/*erstes und letztes Tabellen-Element mittig darstellen*/
/* th:last-child, td:last-child{
    text-align:center;
} */
/* td{
    align-items:center;
} */
</style>

<div class="container w-100 justify-content-center my-4">
    <h3>Total credits:</h3>
    <table class="table">
        <thead>
            <tr>
                <th scope="col" style="text-align: left;">{$userMe.isTeacher === true?'Student':'Teacher'}</th>
                <th scope="col" style="text-align: center;">{$userMe.isTeacher===true?'Student\'s':'your'} Credits</th>
                {#if $userMe.isTeacher === true}
                <th scope="col" style="text-align: center;">add/remove Credits</th>
                <th></th>
                {/if}
            </tr>
        </thead>
        <tbody>
            {#each oCreditsTotal as oCT (oCT.id)}
                <tr>
                    <td style="text-align: left;"><Contact {...$users[oCT.userId]} /></td>
                    <td style="text-align: center;" width="20%">
                        <span class={`badge rounded-pill bg-${oCT.credits<0?'danger':'success'}`} style="font-size:1.4rem">{oCT.credits}</span>
                        {#if oCT.add != 0}
                            <span out:send={{key: 'payment'+oCT.id}}
                                class={`badge rounded-pill bg-${oCT.add<0?'danger':'success'}`}
                                style={"font-size:1rem"}>
                                    {oCT.add<0?'':'+'}{oCT.add}
                            </span>
                        {/if}
                    </td>
                    {#if $userMe.isTeacher === true}
                    <td style="text-align: center;" class="text-nowrap">
                        <button type="button" class="btn btn-outline-danger" on:click={()=>oCT.add--}><Fa icon={faMinus} size="1.5x" color="red"/></button>
                        <button type="button" class="btn btn-outline-success" on:click={()=>oCT.add++}><Fa icon={faPlus} size="1.5x" color="green"/></button>
                    </td>
                    <td style="text-align: center;">
                        <button type="button" class="btn btn-outline-success ml-1" style={`visibility: ${oCT.add==0?'hidden':'visible'};`} on:click={()=>addCredits(oCT)}><Fa icon={faCheck} size="1.5x" color="green"/></button>
                    </td>
                    {/if}
                </tr>
            {/each}
        </tbody>
    </table>


    <h3 class="mt-5">Payment history:</h3>
    <table class="table">
        <thead>
            <tr>
                <th scope="col"></th>
                <th style="text-align: left;" scope="col">Date</th>
                <th style="text-align: center;" scope="col">{$userMe.isTeacher === true?'Student':'Teacher'}</th>
                <th style="text-align: center;" scope="col">{$userMe.isTeacher===true?'Student\'s':'your'} Credits</th>
            </tr>
        </thead>
        <tbody>
            {#each oCredits as oC, i (oC.id)}
                <tr animate:flip = {{delay: 0, duration: 1000, easing: quintOut}}>
                    <td><Clickable on:click={()=>deleteCredits(oC)} tooltip='delete' tooltipPlacement='top'><Fa icon={faTrashAlt} size="1.5x"/></Clickable></td>
                    <td style="text-align: left;">{oC.date.toLocaleDateString()}</td>
                    <td style="text-align: center;"><Contact {...$users[oC.ownerId]} /></td>
                    <td style="text-align: center;"><span in:receive={{key: 'payment'+oC.id}} class={`badge rounded-pill bg-${oC.credits<0?'danger':'success'}`} style="font-size:1.4rem">{oC.credits}</span></td>
                </tr>
            {/each}
        </tbody>
    </table>

</div>
