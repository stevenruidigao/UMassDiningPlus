<script lang="ts">
	import Button from '@smui/button';
	import type { TopAppBarComponentDev } from '@smui/top-app-bar';
	import TopAppBar, { Row, Section, Title, AutoAdjust } from '@smui/top-app-bar';
	import IconButton from '@smui/icon-button';
	import { Label, Icon } from '@smui/common';
	// import { Svg } from '@smui/common/elements';
	// import { mdiGithub, mdiWeb } from '@mdi/js';

	let topAppBar: TopAppBarComponentDev;

	let lightTheme =
		typeof window === 'undefined' || window.matchMedia('(prefers-color-scheme: light)').matches;
	function switchTheme() {
		lightTheme = !lightTheme;
		let themeLink = document.head.querySelector<HTMLLinkElement>('#theme');
		if (!themeLink) {
			themeLink = document.createElement('link');
			themeLink.rel = 'stylesheet';
			themeLink.id = 'theme';
		}
		themeLink.href = `/smui${lightTheme ? '' : '-dark'}.css`;
		document.head
			.querySelector<HTMLLinkElement>('link[href$="/smui-dark.css"]')
			?.insertAdjacentElement('afterend', themeLink);
	}
</script>

<TopAppBar bind:this={topAppBar} variant="standard" style="background-color: #881c1c;">
	<Row>
		<Section>
			<div style="display: flex; align-items: center;">
				<IconButton class="material-icons" ripple={false}
				  >fastfood</IconButton
				>
			  </div>
			<Title>UMass Dining+</Title>
		</Section>
	</Row>
</TopAppBar>

<!--link rel="stylesheet" href="/static/smui.css" media="(prefers-color-scheme: light)" />
<link
  rel="stylesheet"
  href="/static/smui-dark.css"
  media="screen and (prefers-color-scheme: dark)"
/-->

<AutoAdjust {topAppBar} style="display: flex; justify-content: space-between;">
	<div class="container" style="width: 100%;"><slot /></div>
	<!-- <div class="container" style="position: fixed;">
		<Button on:click={switchTheme}>
			<Label>{lightTheme ? 'Lights off' : 'Lights on'}</Label>
		</Button>
	</div> -->
</AutoAdjust>
