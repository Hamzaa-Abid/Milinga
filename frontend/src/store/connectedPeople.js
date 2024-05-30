// import {connectedPeople} from 'store/connectedPeople.js';
// {#each $connectedPeople as connectedPerson}
//     id: {connectedPerson.userId}<br>
//     chatCount: {connectedPerson.chatCount}<br>
//     calCount: {connectedPerson.calCount}<br>
// {/each}

import {chat} from 'store/chat.js';
import {myEvents} from 'store/calendar.js';
// import {users} from 'store/users.js';
import {userMe} from 'js/account.js';
import {readable, get} from 'svelte/store';

function createConnectedPeopleStore(){
    let oReadable = readable([], set=>{
        let unsubscribeChat = chat.subscribe(oChat=>{
            let oConnectedPeople = get(oReadable);

            // Update Chat Message-Count
            Object.keys(oChat).forEach(sChatId=>{
                let i = oConnectedPeople.findIndex(o=>o.userId == sChatId);
                if(i === -1){
                    oConnectedPeople.push({
                        userId: sChatId,
                        chatCount: oChat[sChatId].messages.length,
                        calCount: 0,
                    });
                } else {
                    oConnectedPeople[i].chatCount = oChat[sChatId].messages.length;
                }
            });

            set(oConnectedPeople);
        })

        let unsubscribeUsers;
        let oUsersMePromise = new Promise((resolve, reject)=>{
            unsubscribeUsers = users.subscribe(_users=>{
                if('id' in _users.me){
                    unsubscribeUsers();
                    resolve(_users.me.id);
                }
            })
        });
        let unsubscribeCalendar = myEvents.subscribe(oCalendar=>{
            oUsersMePromise.then(sUserIdMe=>{
                let oConnectedPeopleAssoc={};
                get(oReadable).forEach(o=>{oConnectedPeopleAssoc[o.userId] = {...o, calCount:0,}});
                
                //Update Calendar-Event-Count
                oCalendar.forEach(o=>{
                    if(o.teacherId == o.studentId) return;
                    let sIdPartner = (o.teacherId==sUserIdMe)?o.studentId:o.teacherId;
                    if(sIdPartner in oConnectedPeopleAssoc){
                        oConnectedPeopleAssoc[sIdPartner].calCount++;
                    } else {
                        oConnectedPeopleAssoc[sIdPartner] = {
                            chatCount: 0,
                            calCount: 1,
                        }
                    }
                })
                let oConnectedPeopleArray = [];
                Object.keys(oConnectedPeopleAssoc).forEach(sChatId=>{
                    oConnectedPeopleArray.push({
                        ...oConnectedPeopleAssoc[sChatId],
                        userId : sChatId,
                    })
                });

                set(oConnectedPeopleArray);
            })            
        })

        return function stop(){
            unsubscribeChat();
            unsubscribeCalendar();
            unsubscribeUsers();
        }
    })
    return oReadable;
}

export const connectedPeople = createConnectedPeopleStore();