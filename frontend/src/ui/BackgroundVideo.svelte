<!--
import BackgroundVideo from 'ui/BackgroundVideo.svelte';

<BackgroundVideo videoUrl={document.body.dataset.staticurl+".."} />
  <h1 class="display-4">Learn languages</h1>
  <p class="lead mb-0">online from teachers</p>
  <p class="lead">via videoconferencing</p>
</BackgroundVideo>
-->

<script>
    export let videoUrl = 'https://ak3.picdn.net/shutterstock/videos/1028495423/preview/stock-footage-young-asian-business-woman-looking-at-camera-or-webcam-talking-for-online-job-interview-making.mp4';
</script>

<style>
.video-background-holder {
  position: relative;
  background-color: black;
  height: calc(100vh - 72px);
  min-height: 25rem;
  width: 100%;
  overflow: hidden;
}

.video-background-holder video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: 0;
  -ms-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}

.video-background-content {
  position: relative;
  z-index: 2;
}

.video-background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: black;
  opacity: 0.5;
  z-index: 1;
}
</style>


<div class="video-background-holder">
  <div class="video-background-overlay"></div>
  <video playsinline="playsinline" autoplay="autoplay" muted="muted" loop="loop">
        <source src={videoUrl} type="video/mp4">
    </video>
  <div class="video-background-content container h-100">
    <div class="d-flex h-100 text-center align-items-center">
      <div class="w-100 text-white">
        <slot />
        <!-- <h1 class="display-4">Bootstrap video background</h1>
        <p class="lead mb-0">With HTML5 Video and Bootstrap 4</p>
        <p class="lead">Snippet by <a href="https://bootstrapious.com/snippets" class="text-white">
                    <u>Bootstrapious</u></a>
        </p> -->
      </div>
    </div>
  </div>
</div>