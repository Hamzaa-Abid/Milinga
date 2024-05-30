<style>
/*---------------------------------------------------------- */
img {
  max-width: 100%;
  height: auto;
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


/* Client Feedback CSS */
.client-feedback-area {
  position: relative;
  z-index: 1;
  overflow: hidden;
}

/* 
.client-feedback-area .owl-stage-outer {
  right: -50px;
} */

@media only screen and (max-width: 767px) {
  .client-feedback-area .owl-stage-outer {
    right: 0;
  }
}

.client-feedback-area .client-shape {
  position: absolute !important;
  top: -1px;
  left: -1px;
  z-index: -1;
}

.client-feedback-heading {
  position: relative;
  z-index: 1;
  -webkit-box-flex: 0;
  -ms-flex: 0 0 46%;
  flex: 0 0 46%;
  max-width: 46%;
  width: 46%;
  padding-right: 50px;
}

@media only screen and (max-width: 767px) {
  .client-feedback-heading {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 100%;
    flex: 0 0 100%;
    max-width: 100%;
    width: 100%;
    margin-bottom: 50px;
  }
}

.client-feedback-heading .section-heading {
  max-width: 400px;
  margin-left: auto;
}

.client-feedback-content {
  position: relative;
  z-index: 1;
}

@media only screen and (max-width: 767px) {
  .client-feedback-content {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 100%;
    flex: 0 0 100%;
    max-width: 100%;
    width: 100%;
  }
}

.client-feedback-content .feedback-card {
  position: relative;
  z-index: 1;
  border-radius: 10px;
  border-width: 2.5px;
  border-style: solid;
  background-color: #f4f4ff;
  padding: 20px;
  text-align: left;
}

.client-feedback-content .feedback-card .card-body {
  padding: 0;
}

.client-feedback-content .feedback-card:hover {
  border-color: #FF792E !important;
}

.client-feedback-content .feedback-card p {
  font-size: 16px;
  line-height: 1.5rem;
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .client-feedback-content .feedback-card p {
    font-size: 14px;
  }
}

@media only screen and (min-width: 576px) and (max-width: 767px) {
  .client-feedback-content .feedback-card p {
    font-size: 14px;
  }
}

.client-feedback-content .feedback-card .client-info .client-thumb {
  -webkit-box-flex: 0;
  -ms-flex: 0 0 40px;
  flex: 0 0 45px;
  max-width: 45px;
  width: 45px;
  border-radius: 6px;
  margin-right: 15px;
  margin-top: -4px;
}

.client-feedback-content .feedback-card .client-info .client-thumb img {
  border-radius: 6px;
}

.client-feedback-content .feedback-card .client-info .client-name h6 {
  margin-bottom: 5px;
  font-size: 16px;
}

.client-feedback-content .feedback-card .client-info .client-name p {
  margin-bottom: 0;
  font-size: 14px;
}
</style>

<script>
	export let clientFeedback={};
</script>

<div class="card feedback-card bg-white border-gainsboro">
	<div class="card-body">
		<div class="client-info d-flex align-items-center">
		<div class="client-thumb"><img src={clientFeedback.img?clientFeedback.img:document.body.dataset.staticurl+"img/review-thumbnail/placeholder.png"} alt=""></div>
		<div class="client-name">
			<h6>{clientFeedback.name}</h6>
			<p>{clientFeedback.location}</p>
		</div>
		</div>
		<p class="mb-0 mt-3">{clientFeedback.feedback}</p>
	</div>
</div>