<script>
    import { onDestroy } from 'svelte';
    // import { navigate } from "svelte-routing";
    
    import {websocket} from 'js/websocket.js';
    // import {users} from 'store/users.js';
    import {userMe} from 'js/account.js';
    import {myEvents, myWorkingTime} from 'store/calendar.js';
    import {color} from './js/color.js';
    import { getContext } from 'svelte';

    import ModalLessonAccept from './ui/ModalLessonAccept.svelte';
    import ModalLessonInfo from './ui/ModalLessonInfo.svelte';
    import Calendar from 'ui_dyn/calendar/ui/Calendar.svelte';

    const { open } = getContext('simple-modal');

    // let workingTimes = [];

    // let workingTimes=[];
    // let unsubscribeMyWorkingTimes=()=>null;
    // let unsubscribeUserMe = userMe.subscribe(oUserMe=>{
    //     if(oUserMe.isTeacher){
    //         unsubscribeMyWorkingTimes();
    //         unsubscribeMyWorkingTimes = myWorkingTime.subscribe(_workingTimes=>workingTimes=_workingTimes);
    //     } else {
    //         unsubscribeMyWorkingTimes();
    //         unsubscribeMyWorkingTimes=()=>null;
    //     }
    // })
    // onDestroy(function(){
    //     unsubscribeUserMe();
    //     unsubscribeMyWorkingTimes();
    // });
    // $: $userMe.isTeacher && loadWorkingTimes();

    // let bWorkingTimesLoaded = false;
    // function loadWorkingTimes(){
    //     if(bWorkingTimesLoaded === false) {
    //         bWorkingTimesLoaded = true;
    //         websocket.send('cal_getworkingtimes').then(function(_wT){
    //             workingTimes = _wT.map(o=>({
    //                 ...o,
    //                 start: new Date(o.start),
    //                 end: new Date(o.end),
    //                 // color: color.available,
    //             }));
    //         });
    //     }
    // };

    function onLessonClicked(evt){
        let oLesson = evt.detail;
        if(oLesson.extendedProps.teacherId === $userMe.id){
            open(ModalLessonAccept, {
                onAccept: ()=>onAcceptOrReject(oLesson, true),
                onReject: ()=>onAcceptOrReject(oLesson, false),
                event: oLesson,
            });
        } else {
            open(ModalLessonInfo, {
                event: oLesson,
            });
        }
    }

    function onAcceptOrReject(oLesson, bAccept){
        // Loading
        myEvents.update(_myEvents=>{
            let i = _myEvents.findIndex((e)=>e.eventId===oLesson.extendedProps.eventId);
            _myEvents[i].loading = true;
            return _myEvents;
        });

        websocket.send('cal_'+(bAccept?'accept':'reject')+'_lesson', {
            'eventId': oLesson.extendedProps.eventId,
        }, {answer: false})
    }

    let calEvents=[];
    $: calEvents = [
        ...$myEvents.filter(o=>o.teacherId == $userMe.id).map(o=>({
            ...o, 
            color:o.teacherConfirmed === true ? color.teacherConfirmed : color.teacherNotConfirmed,
            title:o.teacherConfirmed === true ? 'confirmed':'booked',
        })),
        ...$myEvents.filter(o=>o.teacherId != $userMe.id).map(o=>({
            ...o, 
            color:color.meBusy,
            title:'I have lesson',
        })),
    ];

    import CalEvent from './ui/CalEvent.svelte';
    function eventRender({detail:{el, event, isEnd, isMirror, isStart, view,}}) {
        el.innerHTML='';
        const calEvent = new CalEvent({
            target: el,
            props:{event, isEnd, isMirror, isStart, view,}
            // hydrate: true
        });
        // el.innerHTML = '<div class="fc-content"><div class="fc-time" data-start="10:00" data-full="10:00 - 10:50"><span>10:00 - 10:50a</span></div><div class="fc-title">I have lesson!!!</div></div>';
        // console.dir(event);
        // element.find(".fc-title").append(" (miau)");
        // console.dir(element);
    }
</script>

<Calendar
    workingTimes={$myWorkingTime}
    workingTimesEditable={$userMe.isTeacher && $userMe.emailVerified}
    workingTimesColor={color.available}
    events={calEvents}
    on:eventClicked={onLessonClicked}
    on:changeWorkingTimes={(event)=>{websocket.send('cal_changeworkingtimes', event.detail, {answer:false})}}
    on:eventRender={eventRender} />