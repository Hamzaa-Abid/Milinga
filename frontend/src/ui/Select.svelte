<!--
Vorteil:
* Falls Sprache (items) aktualisiert wird, wird Select auch aktualisiert
* selectedId wird automatisch upgedatet statt selectedValue
* Label wird unterstützt

import Select from 'ui/Select.svelte';

<Select
    placeholder={'What do you teach?'}
    items={$subjects}
    keyValue='subject'
    isMulti={true/false}
    on:select={...}
    bind:selectedId={sId / oIds} />

mit eigenem Item:
<Select
    placeholder={'What do you teach?'}
    items={countriesArray}
    {Item}
    keyId='key'
    keyValue='value'
    isMulti={false}
    bind:selectedId={countryCode}
    {label} {required}/>
-->
<script>
    import Select from 'svelte-select';
    import {createEventDispatcher} from 'svelte';

    export let items=[];
    export let Item;
    export let keyId='id';
    export let keyValue='value';
    export let selectedId;
    export let isMulti=false;
    export let label;
    export let placeholder=label;
    export let required=false;
    export let isVirtualList=false;

    let selectedValue;

    const dispatch = createEventDispatcher();

    $: items /* falls Sprache geändert wird */, selectedId, updateSelectedValueFromId();
    function updateSelectedValueFromId(){
        if(selectedId === undefined){
            selectedValue = undefined;
            return;
        }
        if(isMulti){
            selectedValue = selectedId.map((sId)=>getItemFromId(sId));
        } else {
            selectedValue = getItemFromId(selectedId);
        }
    }

    function getItemFromId(sId){
        let oRtn = {};
        oRtn[keyId] = sId;
        let oItem = items.find((o)=>o[keyId] === sId)
        oRtn[keyValue] = oItem?oItem[keyValue]:'';
        return oRtn;
    }

    function getIdFromItem(item){
        if(isMulti){
            return (item||[]).map(_item=>_item[keyId]);
        } else {
            return item[keyId];
        }
    }

    function onSelect(){
        selectedId = getIdFromItem(selectedValue);
        dispatch('select');
    }
</script>

{#if label}
    <div class="mb-3">
        <label class:requiredField={required}>
            {label}{#if required}<span class="asteriskField">*</span>{/if}
        </label>
        <Select {items} {Item} Selection={Item}
            bind:selectedValue={selectedValue}
            optionIdentifier={keyId}
            {placeholder}
            getOptionLabel={(option, filterText) => option.isCreator?filterText:option[keyValue]}
            getSelectionLabel={(option) => option[keyValue]}
            createItem={(filterText) => {return { keyId:filterText, keyValue:filterText }}}
            isClearable={true}
            isCreatable={false}
            {isMulti}
            on:select={onSelect}
            {isVirtualList} />
    </div>
{:else}
    <Select {items} {Item} Selection={Item}
        bind:selectedValue={selectedValue}
        optionIdentifier={keyId}
        {placeholder}
        getOptionLabel={(option, filterText) => option.isCreator?filterText:option[keyValue]}
        getSelectionLabel={(option) => option[keyValue]}
        createItem={(filterText) => {return { keyId:filterText, keyValue:filterText }}}
        isClearable={true}
        isCreatable={false}
        {isMulti}
        on:select={onSelect}
        {isVirtualList} />
{/if}