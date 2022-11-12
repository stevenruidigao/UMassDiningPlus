<script>
    const DCs = [
        {
            name: 'Worcester',
            status: 'Very Crowded',
            img: './img/woo.jpeg',
            description: 'Closes 12:00 AM',
            buttonText: 'WATCH THE LIVESTREAM',
            colorCSS: 'background-color: #cdff8c;',
            href: 'https://google.com'
        },

        {
            name: 'Franklin',
            status: 'Crowded',
            img: './img/frank.jpeg',
            description: 'Closes 10:00 PM',
            buttonText: 'WATCH THE LIVESTREAM',
            colorCSS: 'background-color: #cdff8c;',
            href: 'https://google.com'
        },

        {
            name: 'Berkshire',
            status: 'Not Busy',
            img: './img/berk.jpeg',
            description: 'Closes 12:00 AM',
            buttonText: 'WATCH THE LIVESTREAM',
            colorCSS: 'background-color: #cdff8c;',
            href: 'https://google.com'
        },

        {
            name: 'Hampshire',
            status: 'Crowded',
            img: './img/hamp.jpeg',
            description: 'Closes 10:00 PM',
            buttonText: 'WATCH THE LIVESTREAM',
            colorCSS: 'background-color: #cdff8c;',
            href: 'https://google.com'
        },

        {
            name: 'Harvest Market',
            status: 'Not Busy',
            img: './img/market.jpeg',
            description: 'Closes 9:00 PM',
            buttonText: 'WATCH THE LIVESTREAM',
            colorCSS: 'background-color: #cdff8c;',
            href: 'https://google.com'
        },
    ];

</script>

<div class="top-container">
    <div class="ribbon">

    </div>

    <div class="hero-text-container">
        <div class="title-text">DC Traffic Dashboard</div>
        <div class="flavor-text">How busy is your favorite dining common? 🏃</div>

    </div>

    <div class="grid-container">
        {#each DCs as DC}
            <div class="card">
                <div class="card-title">{DC.name}</div>
                <div class="image-container">
                    <img src={DC.img} class="card-image">
                </div>
                <div class="card-status" style={DC.colorCSS}>{DC.status}</div>
                <button class="card-button">
                    <a href={DC.href}>{DC.buttonText}</a>
                </button>
            </div>
        {/each}
    </div>

    <div class='footer'>
        <div class='footer-text'>
            Brought to you by DC Traffic Metrics LLC.
        </div>
    </div>
</div>

<style>
    .top-container {
        width: 100vw;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .ribbon {
        position: absolute;
        width: 100vw;
        height: 10px;
        background-color: #cdff8c;
        top: 0;
        left: 0;
    }

    .hero-text-container{
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .title-text {
        font-size: 3.5em;
        padding-top: 0.5em;
    }

    .flavor-text {
        font-size: 1.25em;
        padding: 0.5em;
    }

    .grid-container {
        width: 80%;
        padding-top: 2em;

        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 10px;
        grid-auto-rows: minmax(100px, auto);
        row-gap: 2em;
    }

    .card {
        width: 18em;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-left: auto;
        margin-right: auto;

        border-radius:8px;
        box-shadow: 0px 2px 1px -1px rgb(0 0 0 / 20%), 0px 1px 1px 0px rgb(0 0 0 / 14%), 0px 1px 3px 0px rgb(0 0 0 / 12%);
    }

    .card-title {
        padding-top: 0.5em;
        padding-bottom: 00.5em;
        font-size: 1.5em;
    }

    .image-container {
        width: 80%;
        overflow: hidden;
        border-radius: 8px;
    }

    .card-image {
        height: 14em;
    }

    .card-status {
        width: 70%;
        font-size: 1.5em;
        padding: 0.5em;
        border-radius: 8px;
        text-align: center;
    }

    .card-button {
        padding: 1em;
        width: 80%;
        border: none;
        background-color: white;
    }

    .footer {
        margin-top: 2em;
        border-top: 1px solid rgba(0, 0, 0, 0.12);
        width: 80vw;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .footer-text {
        padding: 2em;
        padding-top: 1em;
    }
</style>
