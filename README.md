# NLP Drug Prescription Using Patient Reviews #


# Overview
## Problem Statement ##
Identifying, resolving, and preventing drug therapy problems are the unique contributions of the pharmaceutical care practitioner. However, depending on the pharmaceutical care practitioner to gather enough data for assessment may not be sufficient. This is where patient reviews of drugs helps to supplement the pharmaceutical care practitioner's data and help review drug performance. Such reviews may help drug companies determine effective forms of a pharmaceutical product, showing the ones to discotinue in production and the ones to focus on in production. An effective way to analyse reviews and make recommendations is the use of natural language processing and classification modeling for prediction. For most people with no access to doctors or with common ailments that requires no physician attention or prescription, they have to rely on word of mouth recommendation or historical use. However, newer effective drugs often replace older ones and therefore extracting and standardizing patient reviews will help to improve the predictive power of the reviews and usefulness factor. While this application is not intended for individual use for prescription, it can help pharmaceutical companies and pharmaceutical care practioners constantly update their treatment options.

## Summary ##
*We have developed a natural language processing (NLP)-based application for prescribing the right medication for a particular condition based on paient reviews of the medication and usefulness factor calculation.*

## Project Step-by-step process ##
**Apply NLP and standard medical terminologies to preprocess input features.**

**Package prescription Code in App**

**Deploy App in Development using Docker**

**Deploy App in Production using Google Cloud**

## Data ##
input data that contain patient reviews and medical conditions. 

## Natural Language Processing ## 
Natural Language processing was employed to preprocess the customer reviews in the dataset. After preprocessing and exploratory data analysis, it was discovered that the reviews did not have much effect on the ratings. Also, to ensure we prescribe the correct drugs for a particular condition, we feature engineered only the ratings and usefulness factor to determine the actual effectiveness of a particular medication. 

## Models ##
No modeling was employed, but we designed a recommendation based on the usefulness of the drugs to determine the best and worst drugs for a particular condition. It is hoped that the usefulness is contantly updated with current ratings to reflect the most effective drugs at any point in time.

## Application

## How to run ##
We describe below a tutorial for executing the prescription forecasting code using sample raw data.

Step 1 - to run the code
**python3 app.py**

Step 2 - To run the application
**streamlit run app.py**

Step 3 - Generate dependencies for building Docker - requirements.txt
**pipreqs  /"Working Directory"/**

Step 4 - Build and run Docker
**docker build**
**docker run -p:5000** 

Step 4 - Deploy App in Production Using Google Cloud
* List Projects
**gcloud__projects__list**
* To change to the project you created you can use
**gcloud__config__set__project__your_projectname**
* To check for the current project you use
**gcloud__config__get-value__project**
* To deploy our app we will be using
**gcloud__app__deploy**




