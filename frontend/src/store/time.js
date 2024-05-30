//import {time} from 'store/time.js';
import { readable } from 'svelte/store';

/**
 * time is a readable, which returns an always up to date Date()-object.
 * 
 * @returns {function} A callback, which stops the updating of the Date()-object.
 */
export const time = readable(new Date(), function start(set) {
	const interval = setInterval(() => {
		set(new Date());
	}, 1000);

	return function stop() {
		clearInterval(interval);
	};
});
