<script>
    import allLocales from '@fullcalendar/core/locales-all.js';
    import {createEventDispatcher} from 'svelte';

    import FullCalendar from 'svelte-fullcalendar';
	// import dayGridPlugin from '@fullcalendar/daygrid';
	import timeGridPlugin from '@fullcalendar/timegrid';
    import interactionPlugin from '@fullcalendar/interaction';
    // import {preferences} from 'store/preferences.js';
    import './fullcalendar.scss';

    import {languageCode} from 'store/languages.js';

    const dispatch = createEventDispatcher();

    let plugins = [timeGridPlugin, interactionPlugin];
    let calendarComponentRef;
    
    export let workingTimes=[];
    export let events=[];
    export let workingTimesEditable = false;
    export let workingTimesColor;
    export let eventBookable = false;
    export let eventBookableMinDate = new Date();

    let businessHours = {
        startTime: '08:00', // a start time (10am in this example)
        endTime: '20:00', // an end time (6pm in this example)
    };
    let calStartHour = 7;
    let calEndHour = 22;

    let calendarEvents=[];

    $: workingTimes, events, function(){
        calendarEvents = [
            ...workingTimes.map(o=>({...o, rendering:'background',})),
            ...events.map(o=>({...o, durationEditable: false,extendedProps:{eventId: o.eventId,}})),
        ];

        // //working times
        // let workingTimesTmp=[];
        // for(let i=0; i<workingTimes.length; i++){
        //     workingTimesTmp.push({
        //         start: workingTimes[i].start,
        //         end: workingTimes[i].end,
        //         rendering: 'background',
        //         color: workingTimes[i].busy===true?sBGColorBusy:sBGColorAvailable,
        //     })
        // }

        // //events
        // let eventsTmp=[];
        // for(let i=0; i<events.length; i++){
        //     let sColor;
        //     if(events[i].busy === true){
        //         sColor = sBGColorBusy;
        //     } else {
        //         sColor = events[i].teacherConfirmed === true ? sBGColorTeacherConfirmed : sBGColorTeacherNotConfirmed
        //     }

        //     eventsTmp.push({
        //         start: events[i].start,
        //         end: events[i].end,
        //         durationEditable: false,
        //         color: sColor,
        //         extendedProps:{
        //             // type: 'myevent',
        //             eventId: events[i].eventId,
        //         }
        //     })
        // }
        
        // calendarEvents = [...workingTimesTmp, ...eventsTmp];

        if(eventBookable === true){
            if(calendarEvents.length>0) {
                calStartHour = Math.min(...calendarEvents.map(o=>o.start.getHours()));
                calEndHour = Math.max(...calendarEvents.map(o=>o.end.getHours()));
            } else {
            calStartHour = 10;
            calEndHour = 18;
            }
        }
    }();

    function eventOverlap(stillEvent, movingEvent) {
        return stillEvent.rendering == 'background';
    }
    function selectOverlap(event) {
        return event.rendering === 'background';
    }
    let oSelectionStarted={
        start:'',
        end:'',
    };

    function selectAllow(selectInfo){
        //remember start of selection
        if(oSelectionStarted.start !== selectInfo.start.getTime() && oSelectionStarted.end !== selectInfo.end.getTime()){
            oSelectionStarted = {
                start: selectInfo.start.getTime(),
                end: selectInfo.end.getTime(),
            }
        }
        if(selectInfo.start.getDay() != selectInfo.end.getDay()){
            //just same day
            return false;
        }
        if(selectInfo.start < new Date()) {
            //not in the past
            return false;
        }
        return true;
    }

    function select(selectionInfo){
        if(workingTimesEditable === false){
            return;
        }
        let oSelection = selectionInfo.detail;
        //create or remove?
        let bDrawAvailable = true;
        for(let i=0; i<workingTimes.length;i++){
            if((oSelectionStarted.start == oSelection.start.getTime() && (workingTimes[i].start.getTime()<=oSelectionStarted.start && workingTimes[i].end.getTime()>oSelectionStarted.start))
            || (oSelectionStarted.end == oSelection.end.getTime() && (workingTimes[i].start.getTime()<oSelectionStarted.end && workingTimes[i].end.getTime()>=oSelectionStarted.end))){
                bDrawAvailable = false;
                break;
            }
        }
        oSelectionStarted = {
            start:'',
            end:'',
        };


        calendarComponentRef.getAPI().unselect();

        let oEventsToDelete = [];
        let oEventsToCreate = [];

        // let oEvents = calendar.getEvents().filter(function(oEvent){
        //     return oEvent.rendering === 'background';
        // });
        for(let i=0;i<workingTimes.length;i++){
            let oEvent = workingTimes[i];
            if(oEvent.start >= oSelection.start && oEvent.end <= oSelection.end){
                //existing event is inside selected event
                // oEvent.remove();
                oEventsToDelete.push(oEvent);
                continue;
            }
            if(oEvent.start <= oSelection.start && oEvent.end >= oSelection.end){
                //existing event is around selected event
                if(!bDrawAvailable) {
                    // oEvent.remove();
                //     oEventsToDelete.push(oEvent);
                //     oSelection.start = oEvent.start;
                //     oSelection.end = oEvent.end;
                // } else {
                    // oEvent.remove();
                    oEventsToDelete.push(oEvent);
                    if(oEvent.start<oSelection.start){
                        oEventsToCreate.push({
                            start: oEvent.start,
                            end: oSelection.start,
                        });
                    }
                    if(oSelection.end<oEvent.end){
                        oEventsToCreate.push({
                            start: oSelection.end,
                            end: oEvent.end,
                        });
                    }
                    // self.addEvent({
                    //     title: '{% trans "available" %}',
                    //     start: oEvent.start,
                    //     end: oSelection.start,
                    //     rendering: 'background',
                    //     color: sBGColorAvailable,
                    // });
                    // self.addEvent({
                    //     title: '{% trans "available" %}',
                    //     start: oSelection.end,
                    //     end: oEvent.end,
                    //     rendering: 'background',
                    //     color: sBGColorAvailable,
                    // });
                }
                continue;
            }
            if(oEvent.start <= oSelection.start && oSelection.start <= oEvent.end){
                //selected events start is in existing event
                if(bDrawAvailable) {
                    oSelection.start = oEvent.start;
                    // oEvent.remove();
                    oEventsToDelete.push(oEvent);
                } else {
                    // oEvent.setEnd(oSelection.start);
                    oEventsToDelete.push(oEvent);
                    oEventsToCreate.push({
                        start: oEvent.start,
                        end: oSelection.start,
                    });
                    continue;
                }
            }
            if(oEvent.start <= oSelection.end && oSelection.end <= oEvent.end){
                //selected events end is in existing event
                if(bDrawAvailable) {
                    oSelection.end = oEvent.end;
                    // oEvent.remove();
                    oEventsToDelete.push(oEvent);
                } else {
                    // oEvent.setStart(oSelection.end);
                    oEventsToDelete.push(oEvent);
                    oEventsToCreate.push({
                        start: oSelection.end,
                        end: oEvent.end,
                    });
                    continue;
                }
            }
        }
        // color = bDrawAvailable == true ? sBGColorAvailable : '#ff8888';
        if(bDrawAvailable){
            oEventsToCreate.push({
                start: oSelection.start,
                end: oSelection.end,
            });
        }

        for(let i=0;i<oEventsToDelete.length; i++){
            workingTimes = workingTimes.filter(function(oEvent){
                return oEvent !== oEventsToDelete[i];
            })
        }

        for(let i=0;i<oEventsToCreate.length; i++){
            workingTimes=[...workingTimes, {
                title: '{% trans "available" %}',
                start: oEventsToCreate[i].start,
                end: oEventsToCreate[i].end,
                rendering: 'background',
                color: workingTimesColor,
            }];
        }
        
        if(oEventsToCreate.length===0 && oEventsToDelete.length===0){
            return;
        }
        let oToSend = {};
        if (oEventsToCreate.length>0){
            oToSend['create'] = [];
            for(let i=0; i<oEventsToCreate.length; i++){
                oToSend['create'].push({
                    start: new Date(oEventsToCreate[i].start).getTime(),
                    end: new Date(oEventsToCreate[i].end).getTime(),
                });
            }
        }
        if (oEventsToDelete.length>0){
            oToSend['delete'] = [];
            for(let i=0; i<oEventsToDelete.length; i++){
                oToSend['delete'].push({
                    start: oEventsToDelete[i].start.getTime(),
                    end: oEventsToDelete[i].end.getTime(),
                })
            }
        }
        dispatch('changeWorkingTimes', oToSend);
    }

    function createMirrorEvent(mouseEvent){
        let [date, time] = getDayTimeCell(mouseEvent)
        let oDateMouseEvent = new Date(date+'T'+time);
        if (oDateMouseEvent < eventBookableMinDate){
            removeMirrorEvent();
            return;
        }
        let oFreeTimes = findFreeTimes(oDateMouseEvent);
        if (oFreeTimes !== null){
            calendarComponentRef.getAPI().select({
                start: oFreeTimes.start,
                end: oFreeTimes.end,
            });
        } else {
            calendarComponentRef.getAPI().unselect();
        }
        // calendar.select( '2019-11-08T15:00:00', '2019-11-08T16:00:00' )
    }
    function removeMirrorEvent(){
        calendarComponentRef.getAPI().unselect();
    }
    function findFreeTimes(startTime) {
        let iEventDurationInMinutes = 50
        let timeAfter = new Date(startTime.getTime() + iEventDurationInMinutes*60000);
        if(checkConstraints(startTime, timeAfter)) {
            return {
                'start': startTime,
                'end': timeAfter,
            };
        }
        
        let timeBeforeStart = new Date(startTime.getTime() - 30*60000);
        let timeBeforeEnd = new Date(timeBeforeStart.getTime() + iEventDurationInMinutes*60000);
        if(checkConstraints(timeBeforeStart, timeBeforeEnd)) {
            return {
                'start': timeBeforeStart,
                'end': timeBeforeEnd,
            };
        }
        return null;
    }
    function getDayTimeCell(mouseEvent) {
        let mouseX = mouseEvent.clientX;
        let mouseY = mouseEvent.clientY;

        // let days = $('#'+calendarId + ' .fc-day');
        let days = calendarComponentRef.getAPI().el.querySelectorAll('.fc-day');
        for(let i = 0 ; i < days.length ; i++) {
            let day = days[i].getBoundingClientRect();
            if (   mouseX >= day.left && mouseX <= day.left+day.width
                && mouseY >= day.top  && mouseY <= day.top+day.height ) {
                var rtn_date = days[i].dataset.date;
                break;
            }
        }

        // let times = $('#'+calendarId + ' [data-time]');
        let times = calendarComponentRef.getAPI().el.querySelectorAll('[data-time]');
        for(let i = 0 ; i < times.length ; i++) {
            let time = times[i].getBoundingClientRect();
            if (   mouseX >= time.left && mouseX <= time.left+time.width 
                && mouseY >= time.top  && mouseY <= time.top+time.height ) {
                var rtn_time = times[i].dataset.time;
                break;
            }
        }

        return [rtn_date, rtn_time]
    }
    function checkConstraints(start, end){
        let oConstraintsInside = calendarEvents.filter(function(oEvent){
            return oEvent.rendering === 'background';
        });
        let oConstraintsOutside = calendarEvents.filter(function(oEvent){
            return oEvent.rendering !== 'background';
        });
        let bConstraintsInsideFulfilled = false;
        for(let i=0; i<oConstraintsInside.length; i++){
            if(oConstraintsInside[i].start <= start && oConstraintsInside[i].end >= end){
                bConstraintsInsideFulfilled = true;
                break;
            }
        }
        if (bConstraintsInsideFulfilled === false){
            return false;
        }

        let bConstraintsOutsideFulfilled = true;
        for(let i=0; i<oConstraintsOutside.length; i++){
            if((oConstraintsOutside[i].start <= start && oConstraintsOutside[i].end >= start)
                || (oConstraintsOutside[i].start <= end && oConstraintsOutside[i].end >= end)) {
                bConstraintsOutsideFulfilled = false;
                break;
            }
        }
        return bConstraintsOutsideFulfilled;
    }



    function eventClick(eventClickInfo){
        if(eventClickInfo.detail.event.rendering === 'background') return;
        dispatch('eventClicked', eventClickInfo.detail.event);
        // $('#confirmationPopup').modal('show');
        // $('#confirmationPopupLessonName').text(eventClickInfo.event.title)
        // $('#confirmationPopupLessonDate').text(eventClickInfo.event.start.toLocaleDateString())
        // $('#confirmationPopupLessonTime').text(eventClickInfo.event.start.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}))
        // oEventClicked = eventClickInfo.event;
    }

    function dateClick(event) {
        let oDateClick = event.detail.date;
        if (oDateClick < eventBookableMinDate) return;
        let oTimes = findFreeTimes(oDateClick)
        if (oTimes === null) return;
        dispatch('eventBookingClicked', {
            start: oTimes.start,
            end: oTimes.end,
        })
    }

</script>

<style>
	.fullcalendar {
		font-family: Arial, Helvetica Neue, Helvetica, sans-serif;
		font-size: 14px;

        margin: 0 auto;
		/* max-width: 900px; */
    }
    div :global(.fc-mirror) {
        background-color: #ffff00 !important;
        border: none;
        cursor: pointer;
        opacity: 0.5;
    }

    div :global(.fc-event) {
        cursor: pointer;
    }
    
    div :global(.fc-time-grid){
        cursor: var(--calendar-cursor)
    }
</style>
<div class="fullcalendar" style={workingTimesEditable?"--calendar-cursor: cell":''} on:mousemove={(event)=>{if(eventBookable) createMirrorEvent(event)}} on:mouseleave={removeMirrorEvent}>
    <FullCalendar
        bind:this={calendarComponentRef}
        defaultView="timeGridWeek"
        header={{ left: 'prev, today', center: 'title', right: 'next' }}
        plugins={[timeGridPlugin, interactionPlugin]}
        events={calendarEvents}
        locales={allLocales}
        locale={$languageCode}
        
        
        businessHours = {businessHours}
        editable= {false}
        eventOverlap= {eventOverlap}
        selectOverlap= {selectOverlap}
        nowIndicator={true}
        slotDuration='00:30:00'
        snapDuration='00:30:00'
        minTime={calStartHour+':00:00'}
        maxTime={calEndHour+':00:00'}
        scrollTime='08:00:00'
        height= 'auto'
        selectable= {workingTimesEditable}
        unselectAuto= {false}
        selectMirror={eventBookable}
        selectMinDistance = {1}
        longPressDelay = {1000}
        eventBackgroundColor= {workingTimesColor}
        on:select={select}
        selectAllow= {selectAllow}
        on:dateClick={(event)=>{if(eventBookable) dateClick(event)}}
        on:eventClick= {eventClick}
        allDaySlot={false}

        on:eventRender
        />
</div>
