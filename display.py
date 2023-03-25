import os
import glob
from IPython.display import HTML
from base64 import b64encode
import streamlit as st

def get_latest_file(path):
  dir_list = glob.glob(path)
  dir_list.sort(key=lambda x: os.path.getmtime(x))
  return dir_list[-1]
 
Video = get_latest_file(os.path.join('trial', 'results', '*.mp4'))
Video_aud = Video.replace('.mp4', '_aud.mp4')

# concat audio
! ffmpeg -y -i {Video} -i data/{Aud} -c:v copy -c:a aac {Video_aud}

# display
video_file = open(Video_aud, 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
