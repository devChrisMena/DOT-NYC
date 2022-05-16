# DOT-NYC

## Table of Content

1. [Overview](#Overview)
2. [Product Spec](#Product-Spec)
3. [Schema](#Schema)
4. [Wireframes](#Wireframes)
5. [Manual](#Manual)
6. [Documentation](#Documentation)

## Overview

### Description

Create an application that would capture the sentiment of customers automatically and efficiently, thus reducing the resources needed in order to complete this task.
Automatically fetch text from DOT’s Twitter, Instagram, and Facebook. Classify the opinion(positive, negative and neutral) of the text using NLP techniques

### App Evaluation

- **Category:** Social Networking / Neural Network / Language
- **Computer:** This app would be primarily developed for Window devices. Functionality could be limited to Window devices.
- **Story:** Automate feedback gathering from a social group. Users can execute scripts to optain infomartion from their particular following. Optain statistical data to further understand their sentiment. Clasify sentences on wether they are positve, negative or neutral.
- **Market:** Limited to the social media team at the NYC DOT.

## Product Spec

### 1. Crawler Scripts

- [x] Script naviagtes to specified account or page.
- [x] Script can fetch comments from the specified account or page.
- [x] Script can fetch data within a given parameter.

### 2. Neural Network Model

- [x] Model trained.
- [x] Model can clasify sentences.
- [x] Model can rate sentences.

### 3. Screen Archetypes

- To be determine

### 4. Navigation

**Flow Navigation**

- Set parameter --> Set functional parameter for script.
- Specific scripts -- > Specified which scrawler scripts to run.
- Output --> Text and numerial data

## Wireframes

![WorkFlow Diagram](/Img/Workflow.png)
![Work Breakdown Structure](/Img/Work_breakdown_structure.png)

## Schema

### Twitter

| Property      | Type     | Description                                                                                                                                            |
|---------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| name          | String   | user shown name                                                                                                                                        |
| username      | String   | unique username for user                                                                                                                               |
| timestamp     | String   | time when posted                                                                                                                                       |
| comment       | String   | text containing user's response                                                                                                                        |

### Instagram

| Property      | Type     | Description                                                                                                                                            |
|---------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| username      | String   | unique username for user                                                                                                                               |
| timestamp     | String   | time when posted                                                                                                                                       |
| comment       | String   | text containing user's response                                                                                                                        |



## Manual

### 1. GUI

- To be written

### 2. Scripts

 **Twitter** script takes four parameter:

- Login Account Name: Name of dummy account to use.
- Login Account Password: Password for dummy account to use.
- Target Account: Account or Hashtag to search.
- Range Date: Given a number of days, only fetch data within current's date and the current's date minus the given number of days.

 **Instagram** script takes four parameter:

- Login Account Name: Name of dummy account to use.
- Login Account Password: Password for dummy account to use.
- Target Account: Account or Hashtag to search.
- Range Date: Given a number of days, only fetch data within current's date and the current's date minus the given number of days.

### 3. Outputs

- To be written

### 4. Installation

In order to properly use the software we must follow a series of steps in order for everything to work as intended. Be advice that the program is cross-compatible for all major OS in the market. However, this installation process is specifically for Windows devices.

1. Download and install Python. To download [Python](https://www.python.org/downloads/) from the official site. Please select the lastest version avaiable.
    - Be advice that your machine must meet the minimun specification to run Python

2. Download and Install the [Chrome](https://www.google.com/chrome/downloads/) web browser.
    - If alredy install, pleaser update to the lastest build. To do so follow these steps:
        - Click the 3 dots on the top right corner.
        - Go to **Help** Section.
        - Click **About Google Chrome**.
        - Select option to update.
    - Find the version of Chrome. To find the version of chrome please follow the steps above.

3. Download and Install Visucal Studio Code. To download [Visual Studio Code](https://code.visualstudio.com/download) click the previous link.

4. Download the Webdriver from Chrome. To download the Webdriver for Chrome:
    - Find the version of Google Chrome. Please follow step 2 to find Chrome version.
    - Download the version of Chrome [Webdriver](https://chromedriver.chromium.org/downloads) that corresponds to the version of Chrome installed.
    - Save file on a separate directory.

5. Add Webdriver to the **System Variables**.
    - Search for **Edit System Variable** on Windows.
    - Click on ........
    - Add the directory on which the **Webdriver** is located to the system PATH.

6. Download Software Package
    - Clone Repo 
    - Or Download package files by pressing **Code** then **Download as Zip**

7. Setup Packages
    - Open **Visual Studio Code** and open the project directory through it.
    - Run the `Setup.py` to  install needed packages.
    - Run `Download.py` to Download supplemary files needed to run software
        - It is possible for `Download.py` to failed to run. Fix it by switching python interpreter or closing and reopening VS Code.


## Documentation

### 1. Technology

This program was writen to be versitile across any platform that supports Python and Web browser. Our goal is to create a program that can rely on as little outside packages as possible while remanining future proof and innovative. We decided to use the following technologies for this project:

- 

### 2. Functions