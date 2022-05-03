# DOT-NYC

## Table of Content

1. [Overview](#Overview)
2. [Product Spec](#Product-Spec)
3. [Schema](#Schema)
4. [Wireframes](#Wireframes)
5. [Manual](#Manual)

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

* Set parameter --> Set functional parameter for script.
* Specific scripts -- > Specified which scrawler scripts to run.
* Output --> Text and numerial data

## Wireframe

![WorkFlow Diagram](/Img/Workflow.png)
![Work Breakdown Structure](/Img/Work_breakdown_structure.png)


## Manual

### 1. GUI

 * To be written

### 2. Scripts

 **Twitter** script takes four parameter:

- Login Account Name: Name of dummy account to use
- Login Account Password: Password for dummy account to use
- Target Account: Account or Hashtag to search.
- Range Date: Given a number of days, only fetch data within current's date and the current's date minus the givem number of days.

 **Instagram** script takes four parameter:

- Login Account Name: Name of dummy account to use
- Login Account Password: Password for dummy account to use
- Target Account: Account or Hashtag to search.
- Range Date: Given a number of days, only fetch data within current's date and the current's date minus the givem number of days.

### 3. Outputs

* To be written