<script>
    export let length = '100%';
    export let height = '20px';
    export let progress = 0.5;
    export let from = '00ff00';
    export let to = 'ff0000';
    export let direction = 'to right';
    export let colorDirection = -1;

    let leftColorRGB = hexToBytes(from);
    $: leftColorRGB = hexToBytes(from);
    let rightColorRGB = hexToBytes(to);
    $: rightColorRGB = hexToBytes(to);
    let gradient = hslGradient(direction, colorDirection, rgb2HSL(leftColorRGB[0]/255, leftColorRGB[1]/255, leftColorRGB[2]/255), rgb2HSL(rightColorRGB[0]/255, rightColorRGB[1]/255, rightColorRGB[2]/255), progress);
    $: gradient = hslGradient(direction, colorDirection, rgb2HSL(leftColorRGB[0]/255, leftColorRGB[1]/255, leftColorRGB[2]/255), rgb2HSL(rightColorRGB[0]/255, rightColorRGB[1]/255, rightColorRGB[2]/255), progress);

    /**
     * @param {string} hexString - A hex string
     */

    function hexToBytes(hexString) {
        let bytes = [];
        
        for (let c = 0; c < hexString.length; c += 2) {
            bytes.push(parseInt(hexString.substring(c, c + 2), 16));
        }

        return bytes;
    }

    /**
     * @param {number} red - Integer from 0 to 255
     * @param {number} green - Integer from 0 to 255
     * @param {number} blue - Integer from 0 to 255
     */

    function rgb2HSL(red, green, blue) {
        let v = Math.max(red, green, blue)
        let c = v - Math.min(red, green, blue)
        let f = (1 - Math.abs(v + v - c - 1)); 
        let h = c && ((v == red) ? (green - blue) / c : ((v == green) ? 2 + (blue - red) / c : 4 + (red - green) / c)); 
        return [60 * (h < 0 ? h + 6 : h), f ? c / f : 0, (v + v - c) / 2];
    }

    /**
     * @param {string} direction
     * @param {number} colorDirection
     * @param {Array<number>} fromHSL
     * @param {Array<number>} toHSL
     * @param {number} progress
     */

    function hslGradient(direction, colorDirection, fromHSL, toHSL, progress) {
        let currentString = 'linear-gradient(' + direction;
        let hsl = [];

        for (let value of fromHSL) {
            hsl.push(value);
        }
        
        let endHSL = [0, 0, 0];
        endHSL[0] = fromHSL[0] + (toHSL[0] - fromHSL[0]) * progress;
        endHSL[1] = fromHSL[1] + (toHSL[1] - fromHSL[1]) * progress;
        endHSL[2] = fromHSL[2] + (toHSL[2] - fromHSL[2]) * progress;

        while (colorDirection >= 0 ? hsl[0] < endHSL[0] : hsl[0] > endHSL[0]) {
            let differenceFromNext;

            if (colorDirection >= 0) {
                differenceFromNext = toHSL[0] - hsl[0] > 60 - (hsl[0] % 60) ? 60 - (hsl[0] % 60) : toHSL[0] - hsl[0];

            } else {
                let hslMod60Min60 = (hsl[0] % 60 == 0 ? 60 : hsl[0] % 60);
                differenceFromNext = hsl[0] - toHSL[0] > hslMod60Min60 ? hslMod60Min60 : hsl[0] - toHSL[0];
                differenceFromNext *= -1;
            }

            console.log(currentString);
            currentString += ', hsl(' + hsl[0] + ', ' + hsl[1] * 100 + '%, ' + hsl[2] * 100 + '%) ' + (hsl[0] - fromHSL[0]) / (toHSL[0] - fromHSL[0]) / progress * 100 + '%';
            hsl[0] += differenceFromNext;
        }

        currentString += ', hsl(' + (fromHSL[0] + (toHSL[0] - fromHSL[0]) * progress) + ', ' + (fromHSL[1] + (toHSL[1] - fromHSL[1]) * progress) * 100 + '%, ' + (fromHSL[2] + (toHSL[2] - fromHSL[2]) * progress) * 100 + '%) ' + '100%)';
        return currentString;
    }
</script>

<div class="bar-grey" style="width: {length}; height: {height};">
    <div class="bar-rainbow" style="width: {Math.round(progress * 100)}%; height: {height}; background: {gradient};">
    </div>
</div>

<style>
    .bar-grey {
        border: 4px black;
        border-radius:   10px;
        background-color: rgb(218, 220, 219);
        display: flex;
        flex-direction: row;
        gap: 0px;
    }

    .bar-rainbow {
        border-radius: 10px 10px 10px 10px;
    }
</style>
