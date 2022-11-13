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

  //import sock from 'sockjs-client';

  import Button, { Label } from '@smui/button';
  import IconButton, { Icon } from '@smui/icon-button';
  import LayoutGrid, { Cell } from '@smui/layout-grid';
  import ComplexCard from '../components/ComplexCard.svelte';
  import SockJS from 'sockjs-client';
  // Temporary
  const locations = ["worcester", "hampshire", "berkshire", "franklin"];
  const names = ["Worcester Dining Commons", "Hampshire Dining Commons", "Berkshire Dining Commons", "Franklin Dining Commons"];
  const pics = ["woo.jpeg","hamp.jpeg","berk.jpeg","frank.jpeg"];
  const hours = ["7am-12am", "7am-9am", "7am-9am", "11am-12am"];
  let busyness = [0, 0, 0, 0];
  let sock = new SockJS("https://umassdiningplus.tech/api/v1/socket");

  sock.onopen = function() {
    console.log("Connected.");
  };

  sock.onmessage = function(e) {
    let details = JSON.parse(e.data);
    
    for (let i = 0; i < details.length; i ++) {
      busyness[locations.indexOf(details[i].location)] = details[i].loads[details[i].loads.length - 1] == undefined ? 0.5 : details[i].loads[details[i].loads.length - 1];
    }

    busyness = busyness;
  };
</script>

<LayoutGrid>
    {#each names as name, i}
      <Cell span={6}>
        <ComplexCard backgroundImage="/img/{pics[i]}" Name={name} Hours={hours[i]} Progress={busyness[i]}></ComplexCard>
      </Cell>
    {/each}
</LayoutGrid>
 
<style>

</style>