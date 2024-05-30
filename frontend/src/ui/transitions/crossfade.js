// import {send, receive} from 'transitions/crossfade.js';
// <h1 out:send={{key: 'h1'}} in:receive={{key: 'h1'}}>test</h1>

import { quintOut } from 'svelte/easing';
import { crossfade } from 'svelte/transition';

export function createCrossfade({duration=300,} = {}){
    const [send, receive] = crossfade({
        duration: d => Math.sqrt(d * duration),
        // Fehler bei Routing-Seitenwechsel!
        // fallback(node, params) {
        //     const style = getComputedStyle(node);
        //     const transform = style.transform === 'none' ? '' : style.transform;

        //     return {
        //         duration: 600,
        //         easing: quintOut,
        //         css: t => `
        //             transform: ${transform} scale(${t});
        //             opacity: ${t}
        //         `
        //     };
        // }
    });
    return {send, receive};
}