import os
import glob
from IPython.display import HTML
from base64 import b64encode

def get_latest_file(path):
  dir_list = glob.glob(path)
  dir_list.sort(key=lambda x: os.path.getmtime(x))
  return dir_list[-1]
 
Video = get_latest_file(os.path.join('trial', 'results', '*.mp4'))
Video_aud = Video.replace('.mp4', '_aud.mp4')

# concat audio
! ffmpeg -y -i {Video} -i data/{Aud} -c:v copy -c:a aac {Video_aud}

# display
def show_video(video_path, video_width=450):
   
  video_file = open(video_path, "r+b").read()
  video_url = f"data:video/mp4;base64,{b64encode(video_file).decode()}"

  return HTML(f"""<video width={video_width} controls><source src="{video_url}"></video>""")
  
show_video(Video_aud)
