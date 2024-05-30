<style>
.teacher-swiper-pagination {
    margin-top: 60px;
    display: flex;
    float: inherit;
    justify-content: center;
}

/* .teacher-swiper-pagination {
  margin-top: 80px;
  display: flex;
  float: right;
} */

@media only screen and (max-width: 767px) {
    .teacher-swiper-pagination {
        right: 50px;
        bottom: -30px;
        margin-top: 30px;
    }
}

.teacher-swiper-pagination :global(.swiper-pagination-bullet) {
    -webkit-transition-duration: 500ms;
    transition-duration: 500ms;
    -webkit-box-flex: 0;
    -ms-flex: 0 0 10px;
    flex: 0 0 10px;
    width: 10px;
    max-width: 10px;
    margin: 0 5px;
    height: 10px;
    border-radius: 12px;
    background-color: #DDE0E4;
}

.teacher-swiper-pagination :global(.swiper-pagination-bullet-active) {
    background-color: #FF792E;
    -webkit-box-flex: 0;
    -ms-flex: 0 0 26px;
    flex: 0 0 26px;
    width: 26px;
    max-width: 26px;
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
    .teacher-swiper-pagination :global(.swiper-pagination-bullet-active) {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 20px;
        flex: 0 0 20px;
        width: 20px;
        max-width: 20px;
    }
}

@media only screen and (max-width: 767px) {
    .teacher-swiper-pagination :global(.swiper-pagination-bullet-active) {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 20px;
        flex: 0 0 20px;
        width: 20px;
        max-width: 20px;
    }
}
</style>

<svelte:window bind:innerWidth={innerWidth}/>

<script>
    import { Swiper, SwiperSlide } from 'swiper/svelte';
    import 'swiper/swiper.scss';

    import SwiperCore, { Pagination } from 'swiper';
    SwiperCore.use([Pagination]);

    import TeacherCarouselSlide from 'ui/TeacherCarouselSlide.svelte';

    export let teachers;
    let innerWidth;
</script>
<Swiper
    spaceBetween={40}
    slidesPerView={1}
    breakpoints={{
        768: {
            slidesPerView: 2,
        },
        992: {
            slidesPerView: 3,
        },
        1200: {
            slidesPerView: 4,
        },
    }}
    pagination={{
        el: '.teacher-swiper-pagination',
        clickable: true,
        type: 'bullets',
        renderBullet: function (index, className) {
            return '<span class="' + className + '"></span>';
        }
    }}>
    {#if innerWidth<768}
        {#each teachers as teacher}
            <SwiperSlide>
                <TeacherCarouselSlide {teacher} />
            </SwiperSlide>
        {/each}
    {:else}
        {#each {length: teachers.length/2} as _, i}
            <SwiperSlide>
                <TeacherCarouselSlide teacher={teachers[i*2]} />
                {#if teachers.length>i*2+1}
                    <TeacherCarouselSlide teacher={teachers[i*2+1]} />
                {/if}
            </SwiperSlide>
        {/each}
    {/if}
</Swiper>
<div class="teacher-swiper-pagination"></div>