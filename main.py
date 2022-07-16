import os
from string import digits

def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

table = str.maketrans('', '', digits)

DIR = '/home/demid/Music/Rock'

files_str = os.listdir(DIR)

# print(files_str)

new_f = []
for f in files_str:
    n = remove_suffix(DIR+'/'+f.replace('  Supernatural - ', '').replace(
        '(The Road So Far)', '').replace('Netflix Version', '')
            .translate(table)[:-4], 'x') +'.mp4'
    print(n)
    o = DIR+'/'+f
    #print(o)
    os.rename(o, n)
    new_f.append(n)

seen = set()
dupes = [x for x in new_f if x in seen or seen.add(x)]    

print('-'*50)
print(dupes)
"""
import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = '/home/demid/Music/Rock'

playlist = Playlist('https://www.youtube.com/playlist?list=PLfq80JKaBD-K3C7gKiSX_RST_NQNUrq89')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
count = 1
for video in playlist.videos:
    if count > 235:
        audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
        audioStream.download(output_path=DOWNLOAD_DIR)
    print(count)
    count+=1

"""