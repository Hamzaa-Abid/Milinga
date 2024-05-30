<script>
    import {userMe} from 'js/account.js'
	import {myEvents} from 'store/calendar.js';
	import {time} from 'store/time.js';

	// $myEvents = [{
	// 	'eventId': oEvent.id,
	// 	'title': oEvent.title,
	// 	'start': datetime.toTimestamp(oEvent.time_start),
	// 	'end': datetime.toTimestamp(oEvent.time_end),
	// 	'studentConfirmed': oEvent.studentConfirmed,
	// 	'teacherConfirmed': oEvent.teacherConfirmed,
	// 	'teacherId': oEvent.teacher.id,
	//	'studentId': oEvent.student.id,
	// },]

	//	$: mySortedEvents = $myEvents.sort((a,b)=>b.start-a.start)
	$: nextEvent = getNextEvent($myEvents)

	function getNextEvent(oEvents){
		let oSortedFutureEvents = oEvents.sort((a,b)=>a.start-b.start).filter(x=>x.end>new Date())
		return oSortedFutureEvents[0] || {};
	}

	$: nextEventStartSec = Math.trunc((nextEvent.start - $time)/1000);

	function startVideoConference(){
		window.location.href='https://meet.jit.si/milinga_'+nextEvent.vcId+'#userInfo.displayName=%22'+$userMe.name+'%22';
	}
</script>

{#if nextEventStartSec < 14*60}
	<section class="p-5 text-center" class:bg-warning={nextEventStartSec > 0} class:bg-danger={nextEventStartSec <= 0}>
		<div class="container">
			<h1>
				{#if nextEventStartSec > 0}
					Unterricht startet in {Math.trunc(nextEventStartSec/60)} min {nextEventStartSec%60} sec.
				{:else}
					Unterricht hat bereits begonnen!!!
				{/if}
			</h1>
			<button type="button" class="btn btn-primary" on:click={startVideoConference}>START VIDEOCONFERENCE</button>
		</div>
	</section>
{/if}