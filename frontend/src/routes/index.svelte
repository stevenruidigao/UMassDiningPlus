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
  
  // Temporary
  const locs = ["Worcester Dining Commons", "Hampshire Dining Commons", "Berkshire Dining Commons", "Franklin Dining Commons"];
  const pics = ["woo.jpeg","hamp.jpeg","berk.jpeg","frank.jpeg"];
  const hours = ["7am-12am", "7am-9am", "7am-9am", "11am-12am"];

</script>

<LayoutGrid>
    {#each locs as loc, i}
      <Cell span={6}>
        <ComplexCard backgroundImage="/img/{pics[i]}" Name={loc} Hours={hours[i]}></ComplexCard>
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