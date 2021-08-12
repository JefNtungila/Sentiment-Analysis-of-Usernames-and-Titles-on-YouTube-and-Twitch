# -*- coding: utf-8 -*-
"""Sentiment Analysis of Usernames and Titles on YouTube and Twitch_DATA_WRANGLING.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mIwk5d0UgcHa2NUvXkNEXOksoHfcXmtA

# Sentiment Analysis of Usernames and Titles on YouTube and Twitch

## Data Preperation, Wrangling and Cleaning

This notebook concatenates all the files that were pushed on a scheduled basis from the social media platforms to GitHub.

The data is then filtered from the 28th of May 2021 till the 28th of July 2021. The textual data is processed, cleaned and made ready for visualisatioin and sentiment analysis

## Setting up environments
"""

!python -m spacy download en_core_web_lg

!pip install PyGithub

pip install scipy

"""## Ingesting Data """

!git clone https://github.com/JefNtungila/master_thesis.git

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# !cp master_thesis/* /content/master_thesis/

# import OS module
import os
import pandas as pd

pd.options.display.max_colwidth = 100

# Get the list of all files and directories
#saved in the master thesis directory
path = '/content/master_thesis/'
dir_list = os.listdir(path)
 
#reading the files in as csv, appending them to a list, concatinating them as a whole 
twitch_files = pd.concat([pd.read_csv(f'{path}{file_}') for file_ in dir_list if 'twitch' in file_])
youtube_files = pd.concat([pd.read_csv(f'{path}{file_}') for file_ in dir_list if 'youtube' in file_])

print(len(twitch_files))
print(len(youtube_files))

"""## Data Wrangling and Cleaning"""

# Commented out IPython magic to ensure Python compatibility.
# %time
from spacy.tokenizer import Tokenizer
import spacy
import html
from html.parser import HTMLParser
import re

#loading spacy encore model - need pip install it and restart runtime
nlp = spacy.load('en_core_web_lg')
tokenizer = Tokenizer(nlp.vocab)

def token_text(doc):
  '''
  formatting as non html for visualisation
  keep only characters 
  tokenise sentence into words if those words are not punctuation, pronouns or stop words 
  '''
  doc = html.parser.unescape(doc) #remove html
  doc = re.sub(r'[^a-zA-Z ^0-9]', '', doc) #keep alphanumerical characters
  doc = re.sub('[0-9]+', '', doc) #remove numerical characters
  doc = doc.lower() #convert all strings to lowercase
  tokens = [token.text for token in tokenizer(doc)  if (token.is_punct == False) and (token.is_stop == False)]
  tokens = [''.join(x.split()) for x in tokens if x] #remove multiple random number leading spaces from each token in a doc
  tokens = [token for token in tokens if token != ''] #remove empty string from leading edges
  return tokens

from datetime import datetime, date, time, timedelta
import datetime

def wrangle(X):

  ''' wrangle function sort values by api call time and index 
  formats the api call time in usuable features
  filtering data from 28th of MAY when youtube data was ingested cleanly
  keeping 2 months of data for study
  creates tokenised version of username
  creates tokenis version of titles'''

  X = X.sort_values(['api_call_time', 'Unnamed: 0'])
  X['date_api_call_time'] = pd.to_datetime(X['api_call_time']).dt.date
  X['hour_api_call_time']  = pd.to_datetime(X['api_call_time']).dt.hour
  X = X[X['date_api_call_time'] >= datetime.date(2021, 5, 28)]
  X = X[X['date_api_call_time'] <= datetime.date(2021, 7, 28)]
  X.rename(columns={'Unnamed: 0': 'reference_index'}, inplace=True)
  X = X.reset_index(drop=True)
  X['tokenised_title'] = X[X.columns[X.columns.to_series().str.contains('title')]].iloc[:, 0].apply(lambda x : token_text(str(x)))

  #### add in date filter from when data is clean enough

  return X

def token_text_with_stopwords(doc):


  '''
  tokenising for NLP purposes
  formatting as non html for visualisation
  keep only characters 
  tokenise sentence into words if those words are not punctuation, pronouns or stop words 
  remove potential leading spaces
  '''

  doc = html.parser.unescape(doc) #remove html
  doc = re.sub(r'[^a-zA-Z ^0-9]', '', doc) #keep alphanumerical characters
  doc = re.sub('[0-9]+', '', doc) #remove numerical characters
  doc = doc.lower() #convert all strings to lowercase
  tokens = [token.text for token in tokenizer(doc)  if (token.is_punct == False) ]
  tokens = [''.join(x.split()) for x in tokens if x] #remove multiple random number leading spaces from each token in a doc
  tokens = [token for token in tokens if token != ''] #remove empty string from leading edges
  
  return tokens

twitch_data = wrangle(twitch_files)
youtube_data = wrangle(youtube_files)

#tokenising titles and keeping stopwords
twitch_data['tokenised_titles_with_stopwords'] = twitch_data['title'].apply(lambda x: token_text_with_stopwords(str(x)))
youtube_data['tokenised_titles_with_stopwords'] = youtube_data['video_title'].apply(lambda x : token_text_with_stopwords(str(x)))

print(twitch_data.shape)
print(youtube_data.shape)

"""## Adding Twitch Data Genres"""

vgsales = pd.read_csv('https://raw.githubusercontent.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/main/data/vgsales.csv')

#manual labelling of missing top 30 games, often published after 2018
#complementart to classification by VGS which labelled more than 30K titles

game_genre = pd.DataFrame({'game_name': ['Call of Duty: Warzone', 'VALORANT',
       'Hearthstone', 'Genshin Impact', 'FIFA 21', 'Escape from Tarkov',
       'Teamfight Tactics', "Tom Clancy's Rainbow Six Siege", 'SMITE',
       'Resident Evil Village'],
       'game_genre': ['Shooter','Shooter','Misc','Misc','Sports','Shooter','Strategy', 'Shooter', 'Misc', 'Misc']})

#merging with vgsales
twitch_data = twitch_data.merge(vgsales[['Name', 'Genre']].drop_duplicates(subset= ['Name']), how = 'left', left_on='game_name', right_on='Name')
#merging with modern games dataframe (game_genre)
twitch_data = twitch_data.merge(game_genre, how = 'left', left_on = ['game_name'], right_on = ['game_name'])
twitch_data['Genre'] = twitch_data['Genre'].fillna(twitch_data['game_genre'])
twitch_data['Genre'] = twitch_data['Genre'].fillna('Other')
twitch_data = twitch_data.rename(columns = {'Genre': 'genre'})
twitch_data = twitch_data.drop(columns = ['game_genre', 'Name'])

twitch_data.columns.values

#producing summary statistics for twitch data
#viewer count feature is right skewed min/ max? boxplot???
#bob ross is most occuring title

twitch_data[['reference_index', 'user_name', 'game_name', 'title',
       'viewer_count', 'started_at', 'api_call_time',
       'date_api_call_time', 'hour_api_call_time',  'genre']].describe(include = 'all').T

"""## Adding YouTube Genres"""

vid_genre = pd.read_csv('https://raw.githubusercontent.com/JefNtungila/Sentiment-Analysis-of-Usernames-and-Titles-on-YouTube-and-Twitch/main/data/Trending_CrowdSourced_Classification.csv', 
                        encoding = 'latin1')
#replacing conventionally viral youtubers with the general youtuber
vid_genre['classification'] = vid_genre['classification'].replace({'CV':'YT'})

#renaming columns to actual words from accronym
vid_genre['classification'] = vid_genre['classification'].replace({'YT': 'Youtuber',
                                                                    'CO': 'Commercial',
                                                                    'TR':'Trailer',
                                                                    'MU': 'Music',
                                                                    'TM': 'Traditional Media'})
vid_genre = vid_genre[vid_genre['classification'].notna()]
vid_genre = vid_genre.rename(columns={'classification':'genre'})

#merging with the crowdsourced video genre
youtube_data = youtube_data.merge(vid_genre[['channel', 'genre']], how = 'left', left_on='username', right_on='channel')
youtube_data = youtube_data.drop(columns=['channel'])

from sklearn.feature_extraction.text import CountVectorizer


#creating word scarse count vectorised matric from youtube titles
countvec = CountVectorizer()
df_one_hot_encoded = pd.DataFrame(countvec.fit_transform(youtube_data['video_title']).toarray(), 
                                  index=youtube_data['video_title'], columns=countvec.get_feature_names())

#adding the target column to the countvectorised matrix

df_processed = pd.concat([df_one_hot_encoded.reset_index(drop=True),  
                          youtube_data['genre'].reset_index(drop = True)], axis = 1)

import numpy as np
from sklearn.model_selection import train_test_split

#selecting labelled data for training and testing

X = df_processed[df_processed['genre'].notna()].drop(columns= ['genre'])
y = df_processed[df_processed['genre'].notna()]['genre']

#splitting in 80, 20
X_train, X_val, y_train, y_val = train_test_split( X, y, train_size = 0.8, stratify=y, random_state=42)

print(X_train.shape, y_train.shape, X_val.shape, y_val.shape)

pip install xgboost

from xgboost import XGBClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer



eval_set = [(X_train, y_train), (X_val, y_val)]


# Fit on train, score on val, predict on test, 100 trees, stop after no improvemnt for 30 epochs
model = XGBClassifier(n_estimators = 100, n_jobs = -1)
model.fit(X_train, y_train, eval_set = eval_set , early_stopping_rounds = 30)

y_pred = model.predict(X_val) #actually storing the predictions it would have made for X_val
print('Validation Accuracy', model.score(X_val, y_val))

#predicting genres for those that don't have a genre
pred = model.predict(df_processed[df_processed['genre'].isna()].drop(columns= ['genre']))
index_no_genre = youtube_data[youtube_data['genre'].isna()].reset_index()['index'].tolist()

#creating dataframe with the predicted genres and the row indeces on which they should be merged
pred_df = pd.DataFrame({'label': pred,
                        'index': index_no_genre})

pred_df['label'].value_counts()

#merge original dataframe with new labels
youtube_data = pd.merge(youtube_data.reset_index(), pred_df, how = 'left', on='index')
youtube_data['genre'] = youtube_data['genre'].fillna(youtube_data['label'])
#deleting columns that were used as reference for the merge
youtube_data = youtube_data.drop(columns=['index', 'label'])

youtube_data[['reference_index', 'username', 'video_title', 'publish_time',
       'view_count', 'comment_count', 'like_count', 'dislike count',
       'api_call_time', 'date_api_call_time', 'hour_api_call_time', 'genre']].describe(include = 'all').T

"""## Username Wrangling"""

!pip install nltk

import nltk
from nltk import corpus

english_words = nltk.download('words')
english_vocab = set(word.lower() for word in nltk.corpus.words.words())

def word_finder(name):

  
  #not random , emperic testing gives good result 

  name = name.lower()

  #finding intersection with words in the dictionary
  all_possible_words = {name[i:j + i] for j in range(2, len(name)) for i in range(len(name)- j + 1)}
  all_words = english_vocab.intersection(all_possible_words)
  all_words = list(set(list(all_words)))
  if all_words == []:
    all_words = float('NaN')
  else:
    #transforming list of words into string of words
    all_words = ' '.join(word for word in all_words)
    #removing stopwords
    all_words = [token.text for token in tokenizer(all_words)  if (token.is_stop == False)] 

  return all_words

youtube_data.columns

twitch_data['words_in_names'] = twitch_data['user_name'].apply(lambda x : word_finder(x))
youtube_data['words_in_names'] = youtube_data['username'].apply(lambda x : word_finder(x))

"""## Pushing data to drive and GitHub"""

from  github import Github

twitch_data.to_csv('twitch_data.csv')
!cp twitch_data.csv 'drive/My Drive/'

youtube_data.to_csv('youtube_data.csv')
!cp youtube_data.csv 'drive/My Drive/'

g = Github('github_ley')
repo = g.get_repo('github_repo)
#parameters are filename, description, content
#cannot update because file is to big so have to delete and update

repo.create_file('twitch_data.csv', 'twitch hourly top 50 streams', str(twitch_data.to_csv()))
repo.create_file('youtube_data.csv', 'youtube top 100 streams worldwide taken every 6 hours', str(youtube_data.to_csv()))