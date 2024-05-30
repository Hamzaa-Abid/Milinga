// import {myEvents, myWorkingTime} from 'store/calendar.js';
//
// $myEvents = [{
//     'eventId': oEvent.id,
//     'title': oEvent.title,
//     'start': datetime.toTimestamp(oEvent.time_start),
//     'end': datetime.toTimestamp(oEvent.time_end),
//     'studentConfirmed': oEvent.studentConfirmed,
//     'teacherConfirmed': oEvent.teacherConfirmed,
//     'teacherId': oEvent.teacher.id,
//     'studentId': oEvent.student.id,
// },]

import {createOnlineStore} from 'store/onlineStore.js';

function createMyEventsStore(){
    let convertEvent = oEvent=>{
        if(oEvent.start != undefined) oEvent.start = new Date(oEvent.start);
        if(oEvent.end != undefined) oEvent.end = new Date(oEvent.end);
        return oEvent;
    };

    let myEvents = createOnlineStore('cal_myEvents', [], {
        onInit: content=>content.map(convertEvent),
        onUpdate: (data, patch)=>{
            let i = data.findIndex(o=>o.eventId === patch.eventId);
            if(patch.rejected===true){
                if(i!=-1) {
                    data.splice(i, 1);
                }
                return data;
            }
            patch = convertEvent(patch);
            if(i!=-1) {
                data[i] = {...data[i], loading: false, ...patch};
            } else {
                data.push(patch)
            }
            return data;
        },
        storeKeepAliveOnUnsubscribe: true,
        authStore:true,
    });

    let myWorkingTime = createOnlineStore('cal_workingtimes', [], {
        onInit: content=>content.map(convertEvent),
        onUpdate: (data, patch)=>{
            let i = data.findIndex(o=>o.eventId === patch.eventId);
            if(patch.rejected===true){
                data.splice(i, 1);
                return data;
            }
            patch = convertEvent(patch);
            if(i!=-1) {
                data[i] = {...data[i], ...patch};
            } else {
                data.push(patch)
            }
            return data;
        },
        storeKeepAliveOnUnsubscribe: false, //TODO: true und MyCalendar-Änderungen + externe Änderungen im Store speichern
        authStore:true,
    });


    return {myEvents, myWorkingTime};
}
export const {myEvents, myWorkingTime} = createMyEventsStore();