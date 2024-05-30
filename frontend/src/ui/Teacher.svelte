<!--
import Teacher from 'ui/Teacher.svelte';
<Teacher
    firstName:{'Martin'}
    lastName={'S.'}
    userId={1}
    teaches={['Deutsch', 'Englisch', 'Spanisch',]}
    description={'Ich bin ein guter Lehrer!'}
    videoId={'vrU6YJle6Q4'}
    profilePic={null}
    rating={teacher.rating}
    on:click={onTeacherClicked} />
-->

<script>
    import Fa from 'svelte-fa';
    import { faEuroSign, faDollarSign, faGraduationCap, faGlobe, faCoins, faAngleUp, faPlay, faStop } from '@fortawesome/free-solid-svg-icons';
    import { faComment } from '@fortawesome/free-regular-svg-icons';
    import CalStudentBookTeacher from 'ui_dyn/calendar/CalStudentBookTeacher.svelte';

    import VideoPlayer from 'ui/VideoPlayer.svelte';
    import { createEventDispatcher } from 'svelte';
    import StarRating from 'svelte-stars-rating';
    import {subjects} from 'store/subjects.js';
    import Clickable from 'ui/Clickable.svelte';

    import CountryFlag from 'ui/CountryFlag.svelte';

    import IconAboutMe from 'svg/about-me.svelte';
    import IconCalendar from 'svg/calendar.svelte';
    import IconHat from 'svg/hat.svelte';
    import IconHeart from 'svg/heart.svelte';
    import IconHeartOutline from 'svg/heart-outline.svelte';
    import IconLessons from 'svg/lessons.svelte';
    import IconMessage from 'svg/message.svelte';
    import IconPlayButton from 'svg/play-button.svelte';
    import IconReviewStar from 'svg/review-star.svelte';
    import IconStudents from 'svg/students.svelte';
    import {OnlineStatus} from 'js/const.js';

	const dispatch = createEventDispatcher();

    export let name = '';
    export let userId=undefined;
    export let onlineStatus=OnlineStatus.online; //TODO: Online-Status
    export let teaches;
    export let country;
    export let numberReviews=5; //TODO: Anzahl Reviews
    export let numberLessons=10; //TODO: Anzahl gegebener Unterrichtstunden
    export let favorite=false; //TODO: Lehrer Favoriten-Markierung speichern und Filter dafür!
    export let description = '';
    export let videoUrl = '';
    export let profilePic;
    export let rating;
    export let pricePerHour;
    export let currency;
    
    let currencyIcon;
    switch(currency){
        case 'EUR': currencyIcon = faEuroSign; break;
        case 'USD': currencyIcon = faDollarSign; break;
    }

    let oSubjectsAll;
    let sSubjectsTaught='';
    
    $: sSubjectsTaught=getSubjects($subjects, teaches);

    function getSubjects(oSubjects, oTeaches){
        let sRtn = '';
        if(oTeaches===undefined || oTeaches.length===0) {
            sRtn = '';
        } else {
            if(typeof oTeaches[0] === 'object'){
                sRtn = oTeaches.map((o)=>o.subject).join(', ');
            } else {
                sRtn = oTeaches.map((sId)=>{
                    let oS = oSubjects.find((o)=>o.id===sId);
                    return oS?oS.subject:'';
                }).join(', ');
            }
        }
        return sRtn;
    }

    if(profilePic === null){
        profilePic = document.body.dataset.staticurl + 'img/noprofilepic.png';
    }

    function onTeacherClicked(){
        dispatch('click', userId);
    }

    let ratingStyle={
        styleStarWidth: 20,
        styleEmptyStarColor: "#737373",
        styleFullStarColor: "#ffd219"
    };

    let bShowVideo=false;
    let bShowCalendar=false;
</script>

<!-- <style>
    div :global(.indicator) { /* StarRating Schriftgröße */
        font-size: 0.8rem;
    }
    .price {
        font-size: 1rem;
    }
    :global(.fc-center) {
        font-size: 0.5rem;
    }

    /* Tabs rechts */
    .nav-link{
        background-color:#eee;
    }
    .nav-link.active{
        background-color:#ddd !important;
    }
    .nav-link:hover{
        background-color:#ccc !important;
    }
</style> -->

<style>
:global(.star-container) {
    display: inline-block!important;
    vertical-align: sub;
}
/* :global(.star-rating) {
    display: block!important;
} */

.listing-card {
    box-shadow: 0 11px 20px rgba(0, 0, 0, 0.12);
}

.avatar {
    max-width: 170px;
    height: 170px;
}

.status-dot {
    content: '';
    display: block;
    width: 18px;
    height: 17px;
    position: absolute;
    background: #dadada;
    border-radius: 100%;
    bottom: 8px;
    right: 25px;
    border: 2px solid #fff;
}

.status-dot.online {
    background-color: #449D44;
}

.status-dot.offline {
    background-color: #D9534F;
}

.status-dot.away {
    background-color: #F0AD4E;
}

.video-btn {
    position: absolute;
    right: -5px;
    border-radius: 100%;
    background: #fff;
    width: 50px;
    height: 50px;
    box-shadow: 1px 7px 15px rgba(0, 0, 0, 0.15);
    color: #7F3CD8;
}
.video-btn-play {
    padding: 12px 16px;
}
.video-btn-stop {
    padding: 13px 15px;
}

:global(.video-btn svg) {
    width: 20px;
}

.hourly-rate span {
    font-size: 1.15rem;
}

:global(.country-flag img) {
    width: 32px;
}

/* .review-star {
    width: 15px;
} */

.teacher-reviews a {
    margin-left: 10px;
    color: #000;
    text-decoration: underline;
}

.theme-primary-btn-sm {
    border: 1.5px solid #e5e5e5;
    vertical-align: middle;
    padding: 5px 15px;
    justify-content: center;
    display: flex;
    align-items: center;
    font-weight: 600;
    transition: 0.3s all;
    background: #fff;
}

.theme-primary-btn-lg {
    border: 1.5px solid #e5e5e5;
    vertical-align: middle;
    justify-content: center;
    display: flex;
    height: calc(2.5rem + 2px);
    align-items: center;
    font-weight: 600;
    padding: 0;
    /* min-width: 110px; */
    transition: 0.3s all;
    background: #fff;
}

:global(.theme-primary-btn-lg svg) {
    width: 16px;
    margin-right: 10px;
}

:global(.theme-primary-btn-sm svg) {
    width: 15px;
    margin-right: 5px;
}

.theme-primary-btn-lg:hover,
.theme-primary-btn-sm:hover {
    box-shadow: 1px 3px 5px rgba(0, 0, 0, 0.1);
    transition: 0.3s all;
}

.theme-primary-btn-lg:focus,
.theme-primary-btn-sm:focus {
    outline: none;
    box-shadow: 1px 3px 5px rgba(0, 0, 0, 0.1);
}

:global(.teach-hat-icon svg){
    width: 20px;
    margin-right: 5px;
}

.teaches {
    color: #7f3cd8;
}

.teaches span {
    margin-right: 15px;
    color: #000;
}

.teaches a {
    text-decoration: none;
    color: #7f3cd8;
}

:global(.total-lessons svg) {
    width: 14px;
    margin-right: 10px;
    margin-top: -3px;
}

.teacher-short-intro {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    line-height: 20px;
    min-height: 62px;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

.country-name {
    color: #7f3cd8;
}

/* .d-grid {
    display: grid;
} */

:global(.active-students svg) {
    width: 14px;
    margin-right: 10px;
    margin-top: -3px;
}

.teacher-intro {
    line-height: 20px;
}

.teacher-intro h6 {
    color: #7f3cd8;
    display: inline-block;
}

:global(.teacher-intro img) {
    width: 18px;
    margin-right: 5px;
    margin-top: -5px;
}

@media only screen and (max-width: 600px) {
    .d-grid {
        display: inherit;
    }
}
</style>


<div class="card rounded-0 mb-3 p-4 listing-card border-0">
    {#if bShowVideo===true}
        <div class="mb-3">
            <VideoPlayer autoplay {videoUrl}/>
        </div>
    {/if}
    <div class="row g-0">
        <div class="col-lg-3 col-md-3 col-sm-12">
            <div class="avatar m-auto position-relative">
                <Clickable on:click={()=>bShowVideo=!bShowVideo} href="">
                    <!-- <IconPlayButton /> -->
                    {#if bShowVideo===false}
                        <div class="video-btn video-btn-play">
                            <IconPlayButton />
                        <!-- <Fa icon={faPlay}/> -->
                        </div>
                    {:else}
                        <div class="video-btn video-btn-stop">
                            <Fa icon={faStop} size="lg"/>
                        </div>
                    {/if}
                </Clickable>
                <img class="rounded-circle w-100"
                    src={profilePic} alt="..." />

                <div class="status-dot"
                    class:online={onlineStatus===OnlineStatus.online}
                    class:offline={onlineStatus===OnlineStatus.offline}
                    class:away={onlineStatus===OnlineStatus.away}></div>

            </div>
            <div class="mt-3 text-center hourly-rate">
                <p class="mb-0">Hourly Rate</p>
                <!-- <span class="rate-min font-weight-bold">$12.00</span>
                <span class="font-weight-bold ml-1 mr-1">-</span>
                <span class="rate-max font-weight-bold">$25.00</span> -->
                <span class="font-weight-bold"><Fa icon={currencyIcon} />{pricePerHour}</span>
            </div>

        </div>
        <div class="col-lg-9 col-md-9 col-sm-12">
            <div class="pl-md-3 pb-0 pr-0">
                <div
                    class="d-md-flex d-block text-center text-sm-left align-items-center justify-content-between">
                    <div class="d-inline-flex mt-3 mt-sm-0">
                        <h5 class="teacher-name mb-0 mr-3 font-weight-bold">{name}</h5>
                        <div class="country-flag d-flex">
                            <CountryFlag flag={country}/>
                        </div>
                    </div>
                    {#if numberReviews>0}
                        <div class="teacher-reviews d-sm-inline-block d-block mt-2 mt-sm-0">
                            <StarRating {rating} style={ratingStyle} isIndicatorActive={false}/>
                            <a href="javascript:void(0);" on:click={()=>{alert('noch nicht programmiert')}}>{numberReviews} Reviews</a>
                        </div>
                    {/if}
                    <div class="d-inline-block float-sm-right float-none mt-3 mt-sm-0">
                        <button class="btn theme-primary-btn-sm rounded" on:click={()=>{favorite=!favorite}}><i class="favorite-icon">{#if favorite===false}<IconHeartOutline />{:else}<IconHeart />{/if}</i>Favorite</button>
                    </div>
                </div>

                <div class="mt-4 mb-3 d-md-flex d-block align-items-center justify-content-between">
                    <div class="teaches d-sm-inline-flex d-block">
                        <i class="teach-hat-icon"><IconHat /></i> <!--<img src="assets/media/hat.svg" class="teach-hat-icon" alt="" />-->
                        <p class="mb-0 d-inline-block">Teaches</p>
                        <p class="mb-0"><span class="ml-0 ml-sm-2">{sSubjectsTaught}</span><!--<a href="">view more...</a>--></p>
                    </div>
                    {#if numberLessons>0}
                        <div class="total-lessons float-sm-right float-none mt-2 mt-sm-0">
                            <p class="mb-0 font-weight-bold"><IconLessons /><small>{numberLessons} Lessons</small></p>
                        </div>
                    {/if}
                </div>
                <p class="card-text teacher-short-intro">{description}</p>

                <div class="btn-group mt-3 mx-auto w-100">
                    <button class="btn rounded theme-primary-btn-lg mr-3" on:click={()=>bShowCalendar=!bShowCalendar}><IconCalendar />Calendar{#if bShowCalendar===true} <Fa icon={faAngleUp} />{/if}</button>
                    <button class="btn rounded theme-primary-btn-lg" on:click={()=>{dispatch('openchat', {userId})}}><!--<IconMessage />--><Fa icon={faComment} /> Chat</button>
                </div>
            </div>
        </div>
    </div>
    <div class="my-1">
        {#if bShowCalendar===true}
            <CalStudentBookTeacher teacherId={userId} />
        {/if}
    </div>
</div>
<!-- <div class="row px-2 py-3 no-gutters border rounded overflow-hidden mt-3 shadow-sm" style="cursor:pointer;">
    LINKS
    <div class="col-3 order-1 col-sm-2 order-sm-1 px-2 justify-content-center" on:click={onTeacherClicked}>
        <img class="row mx-0 shadow-sm img-fluid w-100 rounded-lg" src={profilePic} alt='profile pic'/>
        {#if rating !== -1}
            <div class="row mx-0 justify-content-center mt-2">
                <StarRating {rating} style={ratingStyle} isIndicatorActive={true}/>
            </div>
        {/if}
    </div>

    MITTE
    <div class="col-9 order-last col-sm-5 order-sm-2 px-2 d-flex flex-column" on:click={onTeacherClicked}>
        <h5><CountryFlag flag={country}/> <span style="vertical-align:middle;margin-left:5px;">{name}</span></h5>
        <span class="text-muted"><Fa icon={faGraduationCap}/> {sSubjectsTaught}</span>
        <div class="mt-auto d-flex flex-column">
            <div><span class="price"><Fa icon={faCoins}/> {pricePerHour}</span> <Fa icon={currencyIcon} /></div>
            <span class="text-muted small">per hour pro Stunde</span>    
        </div>
    </div>

    RECHTS 
    <div class="col-12 order-2 d-none d-sm-block col-sm-5 order-sm-3 px-2 justify-content-end align-items-center">
        <div class="nav-tabs d-flex flex-row">
            <span class="nav-link" class:active={activeTab=='Video'} on:click={()=>activeTab='Video'}>Video</span>
            <span class="nav-link" class:active={activeTab=='Vorstellung'} on:click={()=>activeTab='Vorstellung'}>About Me Über mich</span>
            <span class="nav-link" class:active={activeTab=='Termine'} on:click={()=>activeTab='Termine'}>Calendar Termine</span>
        </div>
        {#if activeTab=='Video'}
            <VideoPlayer {videoUrl}/>
        {:else if activeTab=='Vorstellung'}
            <span class="card-text">{description}</span>
        {/if}
    </div>
</div>
<div class="mb-3">
    {#if activeTab=='Termine'}
            <CalStudentBookTeacher teacherId={userId} />
    {/if}
</div> -->
