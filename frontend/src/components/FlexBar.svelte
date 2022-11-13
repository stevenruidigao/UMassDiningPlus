<script>
export let length = 100;
export let height = 20;
export let progress = 0.5;


var greenProg = 100*Math.min(progress, 0.34);
var yellowProg = 100*Math.max(0, Math.min(progress-0.33,0.34));
var redProg = 100*Math.max(0, Math.min(progress-0.66,0.34));

</script>

<div class="flexbar-container" style="width:{length}%;height:{height}px;" >
    <div class="bar-green" style="width:{greenProg}%">
    </div>
    <div class="bar-yellow"  style="width:{yellowProg}%">
    </div>
    <div class="bar-red"  style="width:{redProg}%">

    </div>
</div>
<style>
.flexbar-container {
    border:4px black;
    border-radius:20px;
    background-color: rgb(218, 220, 219);
    display:flex;
    flex-direction:row;
    justify-content: flex-start;
    gap:0px;
}
.bar-green {
    border-radius:20px 0px 0px 20px;
    background-color: #66bb6a; /*linear-gradient(to right, green, yellow)*/
}
.bar-yellow {
    background-color: #ffeb3b;
}
.bar-red {
    border-radius:0px 20px 20px 0px;
    background-color: #ef5350;
}
</style>