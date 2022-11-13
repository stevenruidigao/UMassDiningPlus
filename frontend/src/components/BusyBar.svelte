{#each Array(repeat) as __, i}
    <LinearProgress class='my-colored-bar' progress={progress} closed={closed}/>
{/each}

<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import LinearProgress from '@smui/linear-progress';

  let progress = 0.69;
  let closed = false;
  export let repeat = 1;
  
</script>

<style>
  /* md-progress-linear .md-container {
    height: 200px;
  }

  md-progress-linear .md-container .md-bar .mdc-linear-progress__bar-inner mdc-linear-progress__bar-inner {
      height: 200px;
      border-color: black;
      border-width: 100px;
  }

  .lp-bar {
    color: aliceblue;
    background-color: rebeccapurple;
    colorPrimary: aliceblue;
    colorSecondary: rebeccapurple;
  } */
</style>