# UMassDiningPlus
The UMass Dining app, but better.
## Inspiration
The original UMass Dining app has a feature that tells if a dining hall is “busy,” “moderate,” or “not busy.” On paper, it’s a useful widget: students plan out their time and dodge the lines. The only caveat is that it doesn’t work! Countless bogus readings and avoidable crowds led us to create our project, “UMass Dining+”! Our mobile-friendly website aims to accurately show how busy each dining common is by using youtube livestreams that monitor each eatery.

## What it does and How we built it
Our Python backend scans UMass-provided livestreams for Worcester, Berkshire, and Hampshire Dining Commons via the youtube-dl library before processing them with a computer vision machine learning model to estimate the number of people in the area. We used OpenCV in conjunction with an object detection model found on Hugging Face. The estimation of how busy the dining area is then gets sent to a Redis database.

We used Redis as a feature-packed key-value store to hold our estimates of the activity levels at the dining halls over time. Go was chosen as an efficient and simple language to serve static files and respond to API requests.

We used SockJS to stream the activity level data of each location to website visitors in real time, enabling the website to automatically update.

We used Sveltekit Material UI to design and build our frontend webpage. Svelte’s dynamic elements allowed us to develop a streamlined UI/UX. The Svelte and SCSS formatting files for the web app were compiled and deployed using Vite.

Our overall tech stack consists of Python, Redis, Go, and Svelte, and we host the website online using the free .tech domain offered by domains.com.

## Challenges we ran into
* Inaccurate detection models
* Connecting the database to the frontend
* Inconsistent package management between multiple build environments
* Dynamically updating CSS styles using SASS mix-ins

## Accomplishments that we're proud of
* An accurate human detection ML model
* A polished front end with mobile support
* A unique and adventurous tech stack
* It works!!! :)

## What's next for UMass Dining+
We will accumulate more data to add a graph displaying past trends of a particular dining hall based on the current day of the week. We will also implement expanding boxes for each dining hall to show more detailed information such as recent trends (past 30-60 minutes) in activity. In addition, we will add menus within the details of each dining hall as well.
