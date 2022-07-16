import re
from pytube import Playlist

class Downloader:

    
    YOUTUBE_STREAM_AUDIO = '140'


    def __init__(self, directory, playlist):
        self.download_dir = directory
        self.playlist = Playlist(playlist)
        self.playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    def get_num_links(self):
        return len(playlist.video_urls)

    def get_links(self):
        return playlist.video_urls

    def download(self):
        # physically downloading the audio track
        count = 1
        for video in playlist.videos:
            if count > 235:
                audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
                audioStream.download(output_path=download_dir)
            print(count)
            count+=1