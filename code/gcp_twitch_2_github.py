# -*- coding: utf-8 -*-
"""gcp_twitch_2_github.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SiwVyCON1E9ijA4iHP1xRWd6MYsT3uhT
"""

import base64
import twitch
import pandas as pd
from datetime import datetime
from github import Github


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.

        This function pushes data from Twitch to GitHub
    """

    #accesing data from twitch

    time = str(datetime.now().isoformat())

    #ingest every 6th minute of the hour
    if time[14:16] == '06':
      
      client = twitch.TwitchHelix(client_id='client_id_here', client_secret='client_secret_here', 
                              scopes=[twitch.constants.OAUTH_SCOPE_ANALYTICS_READ_EXTENSIONS])
      client.get_oauth()
      streams = client.get_streams(page_size=100, languages= ['en'])
      print(len(streams))


      #ensures that the data is not cut
      pd.options.display.max_colwidth = 10000

      


      df_holder = []
      # formatting list of stream details into dataframe 
      for df in streams:
        try:
          df = pd.DataFrame(df)
          df['time'] = time
          df_holder.append(df)
        except:
          continue

      # concatenating all the dataframes together 
      df = pd.concat([df for df in df_holder])
      df = df[['user_name', 'game_name', 'title', 'viewer_count', 'started_at']]
      df['api_call_time'] = time
      df = df.drop_duplicates()
      df = df.reset_index(drop = True)
      df = df[:100]

      #using unique api call time to name file
      file_name = f'twitch_{time}.csv'
      g = Github('github_key_here')
      repo = g.get_repo('github_repo_here')
      #parameters are filename, descritption, content
      repo.create_file(file_name, file_name, str(df.to_csv()))

      pubsub_message = base64.b64decode(event['data']).decode('utf-8')
      print(pubsub_message)