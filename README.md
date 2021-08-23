# Master Thesis: Sentiment Analysis of Usernames and Titles on YouTube and Twitch

This Master Thesis investigates the influence of username and title sentiment on video performance in terms of viewership on Social Media Platforms YouTube and Twitch. Google Cloud Functions were deployed that utilised the Twitch API and YouTube API to fetch the data and pushed the data to GitHub. NLP techniques were used to gain an in depth understanding of the unstructured data.

Critical analysis of the literature and sentiment models results in interesting insights. These insights culminated in the creation of a search engine flutter app which deployed a machine learning model using Google Cloud Functions on the Google Cloud Platform. This search engine takes a username or title in and returns the sentiment classification. This technology can be used for user centric recommendations based on the user mood, in addition to the current predictive application.

## Data
Data folder contains:
* [Twitch Data](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/data/twitch_data.csv.zip) - Data from top trending twitch streams, collected on an hourly basis from 28th of May till the 28th of July, 139 500 observations (file name = twitch_data.csv.zip)
* [YouTube Data](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/data/youtube_data.csv) - Data from top trending YouTube videos worldwide using KWORBS as reference, collected from 28th of May till the 28th of July, 11 783 observations (file name = yotube_data.csv)
* [Twitch Views](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/data/twitch_views.csv) -  Data of the unique observations of top trending streams, with percentage increase of viewership over lifetime on the trending tab feature, title and username sentiment anaysis (VADER and Emote Controlled), and sentiment analysis using Afinn extracting nominal realism from Twitch usernames. 23 578 observations (file name = twitch_views.csv)
* [YouTube Views](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/data/youtube_views.csv) -  Data of the unique observations of top trending videos, with percentage increase of viewership over lifetime on the trending tab feature, title and username sentiment anaysis (VADER), and sentiment analysis using Afinn extracting nominal realism from YouTube usernames. 1454 observations (file name = youtube_views.csv)
* [Emote Controlled](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/data/emote_average) - Data from Kobs et al mapping Twitch emotes to valence ratings
* [VGS Sales](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/data/vgsales.csv) - Video Games Sales Data from vgchartz.com via Kaggle
* [YouTube Crowdsourced Classification](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/data/Trending_CrowdSourced_Classification.csv) - Data by the YouTuber CoffeeBreak
## Code

Code folder contains:
*  [Google Cloud Function Python file: YouTube](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/code/gcp_youtube_2_github.py) - ingests data from YouTube and pushes it to GitHub
* [Google Cloud Function Python file: Twitch ](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/code/gcp_twitch_2_github.py) - that ingests data from Twitch and pushes it to GitHub
* [YouTube and Twitch Data Wrangling NoteBook ](https://github.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/blob/main/code/Sentiment_Analysis_of_Usernames_and_Titles_on_YouTube_and_Twitch_DATA_WRANGLING.ipynb) -Jupyter Notebook that wrangles all the ingested YouTube and Twitch files and adds genre


