import os

import upload_video
from upload_video import upload_video

def upload_playlist(youtube,playlist_path):
    videos_list = os.listdir(playlist_path)
    for video in videos_list:
        video_path=playlist_path + '\\' + video
        #print(video_path)
        upload_video(youtube, video_path)
