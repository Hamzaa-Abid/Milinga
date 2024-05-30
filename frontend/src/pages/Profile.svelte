<script>
    // import { navigate } from "svelte-routing";
    import Fa from 'svelte-fa';
    import { faUserEdit } from '@fortawesome/free-solid-svg-icons';
    import moment from 'moment-timezone';

    import Teacher from 'ui/Teacher.svelte';
    import TextField from 'ui/TextField.svelte';
    import TextArea from 'ui/TextArea.svelte';
    import Button from 'ui/Button.svelte';
    import CheckBox from 'ui/CheckBox.svelte';
    import ImageChooser from 'ui/ImageChooser.svelte';
    import ProfileTeacherData from './ui/ProfileTeacherData.svelte'
    import Alert from 'ui/Alert.svelte';
    import Slide from 'transitions/Slide.svelte';
    import CountryFlagChooser from 'ui/CountryFlagChooser.svelte';
    import TimezonePicker from 'ui/TimezonePicker.svelte';

    import { websocket } from 'js/websocket.js';
    // import { users } from 'store/users.js';
    import {userMe} from 'js/account.js';
    import {time} from 'store/time.js';

    // export let authenticated;

    // $: authenticated, function(){
    //     if(authenticated === false){
    //         navigate('/', {replace:false});
    //     }
    // }();

    let first_name='';
    let last_name='';
    let timezone;
    let country;
    let description='';
    let isTeacher=false;
    let pricePerHour;
    let currency;
    let videoUrl;
    let teaches;

    let bShowAlertSuccess=false;

    websocket.send('profile_get').then(function(oProfile){
        first_name = oProfile.first_name;
        last_name = oProfile.last_name;
        country = oProfile.country;
        description = oProfile.description;
        isTeacher = oProfile.isTeacher;
        $userMe.isTeacher = oProfile.isTeacher;
        pricePerHour = oProfile.pricePerHour;
        currency = oProfile.currency;
        videoUrl = oProfile.videoUrl;
        teaches = oProfile.teaches;
    })

    let promiseProfilePicChange;
    function onProfilePicChanged(event) {
        let file = event.detail;
        promiseProfilePicChange = websocket.send('user_profilepic', null, {file:file});
        promiseProfilePicChange.then(function(sNewPath){
            $userMe.profilePic = sNewPath;
        })
    }

    let promiseOnSubmit;
    function onSubmit(){
        bShowAlertSuccess=false;
        let oProfile = {
            first_name: first_name,
            last_name: last_name,
            country: country,
            timezone: timezone,
            description: description,
            isTeacher: isTeacher,
            teaches: isTeacher?teaches:undefined,
            videoUrl: videoUrl,
            pricePerHour: pricePerHour,
            currency: currency,
        }
        promiseOnSubmit = websocket.send('profile_save', oProfile);
        promiseOnSubmit.then(function(){
            bShowAlertSuccess=true;
            $userMe = {
                ...$userMe,
                name: first_name + ' ' + last_name,
                ...oProfile,
            };
        });
    }

    $: sTimeInTimezone = timezone != undefined ? moment($time).tz(timezone).format("HH:mm:ss") : '';
</script>

<div class="container align-items-center justify-content-center my-4">

<h1>Profile</h1>
<form method="post">
    <div class="form-row">
        <!-- Thumbnail -->
        <div class="col-lg-4 col-md-4 col-sm-6 col-6 d-flex align-items-center justify-content-center">
            <ImageChooser
                src={$userMe.profilePic}
                on:change={onProfilePicChanged} />
        </div>
        <div class="form-row col-lg-8 col-md-8 col-sm-6 col-6 px-0">
            <div class="mb-0 col-lg-12 col-md-12 col-sm-12 col-12 d-flex justify-content-between">
                <!-- Name -->
                <TextField
                    type='text'
                    label='First Name'
                    placeholder='First Name'
                    required={true}
                    bind:value={first_name} />
                <TextField
                    type='text'
                    label='Last Name'
                    placeholder='Last Name'
                    required={true}
                    bind:value={last_name} />
            </div>
            <div class="mb-0 col-lg-12 col-md-12 col-sm-12 col-12 d-flex justify-content-between">
                <CountryFlagChooser label="Where are you from?" required={true} bind:country={country} />
                <TimezonePicker bind:timezone label={`Timezone (${sTimeInTimezone})`} required={true} />
            </div>
        </div>
        <div class="col-12 mt-4">
            <CheckBox
                label='I am a teacher'
                bind:value={isTeacher} /><br>
        </div>
        <div class="col-12">
            <Slide show={isTeacher}>
                <!-- <h1>Vorschau:</h1>
                <Teacher
                    name={first_name + ' ' + last_name}
                    profilePic={$userMe.profilePic}
                    rating={5}
                    {teaches} {description} {pricePerHour} {currency}
                    {videoUrl} /> -->

                <ProfileTeacherData
                    bind:teaches
                    bind:description
                    bind:videoUrl
                    bind:pricePerHour
                    bind:currency />
            </Slide>
        </div>
        <div class="col-12">
            <Alert type="success" show={bShowAlertSuccess} autoClose={true}>Profil wurde aktualisiert!</Alert>
            <!-- <Alert type="error" show={true} autoClose={true}>Fehler!</Alert> -->

            <Button
                on:click={onSubmit}
                icon={faUserEdit}
                promise={promiseOnSubmit}
                text="Update Profile" />
        <!-- <button type="submit" class="btn btn-primary"><i class="fas fa-user-edit"></i> Update Profile</button> -->
        </div>
    </div>
</form>

</div>