<script>
    import Select from 'ui/Select.svelte';
    import {countries} from 'ui/CountryFlag.svelte';
    
    import Item from 'ui/CountryFlagChooserItem.svelte';

    let countriesArray=[];
    for(let key in countries) {
        countriesArray = [...countriesArray, {
            key: key,
            value: countries[key],
        }];
    }

    export let label;
    export let required;
    export let country;

</script>

<Select
    placeholder={label}
    items={countriesArray}
    {Item}
    keyId='key'
    keyValue='value'
    isMulti={false}
    bind:selectedId={country}
    {label} {required}
    isVirtualList={false}
    />

    <!-- <Select items={countriesArray} {Item} Selection={Item}
        getOptionLabel={(option, filterText) => option.isCreator?filterText:option.value}
        getSelectionLabel={(option) => option.value}
        bind:selectedValue={selectedValue}
        isClearable={false}
        isCreatable={false}
        on:select={onSelect}
        /> -->
