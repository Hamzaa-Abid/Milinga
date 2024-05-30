<script>
    import Fa from 'svelte-fa';
    import TextField from 'ui/TextField.svelte';
    import Select from 'ui/Select.svelte';
    import {subjects} from 'store/subjects.js';

    import TextArea from 'ui/TextArea.svelte';

    // let subjects = [
    //     {
    //         id: '14',
    //         value: 'Deutsch',
    //     },
    //     {
    //         id: '17',
    //         value: 'Englisch',
    //     },
    //     {
    //         id: '21',
    //         value: 'Spanisch',
    //     },
    //     {
    //         id: '31',
    //         value: 'Französisch',
    //     },
    // ]

    export let teaches;
    export let description;
    export let videoUrl;
    export let pricePerHour;
    export let currency = 'USD';
</script>

<!-- <h1>Teacher-Profile</h1> -->
<div class="row">
        <div class="col-lg-12 col-md-12 col-sm-12 col-12">
            <Select
                placeholder={'What do you teach?'}
                items={$subjects}
                keyValue='subject'
                isMulti={true}
                bind:selectedId={teaches}
                label='I teach:'
                required={true}
                 />
        </div>
        <div class="col-lg-12 col-md-12 col-sm-12 col-12">
            <TextArea
                label='description'
                required={true}
                rows={10}
                bind:value={description} />
        </div>
        <div class="col-lg-12 col-md-12 col-sm-12 col-12">
            <TextField
                type='url'
                label='Video URL'
                required={true}
                bind:value={videoUrl} />
        </div>
        <div class="col-12 d-flex align-items-left">
            <TextField
                type='number'
                label={`Price in ${currency} per hour`}
                required={true}
                bind:value={pricePerHour} />
        </div>
</div>
<!-- {{ teacher_form.videoUrl|as_crispy_field }}
{{ teacher_form.pricePerHour|as_crispy_field }}
{{ teacher_form.pricePerHour.errors }}

{% comment %}
{#% render_field teacher_form.pricePerHour %#}
{#% render_field teacher_form.pricePerHour.1 %#}
<div class="row">
<div class="col-lg-2 col-md-3 col-xs-auto">{% render_field teacher_form.pricePerHour.amount %}</div>
<div class="col-lg-5 col-md-6 col-xs-auto">{% render_field teacher_form.pricePerHour.currency class+="select2" %}</div>
</div>
{{ teacher_form.pricePerHour.errors }}
{% endcomment %} -->