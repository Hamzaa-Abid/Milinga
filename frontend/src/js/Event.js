/**
 * Listen to events, remove the listener and dispatch events
 */
class EventListeners {
    constructor(){
        this.callbacks={};
    }

    /**
     * Listen to events with the id sId and call the callback-function callback.
     * 
     * @param {String} sId The id of the dispatched event.
     * @param {Function} callback Callback, which gets called, if an event with the event-id is dispatched.
     */
    addEventListener(sId, callback) {
        if(this.callbacks[sId]===undefined){
            this.callbacks[sId] = [];
        }
        if (this.callbacks[sId].indexOf(callback) < 0) {
            this.callbacks[sId].push(callback);
        }

        return ()=>this.removeEventListener(sId, callback);
    }

    /**
     * Remove a callback-function from the event listeners.
     * 
     * @param {String} sId sId The id of the dispatched event.
     * @param {Function} callback The callback function, which should be removed from the event-listener.
     */
    removeEventListener(sId, callback) {
        let index;
        if ((index = this.callbacks[sId].indexOf(callback)) >= 0) {
            this.callbacks[sId].splice(index, 1);
        }
    }

    /**
     * Dispatch an Event
     * 
     * @param {String} sId Id of the event to be dispatched
     * @param  {...any} params Parameters to be passed to the listener callback function
     */
    dispatch(sId, ...params) {
        if(this.callbacks[sId]!=undefined){
            this.callbacks[sId].forEach(callback=>callback(...params));
        }
    }
}
const Event = new EventListeners();
export default Event;