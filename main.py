

import arabic_reshaper
from bidi.algorithm import get_display

import update_video_functions
from upload_video import upload_video
import update_playlist_functions

import os.path
from googleapiclient.discovery import build


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


import pandas as pd
client_id="233931312133-tnolfdh6j0afc1ci92kagqaiiq430qa2.apps.googleusercontent.com"
client_secret="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"
Emad_channal_id='UC2VtseEd46wuDfmDXhfB9Ag'
from IPython.display import JSON

#!/usr/bin/python

# Retrieve the authenticated user's uploaded videos.
# Sample usage:
# python my_uploads.py

import argparse
import os
import re
import pandas

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow



CLIENT_SECRETS_FILE = 'client_secret.json'

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
#SCOPES = ['https://www.googleapis.com/auth/youtube']

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Authorize the request and store authorization credentials.
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)



disc='''الكورس كامل  و ملفات الشرح
 https://si-manual.com

للتواصل 
+201100184676


الشرح من كتاب 
Fundamentals of Electric Circuits (5th Edition) by Alexander Sadiku

محتوي الشابتر:
9.1 Introduction
9.2 Sinusoids
9.3 Phasors
9.4 Phasor Relationships for Circuit Elements
9.5 Impedance and Admittance
9.6 †Kirchhoff’s Laws in the Frequency Domain
9.7 Impedance Combinations
solved Examples 
Solved problems

محتوي الكورس :
CHAPTER 9 Sinusoids and Phasors
CHAPTER 10 Sinusoidal Steady-State Analysis
CHAPTER 11 AC Power Analysis
CHAPTER 12 Three-Phase Circuits
CHAPTER 13 Magnetically Coupled Circuits'''

def main():

    youtube = get_authenticated_service()


    ##########################################################

  

    #video_file=r"C:\Users\El-Wattaneya\Midterm_G1_solution_Q5.MP4"

    #upload_video(youtube, video_file)
    title='new test playlist'
    description='si-manual.com'
    privacy='public'
    #update_playlist_functions.add_playlist(youtube, title, description,privacy)
    playlist_id='PLSRx5jmWD9u21h9hAAeEYxGa2vZUPHx4k'
    #videos_id_list= update_playlist_functions.get_playlist_videos_id(youtube, playlist_id)
    #print(videos_id_list)
    description = 'si-manual.com'

    #print(disc)
    #update_playlist_functions.update_playlist_videos_description(youtube, playlist_id, disc)
    video_id='RHDCBdhJ9_4'
    update_playlist_functions.add_video_to_playlist(youtube, playlist_id, video_id)
if __name__ == '__main__':
    main()