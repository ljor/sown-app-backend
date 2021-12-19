# Sown App (Backend)

Sown is a seed starting planner that helps users figure out when to start planting seeds based on their last frost dates (through zip code) and reminds them in the appropriate timeframe. The user will select the seeds they are planning to grow for the season from the database, or add their own (if none are available), and the app will save and display when to start planting the seeds.

The working app can be found at:
[https://sown-app.herokuapp.com/](https://sown-app.herokuapp.com/)

The github repository for the frontend of this app can be found at:
[https://github.com/ljor/sown-app](https://github.com/ljor/sown-app)

## Technologies Used
This app was created using React.js and Flask

## Installation

Inside your python virtual environment, install with pip:

```
$ pip install -r requirements.txt
```

This will install any used dependencies needed to run the file. Note that you will need create a .env file in the root directory and create a FLASK_APP_SECRET variable. Set the variable to equal a long string of random characters -- (recommend key smashing or hiring a cat) -- for security purposes 

## User Stories

- As a gardener, I want to be able to keep track of when to sow the seeds I want to grow in my garden so that I can get them started on time
- As a planner, I want to know when to get my seeds started so I can plan the time to do that



## Wireframes


## Future Plans

- Improvements to the database.
- Improvements to the user interface and dashboard that includes:
    - Adding a calendar view, where users can get an overview of the dates they need to start sowing
    - A timeline overview table display
    - Search/filtering features
- Mobile reminder features, where a user can be notified when they can start planting the seeds of plants they want to grow in their garden
- Print options for users that want to print out their planned seeds calendar