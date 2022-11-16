
<Card>
    <Media class="card-media-16x9" aspectRatio="16x9" style="background-image: 
    linear-gradient(to bottom, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.75)), url({backgroundImage});">
        <MediaContent>
            <div style="color: #fff; position: absolute; bottom: 16px; left: 16px;">
                {#if windowWidth < 800}
                    <h1 class="mdc-typography--headline1"
                    style="margin: 0; padding-left: 2%; padding-top: 10%; font-size:2em; line-height:110%">
                        {name}
                    </h1>

                {:else}
                    <h1 class="mdc-typography--headline1"
                    style="margin: 0; padding-left: 2%; padding-top: 10%; font-size:4em; line-height:130%">
                        {name}
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
                    {#if progress <= 0.33}
                        Not Busy

                    {:else if progress <= 0.67}
                        Moderate

                    {:else}
                        Busy
                    {/if}
                </span>

                <h3 class="mdc-typography--headline5" style="margin: 0; align: right;
                font-size:1.1em">
                Hours: {hours}
                </h3>
            </div>
        </Content>

    {:else}
        <Content class="mdc-typography--headline5" style='padding-left: 5%;
        padding-right: 5%; padding-top: 2.5%; padding-bottom: 2.5%; font-size: 1.75em'>
            <div class = "info-container">
                <span>
                Activity Level: 
                {#if progress <= 0.33}
                    Not Busy

                {:else if progress <= 0.67}
                    Moderate

                {:else}
                    Busy
                {/if}
                </span>

                <h3 class="mdc-typography--headline5" style="margin: 0; align: right;
                font-size: 1em">
                    Hours: {hours}
                </h3>
            </div>
        </Content>
    {/if}

    <div style="padding-left: 5%; padding-right: 5%">
        <FlexBar progress={progress}/>
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

    export let backgroundImage = '';
    export let name = '';
    export let hours = ''
    export let progress = 0.5;

    let windowWidth = 0;
</script>

<style>
    .info-container {
        display: flex;
        flex-direction:row;
        justify-content: space-between;
    }
</style>