<div class="card-display">
  <div class="card-container">
    <Card>
      <PrimaryAction on:click={() => clicked++}>
        <Media class="card-media-16x9" aspectRatio="16x9" style="background-image: url({backgroundImage});">
          <MediaContent>
            <div
              style="color: #fff; position: absolute; bottom: 16px; left: 16px;"
            >
              <h1 class="mdc-typography--headline6" style="margin: 0;">
                {Name}
              </h1>
              <h3 class="mdc-typography--subtitle2" style="margin: 0;">
                Hours: {Hours}
              </h3>
            </div>
          </MediaContent>
        </Media>
        <Content class="mdc-typography--body2" style='padding-left: 5%; padding-right: 5%'>
          Activity Level
        </Content>
        <div style="padding-left: 5%; padding-right: 5%">
           
          <BusyBar repeat={5} progress={Progress}/>
        </div>

      </PrimaryAction>
      <Actions>
        <ActionIcons>
          <IconButton
            on:click={() => clicked++}
            toggle
            aria-label="Add to favorites"
            title="Add to favorites"
          >
            <Icon class="material-icons" on>favorite</Icon>
            <Icon class="material-icons">favorite_border</Icon>
          </IconButton>
          <IconButton
            class="material-icons"
            on:click={() => clicked++}
            title="More options">more_vert</IconButton
          >
        </ActionIcons>
      </Actions>
    </Card>
  </div>
</div>

<script lang="ts">
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
  import BusyBar from './BusyBar.svelte'

  export let backgroundImage = '/img/frank.jpeg';
  export let Name="woo";
  export let Hours="7am-12am"
  export let Progress=0.69;
  let clicked = 0;
</script>
