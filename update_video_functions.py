



Emad_channal_id='UC2VtseEd46wuDfmDXhfB9Ag'
from IPython.display import JSON

#!/usr/bin/python


import argparse
import os
import re



def update_video_description(youtube,id,description):
    # Call the API's videos.list method to retrieve the video resource.
    videos_list_response = youtube.videos().list(
        id=id,
        part='snippet'
    ).execute()
    videos_list_snippet = videos_list_response['items'][0]['snippet']
    videos_list_snippet['description'] = description

    videos_update_response = youtube.videos().update(
        part='snippet',
        body=dict(
            snippet=videos_list_snippet,
            id=id
        )).execute()

def update_video_title(youtube,id,title):
    # Call the API's videos.list method to retrieve the video resource.
    videos_list_response = youtube.videos().list(
        id=id,
        part='snippet'
    ).execute()
    videos_list_snippet = videos_list_response['items'][0]['snippet']
    videos_list_snippet['title'] = title

    videos_update_response = youtube.videos().update(
        part='snippet',
        body=dict(
            snippet=videos_list_snippet,
            id=id
        )).execute()

def update_video_status(youtube,id,status):
    # Call the API's videos.list method to retrieve the video resource.
    videos_list_response = youtube.videos().list(
        id=id,
        part='snippet'
    ).execute()
    videos_list_snippet = videos_list_response['items'][0]['snippet']

    videos_update_response = youtube.videos().update(
        part='snippet',
        body=dict(
            snippet=videos_list_snippet,
            id=id,
            status=dict(
                privacyStatus='private'
            )
        )

    ).execute()
