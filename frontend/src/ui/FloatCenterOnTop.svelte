<!--
    <FloatCenter>
        <div slot="bg">
            ...
        </div>
        <div slot="fg">
            ...
        </div>
    </FloatCenter>
-->

<style>
    div {
        position:relative;
    }

    .center_on_element {
        display:block;
        position: absolute;
        top:50%;
        left:50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
    }
</style>
<div>
    <slot name="bg"/>
    <div class="center_on_element" >
        <slot name="fg"/>
    </div>
</div>