<!--
import ImageChooser from 'ui/ImageChooser.svelte';

<ImageChooser
    src={''}
    on:change />
 -->

<script>
    import {createEventDispatcher} from 'svelte';
    import Fa from 'svelte-fa';
    import { faPencilAlt } from '@fortawesome/free-solid-svg-icons';
    import Slide from 'transitions/Slide.svelte';
    import Hoverable from 'ui/Hoverable.svelte';

    const dispatch = createEventDispatcher();

    export let src=null;
    let fileInput;

    function inputFileChanged(event) {
        let image = this.files[0]
        dispatch('change', image);
    //     var formData = new FormData();//$('#upload_image_form')[0]);
    //     formData.append('profilePic', this.files[0]);

    //     $.ajax({
    //         url: "{% url 'update_profile_pic' %}",
    //         type: 'POST',
    //         cache: false,
    //         async: true,
    //         dataType: 'json',
    //         processData: false,
    //         data: formData,
    //         enctype: 'multipart/form-data',
    //         contentType: false,
    //         success: function(response){
    //             $("#profile-pic").attr("src",response.image_url);
    //         },
    //     });
    }
</script>

<style>
/* .upload-button {
 font-size: 1.2em;
} */

/* .pro-img  {
 position: relative;
} */

.imagechooser {
    position: relative;
    cursor: pointer;
}

.imagechooserbutton {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 50px;
    height: 50px;
    text-align: center;
    padding-top: 15px;
    color: #fff;
    cursor: pointer;
    background: rgba(0,0,0,.3);
    font-size: 1.2em;
}

.file-upload {
   display: none;
}
</style>

<Hoverable let:hovering>
    <div class="imagechooser" on:click={()=>{fileInput.click()}}>
        <img class="img-fluid rounded w-100 clickable-image" {src} alt='profile pic' />
            <Slide show={hovering}>
                <div class="imagechooserbutton">
                    <Fa icon={faPencilAlt} />
                </div>
            </Slide>
        <!-- <i class="fas fa-pencil-alt upload-button"></i> -->
    </div>
</Hoverable>
<input class="file-upload" bind:this={fileInput} on:change={inputFileChanged} type="file" accept="image/*"/>
