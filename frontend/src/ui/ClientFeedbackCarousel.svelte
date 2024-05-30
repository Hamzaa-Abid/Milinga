<style>
.clientfeedback-swiper-pagination {
  margin-top: 80px;
  display: flex;
  float: right;
}

@media only screen and (max-width: 767px) {
  .clientfeedback-swiper-pagination {
    right: 50px;
    bottom: -30px;
    margin-top: 30px;
  }
}

.clientfeedback-swiper-pagination :global(.swiper-pagination-bullet) {
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

.clientfeedback-swiper-pagination :global(.swiper-pagination-bullet-active) {
  background-color: #FF792E;
  -webkit-box-flex: 0;
  -ms-flex: 0 0 26px;
  flex: 0 0 26px;
  width: 26px;
  max-width: 26px;
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
	.clientfeedback-swiper-pagination :global(.swiper-pagination-bullet-active) {
		-webkit-box-flex: 0;
		-ms-flex: 0 0 20px;
		flex: 0 0 20px;
		width: 20px;
		max-width: 20px;
	}
}

@media only screen and (max-width: 767px) {
	.clientfeedback-swiper-pagination :global(.swiper-pagination-bullet-active) {
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
    import 'swiper/css';

    import SwiperCore, { Pagination } from 'swiper';
    SwiperCore.use([Pagination]);

    import ClientFeedbackSlide from 'ui/ClientFeedbackCarousel_Slide.svelte';

    export let clientFeedback;
    let innerWidth;
</script>
<Swiper
	spaceBetween={40}
	slidesPerView={1}
	breakpoints={{
		0: {
			slidesPerView: 1,
			spaceBetween: 0
		},
		576: {
			slidesPerView: 1,
			spaceBetween: 15
		},
		768: {
			slidesPerView: 2
		},
		992: {
			slidesPerView: 3
		},
	}}
	pagination={{
		el: '.clientfeedback-swiper-pagination',
		clickable: true,
		type: 'bullets',
		renderBullet: function (index, className) {
			return '<span class="' + className + '"></span>';
		}
	}}>
	{#each clientFeedback as clientFeedbackSlide}
		<SwiperSlide>
			<ClientFeedbackSlide clientFeedback={clientFeedbackSlide} />
		</SwiperSlide>
	{/each}
</Swiper>
<div class="clientfeedback-swiper-pagination"></div>