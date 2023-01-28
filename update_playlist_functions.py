#!/usr/bin/python


import update_video_functions
import argparse
import os
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

def add_playlist(youtube, title,description,privacy):
    body = dict(
        snippet=dict(
            title=title,
            description=description
        ),
        status=dict(
            privacyStatus=privacy
        )
    )

    playlists_insert_response = youtube.playlists().insert(
        part='snippet,status',
        body=body
    ).execute()

    print('New playlist ID: %s' % playlists_insert_response['id'])

def retrieve_playlist(youtube,playlist_id):
    response=youtube.playlistItems().list(
        part='snippet,status',
        playlistId=playlist_id,
        maxResults=50
    ).execute()
    if 1 > response.get('pageInfo').get('totalResults'):
        return
    else:
        items = response.get('items')
        nextPageToken=response.get('nextPageToken')
        while nextPageToken:
            response_next_page = youtube.playlistItems().list(
                part='snippet,status',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=nextPageToken
            )
            print(nextPageToken)
            items.extends(response_next_page.get('items'))
            nextPageToken = response.get('nextPageToken')
        return items
def get_playlist_videos_id(youtube,playlist_id):
    videos=retrieve_playlist(youtube,playlist_id)
    videos_id_list = []
    for video in videos:
        videos_id_list.append(video['snippet']['resourceId']['videoId'])

    return videos_id_list

def update_playlist_videos_description(youtube,playlist_id,description):

    videos_id_list=get_playlist_videos_id(youtube,playlist_id)
    for video_id in videos_id_list:
        update_video_functions.update_video_description(youtube, video_id, description)


def add_video_to_playlist(youtube, playlistID,videoID):
    add_video_request = youtube.playlistItems().insert(
        part="snippet",
        body={
            'snippet': {
                'playlistId': playlistID,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': videoID
                }
                # 'position': 0
            }
        }
    ).execute()



