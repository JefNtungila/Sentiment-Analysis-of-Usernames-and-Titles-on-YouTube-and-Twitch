# Master Thesis: Sentiment Analysis of Usernames and Titles on YouTube and Twitch

This Master Thesis investigates the influence of username and title sentiment on video performance in terms of viewership on Social Media Platforms YouTube and Twitch. Google Cloud Functions were deployed that utilised the Twitch API and YouTube API to fetch the data and pushed the data to GitHub. NLP techniques were used to gain an in depth understanding of the unstructured data.

Critical analysis of the literature and sentiment models results in actionable insights. Bayesian causal inference was performed as part of the analysis. These insights culminated in the creation of a search engine flask app which deployed a machine learning model using the Google App Engine on the Google Cloud Platform. This search engine takes a username or title in and returns a performance prediction based on sentiment. This technolog  y can be used for user centric recommendations based on the user mood, in addition to the current predictive application.

## Data
Data folder contains:
* Twitch Data - Data from top trending twitch streams, collected on an hourly basis from 28th of May till the 28th of July, 139 500 observations (file name = twitch_data.csv.zip)
* YouTube Data - Data from top trending YouTube videos worldwide using KWORBS as reference, collected from 28th of May till the 28th of July, 11 783 observations (file name = yotube_data.csv)
* Twitch Views -  Data of the unique observations of top trending streams, with percentage increase of viewership over lifetime on the trending tab feature, title and username sentiment anaysis (VADER and Emote Controlled), and sentiment analysis using Afinn extracting nominal realism from Twitch usernames.
* YouTube Views -  Data of the unique observations of top trending videos, with percentage increase of viewership over lifetime on the trending tab feature, title and username sentiment anaysis (VADER), and sentiment analysis using Afinn extracting nominal realism from YouTube usernames. 1454 observations (file name = youtube_views.csv)
## Code

Code folder contains:


