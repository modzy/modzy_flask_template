# Modzy Flask Template

![Modzy Logo](https://www.modzy.com/wp-content/uploads/2020/06/MODZY-RGB-POS.png)

<div align="center">

![GitHub contributors](https://img.shields.io/github/contributors/modzy/modzy_flask_template)
![GitHub last commit](https://img.shields.io/github/last-commit/modzy/modzy_flask_template)
![GitHub Release Date](https://img.shields.io/github/issues-raw/modzy/modzy_flask_template)

</div>


## Modzy Flask Quickstart tutorial

This code accompanies this [tutorial](https://docs.modzy.com/docs/modzy-in-a-flask-app-tutorial) for creating a simple web app to run a Modzy hosted model from scratch. In this tutorial we will walk through creating a simple web application with Python and the Flask framework backed by AI/ML Algorithms from Modzy.

- Download or clone this project from github: [https://github.com/modzy/modzy_flask_template/](https://github.com/modzy/modzy_flask_template/)
- In your terminal, navigate to the project directory
- Install Python
    - If you already have Python installed, you may skip this step.
    - If you don't have Python installed, install it now. You can download an installer from the [Python official website](http://python.org/download/) or on a Mac you can [install with Homebrew](https://docs.brew.sh/Homebrew-and-Python). 
    - To verify your Python installation open a terminal window and type `python3`.
- Install Flask 
    - If you already have Flask installed, you may skip this step.
    - verify that your terminal is in the Flask Template folder. 
    - enter `python3 -m venv venv` into the terminal and press enter. 
    - After the command completes type `source venv/bin/activate` and press enter.
    - now type `pip install flask` and hit enter. 
- Install Modzy-SDK
    - Paste `pip install modzy-sdk` to your terminal and press enter. 
    - Retrieve your Modzy API key (https://docs.modzy.com/docs/getting-started#key-download-your-api-key)
    - type `export API_KEY=yourAPI_key` and hit enter
    - now type `export FLASK_APP=demo_site.py`
    - Now start flask with the command `flask run`
- Open your new Web server!
    - Using a web browser of your choice, navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    - You should see this in your brower:
    ![](https://files.readme.io/eff62eb-Screen_Shot_2021-10-08_at_7.39.19_AM.png)
    - Type any text into the 'My Text' box and hit Analyze.
    - A few seconds later, the results of the sentiment analysis will be displayed!
    ![resultsscreen.png](https://files.readme.io/939d330-Screen_Shot_2021-10-08_at_7.39.42_AM.png)
    - You're done! Now click [Next Steps](http://127.0.0.1:5000/next) and have some fun!
    

## Table of contents

- [Flask Application code](app)
- [config.py](config.py): Flask configuration details
- [demo_site.py](demo_site.py): Flask startup 

## Contributing

We are happy to receive contributions from all of our users. Check out our [contributing file](https://github.com/modzy/modzy_flask_template/blob/master/CONTRIBUTING.md) to learn more.

## Code of conduct

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](https://github.com/modzy/modzy_flask_template/blob/master/CODE_OF_CONDUCT.md)
