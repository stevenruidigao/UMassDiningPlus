<div class="card-display">
  <div class="card-container">
    <Card>
        <Media class="card-media-16x9" aspectRatio="16x9" style="background-image: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.73)), url({backgroundImage});">
          <MediaContent>
            <div
              style="color: #fff; position: absolute; bottom: 16px; left: 16px;"
            >
            {#if windowWidth < 400}
            <h1 class="mdc-typography--headline1"
            style="margin: 0; padding-left: 2%; padding-top: 10%; font-size:2em; line-height:110%">
              {Name}
            </h1>
          {:else}
            <h1 class="mdc-typography--headline1"
            style="margin: 0; padding-left: 2%; padding-top: 10%; font-size:4em; line-height:130%">
              {Name}
            </h1>
          {/if}
            </div>
          </MediaContent>
        </Media>
        {#if windowWidth < 400}
        <Content class="mdc-typography--headline5" style='padding-left: 5%; padding-right: 5%;
        font-size:1.1em'>
          <div class = "info-container">
            <span>
            {#if Progress <= 0.33}
              Not Busy
            {:else if Progress <= 0.67}
              Moderate
            {:else}
              Busy
            {/if}
            </span>

            <h3 class="mdc-typography--headline5" style="margin: 0; align: right;
            font-size:1.1em">
              Hours: {Hours}
            </h3>
        </div>
        </Content>
          {:else}
          <Content class="mdc-typography--headline5" style='padding-left: 5%;
           padding-right: 5%; padding-top: 2.5%; padding-bottom: 2.5%; font-size: 1.75em'>
            <div class = "info-container">
              <span>
              Activity Level - 
              {#if Progress <= 0.33}
                Not Busy
              {:else if Progress <= 0.67}
                Moderate
              {:else}
                Busy
              {/if}
              </span>
  
              <h3 class="mdc-typography--headline5" style="margin: 0; align: right;
              font-size: 1em">
                Hours: {Hours}
              </h3>
          </div>
          </Content>
          {/if}
        <div style="padding-left: 5%; padding-right: 5%">
           
          <FlexBar progress = {Progress}/>
        </div>

      <Actions>
        <!-- <ActionIcons>
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
        </ActionIcons> -->
      </Actions>
    </Card>
  </div>
</div>

<svelte:window bind:innerWidth={windowWidth}/>

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
  import FlexBar from './FlexBar.svelte';

  export let backgroundImage = '/img/frank.jpeg';
  export let Name="woo";
  export let Hours="7am-12am"
  export let Progress=0.69;

  let windowWidth = 0;

  let clicked = 0;
</script>

<style>
.info-container {
  display: flex;
  flex-direction:row;
  justify-content: space-between;
}
</style>