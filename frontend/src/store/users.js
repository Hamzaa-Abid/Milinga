// import {users} from 'store/users.js';

// users.get(userId, function(oUser){
//     oUser.name
//     oUser.profilePic
//     oUser.isTeacher
// });

// myself:
// users.get('me', function(oUser){
//     oUser.name
//     oUser.profilePic
//     oUser.isTeacher
// });

import { writable } from 'svelte/store';
import { websocket } from 'js/websocket.js';

function createUsersStore(){
    let oUsers = {};

    let oUsersStore = writable(new Proxy(oUsers,{get, set}));

    function get(_oUsers, userId) {
        if(userId === undefined) return {};
        if(!(userId in _oUsers) && userId !=='toJSON'){
            _oUsers[userId] = { //placeholder
                name: '',
                profilePic: null,
                isTeacher: false,
            };
            websocket.send('getUser', {
                userId: userId,
            }).then(_oUser=>set(_oUsers, userId, _oUser));
        }
        return _oUsers[userId];
    };

    function set(_oUsers, userId, oUser) {
        oUsers[userId] = oUser;
        oUsersStore.update(o=>o);
        return oUser;
    };


    return oUsersStore;
}

export const users = createUsersStore();