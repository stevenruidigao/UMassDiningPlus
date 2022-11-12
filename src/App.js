import * as React from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';

import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardHeader from '@mui/material/CardHeader';
import StarIcon from '@mui/icons-material/StarBorder';

import berkimg from './img/berk.jpeg';
import hampimg from './img/hamp.jpeg';
import wooimg from './img/woo.jpeg';
import frankimg from './img/frank.jpeg';
import marketimg from './img/market.jpeg';

const styles = theme => ({
    heroContent: {
        maxWidth: 600,
        margin: '0 auto',
        padding: `${theme.spacing.unit * 8}px 0 ${theme.spacing.unit * 6}px`,
    },
});

const tiers = [
    {
        title: 'Worcester',
        price: 'Very Crowded',
        img: wooimg,
        description: 'Closes 12:00 AM',
        buttonText: 'Watch the livestream'
    },

    {
        title: 'Franklin',
        price: 'Crowded',
        img: frankimg,
        description: 'Closes 10:00 PM',
        buttonText: 'Watch the livestream'
    },

    {
        title: 'Berkshire',
        price: 'Not Busy',
        img: berkimg,
        description: 'Closes 12:00 AM',
        buttonText: 'Watch the livestream'
    },

    {
        title: 'Hampshire',
        price: 'Crowded',
        img: hampimg,
        description: 'Closes 10:00 PM',
        buttonText: 'Watch the livestream'
    },

    {
        title: 'Harvest Market',
        price: 'Not Busy',
        img: marketimg,
        description: 'Closes 9:00 PM',
        buttonText: 'Watch the livestream'
    },
];

export default function App() {
    return (
        <main className='mainContainer'>
            <Box bgcolor='#cdff8c' height={8} className='ribbon'>
                
            </Box>

            <div className={''}>
                <Typography component="h1" variant="h2" align="center" color="textPrimary" gutterBottom className='title'>
                    DC Traffic Dashboard
                </Typography>
                <Typography variant="h6" align="center" color="textSecondary" component="p">
                    How busy is your favorite dining common? 🏃
                </Typography>
            </div>

            <Grid container spacing={4} className='heroGridContainer' width='80vw'>
                {tiers.sort((a, b) => {
                    const encode = label => 
                        label === 'Very Crowded' ? 
                            2 :
                        label === 'Crowded'?
                            1 : 0;
                    console.log("REEE")
                    return encode(a.price) - encode(b.price)
                }).map(tier => (
                    <Grid item key={tier.title} xs={12} sm={6} md={4}>
                        <Card>
                            <CardHeader
                                title={tier.title}
                                subheader={tier.subheader}
                                titleTypographyProps={{ align: 'center' }}
                                subheaderTypographyProps={{ align: 'center' }}
                                action={<StarIcon/>}
                                className={''}
                            />

                            <CardContent>
                                <Box overflow={'hidden'} borderRadius={2}>
                                    <Box component='img'
                                        height='16em'
                                        src={tier.img}>
                                    </Box>
                                </Box>
                                

                                <div className={''}>
                                    <Box bgcolor={
                                        tier.price === 'Very Crowded' ?
                                            '#ff4d4d' :
                                        tier.price === 'Crowded' ?
                                            '#ffdc7a' :
                                            '#cdff8c'
                                    } borderRadius={2} className='trafficLabelContainer'>
                                        <Typography variant="h4" align='center' color="textPrimary" className='trafficLabel'>
                                            {tier.price}
                                        </Typography>
                                    </Box>
                                </div>

                                {/*<Typography variant="subtitle1" align="center" className='closingTimeLabel'>
                                    {tier.description}
                                </Typography>*/}
                            </CardContent>

                            <CardActions className={''}>
                                <Button fullWidth variant={tier.buttonVariant} color="primary">
                                    {tier.buttonText}
                                </Button>
                            </CardActions>
                        </Card>
                    </Grid>
                ))}
            </Grid>

            <footer className='footer'>
                <Typography align="center" color="textSecondary" className='footerText'>
                    Brought to you by DC Traffic Metrics LLC.
                </Typography>
            </footer>
        </main>
    );
}