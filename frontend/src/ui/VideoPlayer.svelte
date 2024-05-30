<!--
import VideoPlayer from 'ui/VideoPlayer.svelte';

<VideoPlayer {videoUrl} />
-->

<script context="module">
    let stopVideo = ()=>{}
</script>

<script>
    import Fa from 'svelte-fa';
    import { faPlayCircle } from '@fortawesome/free-regular-svg-icons';
    import { faVideoSlash } from '@fortawesome/free-solid-svg-icons';

    export let videoUrl='';
    export let autoplay;

    let imageUrl='';
    let bVideoPlaying = false;
    let iframeVideoUrl;

    function parseVideo (url) {
        // - Supported YouTube URL formats:
        //   - http://www.youtube.com/watch?v=My2FRPA3Gf8
        //   - http://youtu.be/My2FRPA3Gf8
        //   - https://youtube.googleapis.com/v/My2FRPA3Gf8
        // - Supported Vimeo URL formats:
        //   - http://vimeo.com/25451551
        //   - http://player.vimeo.com/video/25451551
        // - Also supports relative URLs:
        //   - //player.vimeo.com/video/25451551

        let oMatch = url.match(/(http:|https:|)\/\/(player.|www.)?(vimeo\.com|youtu(be\.com|\.be|be\.googleapis\.com))\/(video\/|embed\/|watch\?v=|v\/)?([A-Za-z0-9._%-]*)(\&\S+)?/);
        if(oMatch === null){
            return {
                type: null,
                id: null,
            };;
        }

        if (RegExp.$3.indexOf('youtu') > -1) {
            var type = 'youtube';
        } else if (RegExp.$3.indexOf('vimeo') > -1) {
            var type = 'vimeo';
        }

        return {
            type: type,
            id: RegExp.$6
        };
    }

    // function createVideo (url, width, height) {
    //     // Returns an iframe of the video with the specified URL.
    //     var videoObj = parseVideo(url);
    //     var $iframe = $('<iframe>', { width: width, height: height });
    //     $iframe.attr('frameborder', 0);
    //     if (videoObj.type == 'youtube') {
    //         $iframe.attr('src', '//www.youtube.com/embed/' + videoObj.id);
    //     } else if (videoObj.type == 'vimeo') {
    //         $iframe.attr('src', '//player.vimeo.com/video/' + videoObj.id);
    //     }
    //     return $iframe;
    // }

    function getIframeUrl (videoUrl) {
        var videoObj = parseVideo(videoUrl);
        if (videoObj.type == 'youtube') {
            return `https://www.youtube.com/embed/${videoObj.id}?autoplay=1`;//&controls=0`;
        } else if (videoObj.type == 'vimeo') {
            return `https://player.vimeo.com/video/${videoObj.id}?autoplay=1`;
        }
    }

    function getVideoThumbnail (url) {
        // Obtains the video's thumbnail and passed it back to a callback function.
        return new Promise((resolve, reject)=>{
            var videoObj = parseVideo(url);
            if (videoObj.type == 'youtube') {
                resolve('https://img.youtube.com/vi/' + videoObj.id + '/mqdefault.jpg' /*hqdefault.jpg*/);
            } else if (videoObj.type == 'vimeo') {
                (async ()=>{
                    let response = await fetch(`https://vimeo.com/api/v2/video/${videoObj.id}.json`);
                    let data = await response.json()
                    resolve(data[0].thumbnail_medium /*thumbnail_small/thumbnail_medium/thumbnail_large*/);
                })();
            }
        })
    }

    $: onVideoUrlChanged(videoUrl)
    function onVideoUrlChanged(videoUrl){
        if(videoUrl === '') return;
        getVideoThumbnail(videoUrl).then(img=>imageUrl=img);
        iframeVideoUrl = getIframeUrl(videoUrl);
    }

    function playVideo(){
        stopVideo();
        if(videoUrl !== ''){
            bVideoPlaying=true;
            stopVideo=()=>bVideoPlaying=false
        }
    }

    if(autoplay === true) {
        playVideo();
    }
</script>
<style>
img {
  width: 100%;
  height: auto;
}
.responsive-video iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
.responsive-video {
    position: relative;
    padding-bottom: 56.25%; /* Default for 1600x900 videos 16:9 ratio*/
    padding-top: 0px;
    height: 0;
    overflow: hidden;
}
.center {
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%)
}
</style>
<div style={imageUrl===''?'background-color:#ddd':''} class="responsive-video rounded-lg">
    {#if bVideoPlaying===false}
        {#if imageUrl !== ''}
            <div on:click={playVideo} style="cursor:pointer;">
                <img src={imageUrl} alt='thumb'/>
                <div class="center"><Fa icon={faPlayCircle} size="3x" primaryColor="white" /></div>
            </div>
        {:else}
            <div class="center"><Fa icon={faVideoSlash} size="4x"/></div>
        {/if}
    {:else}
        <!-- svelte-ignore a11y-missing-attribute -->
        <iframe frameborder="0" width="100%" height="100%" src={iframeVideoUrl} aria-hidden="true"  allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen"></iframe>
    {/if}
</div>
