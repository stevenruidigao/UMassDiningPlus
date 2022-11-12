<script lang="ts">
	// import Button, { Label, Icon } from '@smui/button';
  import Card, {
    Content,
    PrimaryAction,
    Media,
    MediaContent,
    Actions,
    ActionButtons,
    ActionIcons,
  } from '@smui/card';
  import Button, { Label } from '@smui/button';
  import IconButton, { Icon } from '@smui/icon-button';
  import LayoutGrid, { Cell } from '@smui/layout-grid';
  import ComplexCard from '../components/ComplexCard.svelte';
  
</script>

<LayoutGrid>
    {#each Array(4) as _unused, _i}
      <Cell span={6}>
        <ComplexCard backgroundImage="/img/berk.jpeg"></ComplexCard>
      </Cell>
    {/each}
</LayoutGrid>
 
<style>
  .demo-cell {
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: var(--mdc-theme-secondary, #333);
    color: var(--mdc-theme-on-secondary, #fff);
  }
</style>

<!-- <ComplexCard></ComplexCard> -->