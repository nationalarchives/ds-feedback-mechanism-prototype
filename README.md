# Feedback mechanism prototype

## Development approach

The Flask application has been developed following [The National Archives front end development guide](https://github.com/nationalarchives/front-end-development-guide) and process for the [practical application of progressive enhancement](https://github.com/nationalarchives/front-end-development-guide)

## Local development

### What this repository provides

Included in this repository is: 

* Webpack for transpiling JavaScript
* Sass for compiling CSS

### Development machine configuration

Use these steps to get up and running

1. Ensure you have _at least_ Python 3.7 and pip installed
2. Clone this repository
3. Create a virtual environment with `python3 -m venv venv`
4. From the root directory run `source venv/bin/activate` 
5. Install dependencies with `pip install -r requirements.txt`
6. Start the application with `flask run`
7. See the command line for the URL to visit
8. When finished run `deactivate` from the virtual environment

For front end assets:

In a _new terminal_ run these commands:

* `npm install -g sass` will install Sass as a global dependency
* `npm start` will kick off a Sass watch task

_If you are working on JavaScript_, you should also run (in another new terminal):

* `npm run start-scripts` will kick off a Webpack watch task