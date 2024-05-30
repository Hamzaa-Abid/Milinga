<style>

.text-atomic {
  color: #37474F;
}

.text-selective-yellow {
  color: #FAB705;
}

.border-selective-yellow {
  border-color: #FAB705 !important;
}

.card {
  border-color: #eeeeee;
  border-radius: 6px;
}

.classy-navbar .classynav ul li li a i {
  -webkit-box-flex: 0;
  -ms-flex: 0 0 40px;
  flex: 0 0 40px;
  max-width: 40px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  text-align: center;
  font-size: 1.25rem;
  margin-right: 1rem;
  border: 2px solid #eeeeee;
  line-height: 36px;
}

.classy-navbar .classynav ul li li a i {
  margin-right: 0.8rem;
}

.classy-navbar .classynav ul li li a span {
  display: block;
  color: #1f0757;
  -webkit-transition-duration: 400ms;
  transition-duration: 400ms;
}

.classy-navbar .classynav ul li li a span:hover,
.classy-navbar .classynav ul li li a span:focus {
  color: #FAB705;
}

.classy-navbar .classynav ul li li a span span {
  margin-top: 0.5rem;
  color: #8480ae;
  font-size: 13px;
  text-transform: initial;
}

.classy-navbar .classynav ul li li a span span:hover,
.classy-navbar .classynav ul li li a span span:focus {
  color: #8480ae;
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

/* Teacher Area */
.card.teacher-card {
  padding: 0;
}

.card.teacher-card .card-header {
  padding: 0;
  border: none !important;
}

.card.teacher-card .card-body {
  padding: 10px 20px;
}

.teacher-card .teacher-card-title {
  border-bottom: 2px solid #F0F0F0;
  padding-bottom: 10px;
}

.teacher-card .teacher-card-title p {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  margin-bottom: 0;
  font-size: 0.9rem;
  line-height: 1rem;
  font-weight: 400;
  margin-top: 0;
}

.teacher-card p {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  margin-bottom: 0;
  font-size: 1.15rem;
  line-height: 1.75rem;
  font-weight: 600;
  margin-top: 10px;
}

.see-all {
  position: relative;
  top: -2px;
}

.teacher-thumbnail img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.language-icon {
  position: absolute;
  width: 44px;
  height: 44px;
  border-radius: 50px;
  right: 15px;
  top: 15px;
  border: 2.5px solid #fff;
}

/* css icons */
.gg-arrow-right {
  box-sizing: border-box;
  position: relative;
  display: block;
  transform: scale(var(--ggs, 1));
  width: 22px;
  height: 22px
}

.gg-arrow-right::after,
.gg-arrow-right::before {
  content: "";
  display: block;
  box-sizing: border-box;
  position: absolute;
  right: 3px
}

.gg-arrow-right::after {
  width: 9px;
  height: 9px;
  border-top: 2.5px solid;
  border-right: 2.5px solid;
  transform: rotate(45deg);
  bottom: 5px;
}

.gg-arrow-right::before {
  width: 22px;
  height: 2px;
  bottom: 9px;
  background: currentColor;
}
</style>

<script>
    export let teacher;
</script>

<div class="col-12">
    <div class="card mb-4 border-selective-yellow teacher-card wow fadeInUp" data-wow-delay="100ms"
        data-wow-duration="1000ms" style="cursor:pointer;">
        <!-- <a href="#" on:click={()=>{return false;}}> -->
        <div class="card-header position-relative">
            <div class="teacher-thumbnail">
                <img src="{document.body.dataset.staticurl}img/teacher-thumbnail/{teacher.img}" alt="{teacher.lang}">
            </div>
            <div class="language-icon">
                <img src="{document.body.dataset.staticurl}img/language-icon/{teacher.icon}" alt="{teacher.lang}">
            </div>
        </div>
        <!-- </a> -->
        <div class="card-body d-flex justify-content-between flex-column">
            <div class="">
                <div class="d-flex justify-content-between teacher-card-title align-items-center">
                <h4 class="text-atomic mb-0">{teacher.lang}</h4>
                <p class="pt-1">{teacher.teacherCount} Teachers</p>
                </div>
                <p class="justify-content-end d-flex align-items-center">
                    <a href="#" class="d-flex align-items-center text-selective-yellow">See All <span class="ml-3 see-all"><i class="gg-arrow-right"></i></span></a>
                </p>
            </div>
        </div>
    </div>
</div>
