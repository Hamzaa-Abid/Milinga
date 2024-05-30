<script>
    // import { navigate } from "svelte-routing";

    import {websocket} from 'js/websocket.js';
    import {myEvents} from 'store/calendar.js';
    import {users} from 'store/users.js';
    import {color} from './js/color.js';
    import {userMe} from 'js/account.js';
    import { getContext } from 'svelte';

    import ModalLessonBook from './ui/ModalLessonBook.svelte';
    import Calendar from './ui/Calendar.svelte';

    const { open } = getContext('simple-modal');

    export let teacherId;

    let workingTimes = [];
    let teacherBusy = [];
    let calEvents = [];

    websocket.send('cal_getTeacherAvailablilty', {teacherId: teacherId}).then(function(oAvailability){
        workingTimes = oAvailability['workingTimes'].map(o=>({
            ...o,
            start: new Date(o.start),
            end: new Date(o.end),
            // color: color.available,
        }));
        teacherBusy = oAvailability['busy'].map(o=>({
            ...o,
            start: new Date(o.start),
            end: new Date(o.end),
            color: color.busy,
            title: 'busy',
        }));
    })

    $: calEvents = [
        ...teacherBusy.filter(o=>!$myEvents.map(m=>m.eventId).includes(o.eventId)),
        ...$myEvents.filter(o=>o.teacherId == teacherId).map(o=>({
            ...o, 
            color:o.teacherConfirmed === true ? color.teacherConfirmed : color.teacherNotConfirmed,
            title:o.teacherConfirmed === true ? 'confirmed':'booked',
        })),
        ...$myEvents.filter(o=>o.teacherId != teacherId).map(o=>({
            ...o, 
            color:color.meBusy,
            title:'I have lesson',
        })),
    ];


    function onEventBookingClicked(event){
        let oLesson = event.detail;
        open(ModalLessonBook, {
            onBook: ()=>bookLesson(oLesson),
            event: oLesson,
        })
    }

    function bookLesson(oLesson){
        websocket.send('cal_book_lesson', {
            'teacher': teacherId,
            'start': oLesson.start.getTime(),
            'end': oLesson.end.getTime(),
        }).then(function(oEvent){
            if(oEvent){
                $myEvents = [...$myEvents, {
                    start: oLesson.start,
                    end: oLesson.end,
                    teacherId: teacherId,
                    teacherConfirmed: false,
                    studentId: $userMe.id,
                    color: color.teacherNotConfirmed,
                    eventId: oEvent.eventId,
                }]
            } 
        });
    }

    // $: iMyCreditsWithTeacher = $myCredits.filter(o=>o.withPerson==teacherId).reduce((a,b)=>a+b.myCredits, 0);
    // $: iMyBookedEventsWithTeacher = $myEvents.filter(o=>o.teacherId == teacherId).length;
    // $: iTeacherBookedEventsFromMe = $myEvents.filter(o=>o.studentId == teacherId).length;

    // $: iMyCredits = iMyCreditsWithTeacher - iMyBookedEventsWithTeacher + iTeacherBookedEventsFromMe;
</script>

<Calendar
    workingTimes={workingTimes}
    workingTimesEditable={false}
    workingTimesColor={color.available}
    events={calEvents}
    eventBookable={$userMe.emailVerified}
    on:changeWorkingTimes={(event) =>{websocket.send('cal_changeworkingtimes', event.detail, {answer:false})}}
    on:eventBookingClicked={onEventBookingClicked} />