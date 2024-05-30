<style>
.number-input button {
  -webkit-appearance: none;
  background-color: transparent;
  border: none;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin: 0;
  position: relative;
}
.number-input button:before,
.number-input button:after {
  display: inline-block;
  position: absolute;
  content: '';
  height: 2px;
  transform: translate(-50%, -50%);
}
.number-input button.plus:after {
  transform: translate(-50%, -50%) rotate(90deg);
}
.number-input input[type=number] {
  text-align: center;
}


.md-number-input.number-input {
  width: 11.8rem;
}
.md-number-input.number-input button {
  outline: none;
  width: 3rem;
  height: 1.2rem;
}
.md-number-input.number-input button:before,
.md-number-input.number-input button:after {
  width: 1rem;
  background-color: #212121;
}
.md-number-input.number-input input[type=number] {
  max-width: 5rem;
  font-size: 1.4rem;
  height: 1.4rem;
  font-weight: bold;
  outline: none;
}
@media not all and (min-resolution:.001dpcm)
{ @supports (-webkit-appearance:none) and (stroke-color:transparent) {
  .number-input.md-number-input.safari_only button:before, 
  .number-input.md-number-input.safari_only button:after {
    margin-top: -.6rem;
  }
}}
</style>



<script>
    import Fa from 'svelte-fa';
    import {faPlus, faMinus} from '@fortawesome/free-solid-svg-icons';

    import Clickable from 'ui/Clickable.svelte';

    export let value=0;
</script>

<div class="number-input md-number-input">
    <Clickable on:click={()=>value--}><Fa icon={faMinus} size="1.5x" color="red"/></Clickable>
    <!-- <button onclick="this.parentNode.querySelector('input[type=number]').stepDown()" class="minus"></button> -->
    <input class="quantity" {value} type="number">
    <Clickable on:click={()=>value++}><Fa icon={faPlus} size="1.5x" color="green"/></Clickable>
    <!-- <button onclick="this.parentNode.querySelector('input[type=number]').stepUp()" class="plus"></button> -->
</div>