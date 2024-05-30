// import {connectedPeople} from 'store/connectedPeople.js';
// {#each $connectedPeople as connectedPerson}
//     id: {connectedPerson.userId}<br>
//     chatCount: {connectedPerson.chatCount}<br>
//     calCount: {connectedPerson.calCount}<br>
// {/each}

import {chat} from 'store/chat.js';
import {myEvents} from 'store/calendar.js';
import {credits} from 'store/credits.js';
// import {users} from 'store/users.js';
import {userMe} from 'js/account.js';
import {readable, get} from 'svelte/store';

function createCreditsTotalStore(){
    let initialData={ myCredits:{}, myCreditsArray:[], myStudentCredits: {}, myStudentCreditsArray: [],};
    let oReadable = readable(initialData, set=>{
        set(initialData);
        
        // CHAT
        let oCreditsChat={};
        let unsubscribeChat;
        let oPromiseChat = new Promise((resolve, reject)=>{
            unsubscribeChat = chat.subscribe(oChat=>{
                oCreditsChat = Object.keys(oChat).reduce((oTotal, sUserId)=>({...oTotal, [sUserId]:0,}), {});
                resolve();
                updateTotalCredits();
            })
        });

        // USERS
        let unsubscribeUserMe;
        let oUserMePromise = new Promise((resolve, reject)=>{
            unsubscribeUserMe = userMe.subscribe(_userMe=>{
                let sUserIdMe = _userMe.id;
                if(sUserIdMe != undefined){
                    resolve(sUserIdMe);
                }
            })
        })
        oUserMePromise.then(unsubscribeUserMe);

        // CALENDAR
        let oMyCreditsCalendar={}, oMyStudentCreditsCalendar={};
        let unsubscribeCalendar;
        let oPromiseCalendar = new Promise((resolve, reject)=>{
            unsubscribeCalendar = myEvents.subscribe(oCalendar=>{
                oUserMePromise.then(sUserIdMe=>{
                    oMyCreditsCalendar = {};
                    oMyStudentCreditsCalendar = {};
    
                    //Update Calendar-Event-Count
                    oCalendar.forEach(o=>{
                        if(o.teacherId == o.studentId) return;
                        if (o.teacherId==sUserIdMe) { // I am teacher
                            oMyStudentCreditsCalendar[o.studentId] = oMyStudentCreditsCalendar[o.studentId] - 1 || -1;
                        } else {
                            oMyCreditsCalendar[o.teacherId] = oMyCreditsCalendar[o.teacherId] - 1 || -1;
                        }
                    })
                    resolve();
                    updateTotalCredits();
                })            
            })
        });

        // CREDITS PAYED
        let oMyCreditsPayed={}, oMyStudentCreditsPayed={};
        let unsubscribeCredits;
        let oPromiseCredits = new Promise((resolve,reject)=>{
            unsubscribeCredits = credits.subscribe(oCredits=>{
                oUserMePromise.then(sUserIdMe=>{
                    oMyCreditsPayed = {};
                    oMyStudentCreditsPayed = {};
    
                    oCredits.forEach(o=>{
                        if(o.ownerId == sUserIdMe){
                            oMyCreditsPayed[o.teacherId] = (oMyCreditsPayed[o.teacherId]||0) + o.credits;
                        } else {
                            oMyStudentCreditsPayed[o.ownerId] = (oMyStudentCreditsPayed[o.ownerId]||0) + o.credits;
                        }
                    })
                    resolve();
                    updateTotalCredits();
                });
            });
        });

        
        let bAllDataLoaded = false;
        function updateTotalCredits(){
            if(bAllDataLoaded === true){
                let oCredits = {
                    myCredits: calculateCredits(oCreditsChat, oMyCreditsCalendar, oMyCreditsPayed),
                    myStudentCredits: calculateCredits(oCreditsChat, oMyStudentCreditsCalendar, oMyStudentCreditsPayed),
                }
                oCredits.myCreditsArray = toArray(oCredits.myCredits, 'userId', 'credits');
                oCredits.myStudentCreditsArray = toArray(oCredits.myStudentCredits, 'userId', 'credits');
                set(oCredits);
            } else {
                Promise.all([oPromiseChat, oPromiseCalendar, oPromiseCredits]).then(()=>{
                    bAllDataLoaded=true;
                    updateTotalCredits();
                });
            }
        }

        function calculateCredits(...oCredits){
            return oCredits.reduce((oCTotal, oCNew)=>{
                Object.keys(oCNew).forEach(sUserId=>{
                    oCTotal[sUserId] = oCTotal[sUserId] + oCNew[sUserId] || oCNew[sUserId];
                })
                return oCTotal;
            }, {});
        }

        function toArray(oAssocArray, sIdName, sIdValue){
            let oArray = [];
            Object.keys(oAssocArray).forEach(sId=>{
                oArray.push({
                    [sIdName]: sId,
                    [sIdValue]: oAssocArray[sId],
                })
            });
            return oArray;
        }

        return function stop(){
            oPromiseChat.then(unsubscribeChat);
            oPromiseCalendar.then(unsubscribeCalendar);
            oPromiseCredits.then(unsubscribeCredits);
        }
    })
    return oReadable;
}

export const creditsTotal = createCreditsTotalStore();