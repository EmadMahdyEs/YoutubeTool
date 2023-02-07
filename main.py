
import os.path
import pandas as pd
import argparse
import os
import re
from IPython.display import JSON
import arabic_reshaper
from bidi.algorithm import get_display

import update_video_functions
from upload_video import upload_video
import update_playlist_functions
from upload_playlist import upload_playlist
import google_auth

import logic_design_descriptin

Emad_channal_id='UC2VtseEd46wuDfmDXhfB9Ag'



from circuits12_description import circuit12, fundumental_contents
from microprocessors_playlist_names import micro_playlist_names
from microprocessors_playlist_names import micro_discription
def main():

   # youtube = google_auth.get_authenticated_service()
    #path = r"D:\تجهيز المستوي الخامس جامعة الطائف هندسة كهربية\دوائر كهربية ٢\ipad videos\circuits chapter 1 videos edited"

    for ch in fundumental_contents:
        print(fundumental_contents[ch][0] + ' | problems solutions | حلول مسائل')
        #update_playlist_functions.add_playlist(youtube, logic_design_descriptin.logic_design_lecs[n] + ' | شرح عربي',
        #                                      logic_design_descriptin.logic_design_discription, 'public')
if __name__ == '__main__':
    main()