<script>
    import moment from 'moment-timezone';
    import Select from 'svelte-select';
    import LabelForInput from 'ui/LabelForInput.svelte';

    // export let timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    export let timezone = moment.tz.guess();
    export let label;
    export let required;

    let selectedValue = timezone;
    $: timezone = selectedValue ? selectedValue.value : undefined;

    const timezones = moment.tz.names();
</script>
<LabelForInput {label} {required}>
    <Select items={timezones} {label} bind:selectedValue showChevron={true}/>
</LabelForInput>