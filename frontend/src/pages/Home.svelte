<!-- <script>
    import Fa from 'svelte-fa';
    import { faUserPlus } from '@fortawesome/free-solid-svg-icons';

    import {authenticated} from 'js/account.js';

	import Link from 'ui/Link.svelte';
	// import BackgroundVideo from 'ui/BackgroundVideo.svelte';

</script> -->

<!-- {#if authenticated === false}
<BackgroundVideo videoUrl={'https://ak3.picdn.net/shutterstock/videos/1028495423/preview/stock-footage-young-asian-business-woman-looking-at-camera-or-webcam-talking-for-online-job-interview-making.mp4'}>
	document.body.dataset.staticurl+"video/stock-footage-young-asian-business-woman-looking-at-camera-or-webcam-talking-for-online-job-interview-making.mp4
	<h1 class="display-4">Learn languages</h1>
	<p class="lead mb-0">online from teachers</p>
	<p class="lead">via videoconferencing</p>
</BackgroundVideo>
{/if} -->

<style>
/* Hero CSS */
.welcome-thumb {
  position: relative;
  z-index: 1;
  margin-top: 75px;
}

@media only screen and (max-width: 767px) {

  .welcome-thumb {
    margin-top: 50px;
    margin-bottom: -100px;
  }

}

@media only screen and (max-width: 580px) {

  .welcome-thumb {
    margin-top: 50px;
    margin-bottom: -200px;
  }

}

.background-animation {
  position: absolute;
  z-index: 1;
  top: 0;
  left: 0;
  width: 70%;
  height: 100%;
}

.background-animation .star-ani {
  position: absolute;
  border-radius: 50%;
  width: 300px;
  height: 300px;
  top: 15%;
  left: 45%;
  z-index: -1;
  -webkit-animation: rotateAnimation linear 39s infinite;
  animation: rotateAnimation linear 39s infinite;
}

.background-animation .star-ani::after {
  position: absolute;
  content: "\e950";
  top: 10%;
  left: 10%;
  z-index: -1;
  border-radius: 50%;
  font-family: "LineIcons";
  color: rgba(255, 255, 255, 0.26);
  font-size: 22px;
}

.background-animation .cloud-ani {
  position: absolute;
  border-radius: 50%;
  width: 240px;
  height: 240px;
  top: 50%;
  left: 60%;
  z-index: -1;
  -webkit-animation: rotateAnimation linear 46s infinite;
  animation: rotateAnimation linear 46s infinite;
}

.background-animation .cloud-ani::after {
  position: absolute;
  content: "\e950";
  top: 10%;
  left: 10%;
  z-index: -1;
  border-radius: 50%;
  font-family: "LineIcons";
  color: rgba(255, 255, 255, 0.26);
  font-size: 2.5rem;
}

.background-animation .circle-ani {
  position: absolute;
  border-radius: 50%;
  -webkit-animation: rotateAnimation linear 34s infinite;
  animation: rotateAnimation linear 34s infinite;
  width: 180px;
  height: 180px;
  left: 10%;
  top: 10%;
  z-index: -1;
}

.background-animation .circle-ani::after {
  width: 20px;
  height: 20px;
  position: absolute;
  content: "";
  top: 10%;
  left: 10%;
  border: 3px solid rgba(255, 255, 255, 0.2);
  z-index: -1;
  border-radius: 50%;
}

.background-animation .triangle-ani {
  position: absolute;
  border-radius: 50%;
  -webkit-animation: rotateAnimation linear 40s infinite;
  animation: rotateAnimation linear 40s infinite;
  width: 20%;
  height: 20%;
  left: 30%;
  top: 50%;
  z-index: -1;
}

.background-animation .triangle-ani::after {
  width: 0;
  height: 0;
  position: absolute;
  content: "";
  border-top: 14px solid rgba(255, 255, 255, 0.16);
  border-bottom: 14px solid transparent;
  border-left: 14px solid transparent;
  border-right: 14px solid transparent;
  z-index: -1;
}

.background-animation .box-ani {
  position: absolute;
  border-radius: 50%;
  -webkit-animation: rotateAnimation linear 37s infinite;
  animation: rotateAnimation linear 37s infinite;
  width: 15%;
  height: 18%;
  left: 7%;
  top: 70%;
  z-index: -1;
}

.background-animation .box-ani::after {
  width: 26px;
  height: 26px;
  position: absolute;
  content: "";
  z-index: -1;
  background-color: transparent;
  border-radius: 4px;
  border: 3px solid rgba(255, 255, 255, 0.2);
}

.background-animation .line-ani {
  position: absolute;
  border-radius: 50%;
  -webkit-animation: rotateAnimation linear 43s infinite;
  animation: rotateAnimation linear 43s infinite;
  width: 10%;
  height: 12%;
  left: 7%;
  top: 30%;
  z-index: -1;
}

.background-animation .line-ani::after {
  width: 30px;
  height: 3px;
  position: absolute;
  content: "";
  z-index: -1;
  background-color: rgba(255, 255, 255, 0.17);
}

@-webkit-keyframes rotateAnimation {
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes rotateAnimation {
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

.welcome-area {
  position: relative;
  z-index: 2;
  height: 100vh;
  background-color: #FAB705;
  overflow: hidden;
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .welcome-area {
    height: 750px;
  }
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .welcome-area {
    height: 650px;
  }
}

@media only screen and (max-width: 767px) {
  .welcome-area {
    height: 820px;
  }
}

.welcome-area .background-image {
  position: absolute !important;
  width: 100%;
  height: auto;
  top: 0;
  left: 0;
  z-index: -1;
}

.welcome-area .hero-background-shape {
  position: absolute !important;
  top: -40%;
  right: -32%;
  z-index: -1;
}

.welcome-area .welcome-content {
  position: relative;
  z-index: 1;
  margin-top: 75px;
}

@media only screen and (max-width: 767px) {
  .welcome-area .welcome-content {
    margin-top: 60px;
  }
}

.welcome-area .welcome-content h2 {
  font-size: 2.75rem;
  margin-bottom: 1.5rem;
  font-weight: 700;
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .welcome-area .welcome-content h2 {
    font-size: 2.5rem;
  }
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .welcome-area .welcome-content h2 {
    font-size: 2rem;
  }
}

@media only screen and (max-width: 767px) {
  .welcome-area .welcome-content h2 {
    font-size: 1.75rem;
  }
}

.welcome-area .welcome-content p {
  font-size: 1.25rem;
  color: #ffffff;
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .welcome-area .welcome-content p {
    font-size: 1.15rem;
  }
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .welcome-area .welcome-content p {
    font-size: 1rem;
  }
}

@media only screen and (max-width: 767px) {
  .welcome-area .welcome-content p {
    font-size: 1rem;
  }
}

.welcome-area.hero {
  background-color: #ffffff;
}

.welcome-area.hero .hero-big-circle {
  width: 320px;
  height: 320px;
  border-radius: 50%;
  border: 4.5rem solid #f4f4ff;
  position: absolute !important;
  left: -185px;
  top: 54%;
  z-index: -1;
}

.welcome-area.hero .welcome-content p {
  color: #8480ae;
}

.welcome-area.hero .background-animation .star-ani::after {
  color: rgba(12, 82, 255, 0.26);
}

.welcome-area.hero .background-animation .cloud-ani::after {
  color: rgba(12, 82, 255, 0.26);
}

.welcome-area.hero .background-animation .circle-ani::after {
  border: 4px solid rgba(12, 82, 255, 0.13);
}

.welcome-area.hero .background-animation .triangle-ani::after {
  border-top: 14px solid rgba(12, 82, 255, 0.12);
}

.welcome-area.hero .background-animation .box-ani::after {
  background-color: rgba(12, 82, 255, 0.11);
}

.welcome-area.hero .background-animation .line-ani::after {
  background-color: rgba(12, 82, 255, 0.17);
}

/* Client Feedback CSS */
.client-feedback-area {
  position: relative;
  z-index: 1;
  overflow: hidden;
}

/* About CSS */
.steps-area {
  position: relative;
  z-index: 2;
}


@media only screen and (max-width: 767px) {
  .step-thumbnail img {
    margin: 50px auto 0px auto;
    width: 65%;
  }

  .step-thumbnail {
    margin: auto;
    display: flex;
  }

  .step-thumbnail.mt-60 {
    margin-top: 0;
  }
}

@media only screen and (min-width: 767px) {
  .w-md-100 {
    width: 100%;
  }

}

.step-thumbnail {
  position: relative;
  z-index: 1;
  border-radius: .75rem;
  text-align: center;
}

.step-thumbnail img {
  max-width: 514px;
}

.step-content {
  position: relative;
  z-index: 1;
}

/* Service Area */
.card {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  position: relative;
  z-index: 1;
  border-radius: 15px;
  padding: 30px;
  border-width: 3.5px;
  border-style: solid;
  text-align: center;
  overflow: hidden;
}

.why-milinga-card .icon {
  position: relative;
  z-index: 10;
  display: flex;
  justify-content: center;
  height: 200px;
  margin: 0 auto 25px;
}


.why-milinga-card h4 {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  margin-bottom: 1rem;
}

.why-milinga-card p {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  margin-bottom: 0;
  font-size: 1.35rem;
  line-height: 1.75rem;
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .why-milinga-card .card-body {
    flex-direction: row !important;
    align-items: center;
  }

  .why-milinga-card .card-body .icon {
    height: 140px;
    width: 370px;
    margin-bottom: 0;
    margin-right: 40px;
  }

}

@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {

  .row > * {
    padding: 0 15px;
    margin-top: 35px;
  }

  .why-milinga-card .card-body .icon img {
    width: 100%;
    height: 100%;
  }
}


/* CTA Area */
/*.cta-area {
  margin-bottom: -95px;
  z-index: 1;
  position: relative;
}

.cta-box {
  position: relative;
  background-color: #FAB705;
  border-radius: 1rem;
  background-image: url('img/subscribe-bg.png');
  background-repeat: no-repeat;
  background-size: cover;
}

.cta-box:before {
  content: '';
  display: block;
  height: 30px;
  width: 90%;
  position: absolute;
  box-shadow: 0 12px 75px rgb(0 0 0 / 0.4);
  z-index: -1;
  left: 0;
  right: 0;
  margin: auto;
  top: 125px;
}

.cta-area .cta-text h2 {
  font-size: 2.25rem;
  display: block;
  margin-bottom: 1rem;
}

.cta-area .form-control {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  height: 64px;
  padding: 12px 20px 15px 20px;
  font-size: 17px;
  color: #453264;
  background-color: #FFF6E9;
  border-width: 2.5px;
  font-weight: 600;
  font-family: 'Linotte';
  border-radius: 12px;
}

.cta-area .form-control::placeholder {
  color: #C7C0BA;
}

.cta-area .cta-text h5 {
  font-family: 'WoodfordBournePRO';
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .cta-area .cta-text h2 {
    font-size: 2.2rem;
  }
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .cta-area .cta-text h2 {
    font-size: 2rem;
  }
}

@media only screen and (max-width: 767px) {
  .cta-area .cta-text h2 {
    font-size: 1.5rem;
  }

  .cta-area {
    margin-left: 1rem;
    margin-right: 1rem;
  }

  .cta-area .form-control {
    height: 54px;
    border-radius: 8px;
  }

  .cta-area .cta-text h5 {
    font-family: 'WoodfordBournePRO';
    font-size: 1.15rem;
  }
}

@media only screen and (min-width: 576px) and (max-width: 767px) {
  .cta-area .cta-text h2 {
    font-size: 1.75rem;
  }
}

@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .cta-area .cta-text h5 {
    font-family: 'WoodfordBournePRO',sans-serif;
  }

  .cta-area .form-control  {
    font-family: 'Linotte',sans-serif;
  }

}
*/
</style>

<script>
    import ScrollUp from 'ui/ScrollUp.svelte';
    import TeacherCarousel from 'ui/TeacherCarousel.svelte'
    import ClientFeedbackCarousel from 'ui/ClientFeedbackCarousel.svelte'
    import ButtonTheme from 'ui/ButtonTheme.svelte';
    import { navigate } from "svelte-routing";

    let oTeachers = [{
        lang: 'English',
        teacherCount: 323,
        img: 'english-teacher.png',
        icon: 'English.svg',
	},{
        lang: 'French',
        teacherCount: 256,
        img: 'french-teacher.png',
        icon: 'French.svg',
	},{
        lang: 'Chinese',
        teacherCount: 242,
        img: 'chinese-teacher.png',
        icon: 'Chinese.svg',
	},{
        lang: 'Spanish',
        teacherCount: 137,
        img: 'spanish-teacher.png',
        icon: 'Spanish.svg',
	},{
        lang: 'Turkish',
        teacherCount: 53,
        img: 'turkish-teacher.png',
        icon: 'Turkish.svg',
	},{
        lang: 'German',
        teacherCount: 41,
        img: 'german-teacher.png',
        icon: 'German.svg',
	},{
        lang: 'Italian',
        teacherCount: 36,
        img: 'italian-teacher.png',
        icon: 'Italian.svg',
	},{
        lang: 'Dutch',
        teacherCount: 27,
        img: 'dutch-teacher.png',
        icon: 'Dutch.svg',
	},{
        lang: 'Russian',
        teacherCount: 27,
        img: 'russian-teacher.png',
        icon: 'Russian.svg',
	},{
        lang: 'Greek',
        teacherCount: 27,
        img: 'greek-teacher.png',
        icon: 'Greek.svg',
	},{
        lang: 'Portuguese',
        teacherCount: 27,
        img: 'portuguese-teacher.png',
        icon: 'Portuguese.svg',
	},{
        lang: 'Japanese',
        teacherCount: 27,
        img: 'japanese-teacher.png',
        icon: 'Japanese.svg',
	},{
        lang: 'Arabic',
        teacherCount: 27,
        img: 'arabic-teacher.png',
        icon: 'Arabic.svg',
	},{
        lang: 'Afrikaan',
        teacherCount: 27,
        img: 'afrikaan-teacher.png',
        icon: 'Afrikaan.svg',
	}];

    let oClientFeedback=[{
		name: 'Yessica Christy',
		location: 'Shanxi, China',
		feedback: 'The results were exciting, I saw improvement in my ability to speak and understand exponentially and now I feel much more comfortable when I have to speak English.',
		// img:'',
    },{
		name: 'Viezh Robert',
		location: 'Warsaw, Poland',
		feedback: 'I have completed one lesson and am amazed at how much I have already learned. Not only does my teacher converse with me in Italian she also sends me small sound clips that I work on at my own pace.',
		// img:'',
    },{
		name: 'Yessica Christy',
		location: 'Shanxi, China',
		feedback: 'The results were exciting, I saw improvement in my ability to speak and understand exponentially and now I feel much more comfortable when I have to speak English.',
		// img:'',
    },{
		name: 'Kim Young Jou',
		location: 'Seoul, South Korea',
		feedback: 'Two months have passed since I first started and I can say that I have seen great leaps forward in my Japanese. Since my first lesson with my tutor, I realized that he would help me improve exponentially.',
		// img:'',
    }]
</script>

  <section class="welcome-area hero" id="home">
    <!-- Background Shape-->
    <div class="hero-background-shape"><img src="{document.body.dataset.staticurl}img/hero-img-bg.svg" alt=""></div>
    <!-- Background Animation-->
    <div class="background-animation">
      <div class="star-ani"></div>
      <div class="circle-ani"></div>
      <div class="box-ani"></div>
    </div>
    <!-- Hero Circle-->
    <div class="container h-100">
      <div class="row h-100 align-items-center justify-content-between">
        <div class="col-12 col-md-6 col-lg-5 welcome-order-one">
          <!-- Content-->
          <div class="welcome-content pr-3">
            <h2 class="wow fadeInUp text-selective-yellow" data-wow-delay="100ms" data-wow-duration="1000ms">Dreaming of
              Learning a New Language?</h2>
            <h5 class="mb-4 text-meteorite wow fadeInUp" data-wow-delay="300ms" data-wow-duration="1000ms">Choose from
              over 1000 teachers for 1-on-1 lessons based on your goals and interests.</h5>
            <!-- Button Group-->
            <div class="btn-group-one wow fadeInUp" data-wow-delay="500ms" data-wow-duration="1000ms">
              <ButtonTheme on:click={()=>{navigate("/register/", {replace:false})}} text="Get Started" />
            </div>
          </div>
        </div>
        <div class="col-md d-none d-lg-inherit col-lg-1 col-sm-1">
        </div>
        <div class="col-10 col-md-6 col-lg-6 welcome-order-two m-auto">
          <div class="welcome-thumb wow fadeInUp text-lg-right " data-wow-delay="300ms" data-wow-duration="1000ms"><img
              src="{document.body.dataset.staticurl}img/hero-img.svg" alt=""></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Teacher Area-->
  <section class="teacher-area bg-old-lace section-padding-90" id="as">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 col-md-9 col-lg-7 col-xxl-6">
          <div class="section-heading text-center">
            <h2 class="text-selective-yellow">1000+ teachers. Any language.</h2>
            <p class="text-atomic">These are the stories of our customers who have joined us with great pleasure when
              using this crazy feature.</p>
          </div>
        </div>
      </div>
      <div class="row justify-content-center">
        <TeacherCarousel teachers={oTeachers} />
      </div>
    </div>
  </section>

  <!-- Why Milinga -->
  <section class="why-milinga-area section-padding-90" id="service">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 col-md-9 col-lg-7 col-xxl-6">
          <div class="section-heading text-center">
            <h2 class="text-radical-red">Why Milinga?</h2>
            <p class="text-atomic">These are the stories of our customers who have joined us with great pleasure when
              using this crazy feature.</p>
          </div>
        </div>
      </div>
      <div class="row justify-content-center g-5">
        <!-- Customized Learning Area-->
        <div class="col-12 d-flex col-sm-12 col-md-12 col-lg-4 col-xl-4">
          <div class="card border-summer-sky why-milinga-card wow fadeInUp" data-wow-delay="100ms"
            data-wow-duration="1000ms">
            <div class="card-body d-flex justify-content-between flex-column p-0">
              <div class="icon">
                <img src="{document.body.dataset.staticurl}img/customized-learning.svg">
              </div>
              <div class="">
                <h4 class="text-atomic text-left">Customized Learning</h4>
                <p class="text-left">Choose from over 1000 teachers for 1-on-1 lessons based on your goals and
                  interests.</p>
              </div>
            </div>
          </div>
        </div>
        <!-- Pay Per Lesson Area-->
        <div class="col-12 d-flex col-sm-12 col-md-12 col-lg-4 col-xl-4">
          <div class="card border-radical-red why-milinga-card active wow fadeInUp" data-wow-delay="200ms"
            data-wow-duration="1000ms">
            <div class="card-body d-flex justify-content-between flex-column p-0">
              <div class="icon"><img src="{document.body.dataset.staticurl}img/pay-per-lesson.svg"></div>
              <div class="">
                <h4 class="text-atomic text-left">Pay Per Lesson</h4>
                <p class="text-left">On milinga you only pay per lesson and at the price that meets your budget.</p>
              </div>
            </div>
          </div>
        </div>
        <!-- Anytime, Anywhere Area-->
        <div class="col-12 d-flex col-sm-12 col-md-12 col-lg-4 col-xl-4">
          <div class="card border-yellow-green why-milinga-card wow fadeInUp" data-wow-delay="300ms"
            data-wow-duration="1000ms">
            <div class="card-body d-flex justify-content-between flex-column p-0">
              <div class="icon"><img src="{document.body.dataset.staticurl}img/anytime-anywhere.svg"></div>
              <div class="">
                <h4 class="text-atomic text-left">Anytime, Anywhere</h4>
                <p class="text-left">Take online lessons at the time and place that suits you.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- How does It Work Steps Area -->
  <section class="steps-area bg-alice-blue section-padding-90">

    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 col-md-9 col-lg-7 col-xxl-6">
          <div class="section-heading text-center">
            <h2 class="text-yellow-green">How does it work?</h2>
            <p class="text-atomic">These are the stories of our customers who have joined us with great pleasure when
              using this crazy feature.</p>
          </div>
        </div>
      </div>
      <div class="row align-items-center justify-content-md-center ">
        <!-- Step Thumbnail Area-->

        <div class="col-12 col-md-8 col-lg-5">
          <div class="step-thumbnail mt-60 wow fadeInUp" data-wow-delay="300ms" data-wow-duration="1000ms"><img
              class="w-md-100" src="{document.body.dataset.staticurl}img/choose-your-teacher.svg" alt=""></div>
        </div>
        <!-- Step Content Area-->
        <div class="col-12 col-md-8 col-lg-4 offset-lg-1">
          <div class="step-content mt-60 wow fadeInUp" data-wow-delay="600ms" data-wow-duration="1000ms">
            <div class="section-heading mb-0">
              <h4 class="text-meteorite mb-30">1. CHOOSE YOUR TEACHER</h4>
              <p>Watch teacher introduction videos and read reviews from other students.</p>
            </div>
          </div>
        </div>
      </div>

      <div class="row align-items-center justify-content-md-center ">
        <!-- Step Content Area-->
        <div class="col-12 col-md-8 order-one col-lg-4">
          <div class="step-content mt-60 wow fadeInUp" data-wow-delay="600ms" data-wow-duration="1000ms">
            <div class="section-heading mb-0">
              <h4 class="text-meteorite mb-30">2. BOOK YOUR LESSON</h4>
              <p>Only schedule lessons at a time and date that suit you.</p>
            </div>
          </div>
        </div>
        <!-- Step Thumbnail Area-->

        <div class="col-12 col-md-8 order-two col-lg-4 offset-lg-1">
          <div class="step-thumbnail mt-60 wow fadeInUp" data-wow-delay="300ms" data-wow-duration="1000ms"><img
              class="w-md-100" src="{document.body.dataset.staticurl}img/book-your-lesson.svg" alt=""></div>
        </div>
      </div>

      <div class="row align-items-center justify-content-md-center ">
        <!-- Step Thumbnail Area-->

        <div class="col-12 col-md-8 col-lg-5">
          <div class="step-thumbnail mt-60 wow fadeInUp" data-wow-delay="300ms" data-wow-duration="1000ms"><img
              class="w-md-100" src="{document.body.dataset.staticurl}img/start-your-journey.svg" alt=""></div>
        </div>
        <!-- Step Content Area-->
        <div class="col-12 col-md-8 col-lg-4 offset-lg-1">
          <div class="step-content mt-60 wow fadeInUp" data-wow-delay="600ms" data-wow-duration="1000ms">
            <div class="section-heading mb-0">
              <h4 class="text-meteorite mb-30">3. START YOUR JOURNEY</h4>
              <p>Connect with your teacher via video chat software, and let the learning begin!</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
  <!-- Client Feedback Area-->
  <section class="client-feedback-area section-padding-90">

    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 col-md-9 col-lg-7 col-xxl-6">
          <div class="section-heading text-center">
            <h2 class="text-burnt-orange px-lg-5">Trusted by Thousands of Happy Customer</h2>
            <p class="text-atomic">These are the stories of our customers who have joined us with great pleasure when
              using this crazy feature.</p>
          </div>
        </div>
      </div>

      <div class="row">

        <div class="col-lg-12">
          <!-- Client Feedback Content-->
          <div class="client-feedback-content">
            <ClientFeedbackCarousel clientFeedback={oClientFeedback} />
          </div>
        </div>
      </div>
    </div>
  </section>


  <!--CTA Area -->

  <!-- <section class="cta-area">
    <div class="container cta-box px-md-5 py-4 px-sm-4">
      <div class="row align-items-center justify-content-between">
        <div class="col-12 col-lg-5 col-md-12">
          <div class="cta-text mb-4 mb-sm-0">
            <h2 class="text-summer-sky">Subscribe Now for Get Special Offers!</h2>
            <h5 class="text-meteorite">Let's subscribe with us and find the fun.</h5>
          </div>
        </div>
        <div class="col-12 col-md-12 col-lg-7 mt-lg-0 mt-sm-3 text-sm-right ">
          <form action="#" method="POST" class="position-relative">
            <input class="form-control border-burnt-orange" type="email" placeholder="Type your mail">
            <button class="btn theme-btn" type="submit">Subscribe Now</button>
          </form>
        </div>
      </div>
    </div>
  </section> -->

<ScrollUp />