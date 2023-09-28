# DOT-NYC

## Table of Contents

1. [Overview](#overview)
2. [Usage](#usage)
3. [Product Specifications](#product-specifications)
4. [Schema](#schema)
5. [Wireframes](#wireframes)
6. [Manual](#manual)
7. [Documentation](#documentation)

## Overview

### Description

Create an application that captures customer sentiment automatically and efficiently, reducing the resources needed for this task. Automatically fetch text from DOT’s Twitter and Instagram and classify the sentiment (positive, negative, and neutral) of the text using NLP techniques.

### App Evaluation

- **Category:** Social Networking / Neural Network / Language
- **Compatibility:** This app is primarily developed for Windows devices, and its functionality may be limited to such devices.
- **Story:** Automate feedback gathering from a social group. Users can execute scripts to obtain information from their specific followers, gather statistical data to understand sentiment, and classify sentences as positive, negative, or neutral.
- **Market:** Targeted at the social media team at the NYC DOT.

## Usage

Provide login information for Twitter or Instagram, then run one of the scripts to fetch data for the target account.

For more details, check the [Manual](#manual).

## Product Specifications

### 1. Crawler Scripts

- [x] Script navigates to the specified account or page.
- [x] Script can fetch comments from the specified account or page.
- [x] Script can fetch data within given parameters.

### 2. Neural Network Model

- [x] Model is trained.
- [x] Model can classify sentences.
- [x] Model can rate sentences.

### 3. Screen Archetypes

- Creation: Select one of the scripts from a simple GUI interface to fetch and save data from your desired platform.

### 4. Navigation

**Flow Navigation**

- Set parameters: Set functional parameters for the script.
- Specific scripts: Specify which crawler scripts to run.
- Output: Text and numerical data.

## Wireframes

![Workflow Diagram](/Img/Workflow.png)
![Work Breakdown Structure](/Img/Work_breakdown_structure.png)

## Schema

### Twitter

| Property  | Type   | Description                  |
|-----------|--------|------------------------------|
| name      | String | User's displayed name        |
| username  | String | Unique username for the user |
| timestamp | String | Time when posted             |
| comment   | String | Text containing user's response |

### Instagram

| Property  | Type   | Description                  |
|-----------|--------|------------------------------|
| username  | String | Unique username for the user |
| timestamp | String | Time when posted             |
| comment   | String | Text containing user's response |

## Manual

### 1. GUI

The **GUI** is designed for simple use. All functional parameters are preset and ready to run. The GUI has the following components:

- Text Input: Accepts a number representing days. It calculates a date range consisting of the current date minus the given number of days.
- Twitter Button: Runs the Twitter script to fetch data.
- Instagram Button: Runs the Instagram script to fetch data.
- Analyze Twitter: Runs the script model to evaluate a CSV file corresponding to the data fetched from the Twitter script.
- Analyze Instagram: Runs the script model to evaluate a CSV file corresponding to the data fetched from the Instagram script.

Here's a GIF showing how to get the version of Google Chrome:

![Chrome Version](/Img/GVersion.gif)

### 2. Scripts

The **Twitter** script takes four parameters:

- Login Account Name: Name of the dummy account to use.
- Login Account Password: Password for the dummy account.
- Target Account: Account or hashtag to search.
- Range Date: Given a number of days, fetch data within the current date and the current date minus the given number of days.

The **Instagram** script also takes four parameters:

- Login Account Name: Name of the dummy account to use.
- Login Account Password: Password for the dummy account.
- Target Account: Account or hashtag to search.
- Range Date: Given a number of days, fetch data within the current date and the current date minus the given number of days.

### 3. Outputs

Each script outputs two **CSV** files corresponding to the platform from which data was fetched.

- One **CSV** file contains the data fetched from the social media platform, including:
  - Username
  - User's name (optional, for Twitter)
  - Timestamp
  - Comment
- The second **CSV** file contains data processed by the Deep Learning Model, including:
  - Comment fetched
  - Rating for comment
- Optionally, the user can decide whether to save infographics such as bar plots or pie charts when running the scripts.

### 4. Installation

To properly use the software, follow these steps. Note that the program is cross-compatible with all major operating systems, but the installation process is specific to Windows devices:

1. Download and install Python from the official website [Python](https://www.python.org/downloads/), selecting the latest version available.

2. Download and install the [Chrome](https://www.google.com/chrome/downloads/) web browser. If already installed, update it to the latest version by clicking the three dots in the top-right corner, going to the **Help** section, clicking **About Google Chrome**, and selecting the update option.

3. Download and install Visual Studio Code from [here](https://code.visualstudio.com/download).

4. Download the Webdriver for Chrome, which corresponds to your Chrome version, from [Chrome Webdriver](https://chromedriver.chromium.org/downloads) and save it in a separate directory.

5. Add the Webdriver directory to the **System Variables**:
   - Search for **Edit System Variable** on Windows.
   - Click on **Environment Variables**.
   - Select **Path** under **System variables** and click **Edit**.
   - Add the directory where the **Webdriver** is located to the system PATH.

6. Download the software package:
   - Clone the repo or download package files by clicking **Code** then **Download ZIP**.

7. Set up packages:
   - Open **Visual Studio Code**, open the project directory within it.
   - Run `Setup.py` to install necessary packages.
   - Run `Download.py` to download supplementary files needed to run the software. If `Download.py` fails, try switching the Python interpreter or closing and reopening VS Code.

Here's a GIF showing how to add the Webdriver directory to the system PATH:

![Adding Webdriver to System Path](/Img/Path.gif)

## Documentation

### 1. Technology

This program is versatile and can run on any platform that supports Python and a web browser. It aims to minimize external dependencies while remaining future-proof and innovative. The technologies used in this project include:

1. [Selenium](https://www.selenium.dev/): A Python package for automating web browsers. Selenium is used to navigate websites and extract content for further processing.

2. [Tensorflow](https://www.tensorflow.org/): An open-source machine learning platform that allows researchers to advance machine learning and developers to build ML-powered applications.

3. [Pandas](https://pandas.pydata.org/): A fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool, built on top of Python.

4. [Matplotlib](https://matplotlib.org/): A comprehensive library for creating static, animated, and interactive visualizations in Python.

### 2. Functions

#### Twitter & Instagram

- `setDay(value)`: Sets the date range based on a given value in days. The date range consists of the current day minus the specified number of days.

- `getTweetData(card)`: Takes a WebElement corresponding to Twitter post information and returns a tuple with the desired information.

- `loadElement(by, path, browser)`: Loads a page with the given By (a supported locator), Path (path to the desired element), and Browser. Returns a WebElement when loaded successfully or an error if not.

- `loadElements(by, path, browser)`: Loads all elements on a page within a given time frame using the provided By and Path. Returns a list of WebElements when loaded successfully or an error if not.

- `formatTime(data_time)`: Takes a string representing a datetime and formats it as MM/DD/YYYY, returning the formatted string.

- `login(user_name, user_pass, driver)`: Logs into a Twitter account using the provided username, password, and driver (browser).

- `searchFor(target, driver)`: Searches for the target account or hashtag on Twitter using the provided driver (browser) and returns a WebElement corresponding to the target.

- `loadMoreComments(texts, browser)`: Exclusively for Instagram, this function takes the comment section WebElement of a post and attempts to load all comments replying to the original post. It returns a list of all loaded comment WebElements.
