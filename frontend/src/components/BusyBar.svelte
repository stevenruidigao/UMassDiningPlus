{#each Array(repeat) as __, i}
    <LinearProgress class='my-colored-bar' progress={progress} closed={closed}/>
{/each}

<script lang="ts">
  import LinearProgress from '@smui/linear-progress';

  export let progress = 0.69;
  let closed = false;
  export let repeat = 1;
  
</script>

<style lang=scss>
  @use '@material/linear-progress/index' as linear-progress;
  @use '@material/theme/index' as theme;
  .my-colored-bar2 {
    @include linear-progress.bar-color(theme.$red-500);
    @include linear-progress.buffer-color(theme.$green-100);
  }
</style>
