import re
from pytube import Playlist
import time

YOUTUBE_STREAM_AUDIO = '140'

class Downloader:


    def __init__(self, directory, playlist):
        self.count = 0
        self.down_rn = ''
        self.download_dir = directory
        self.playlist = Playlist(playlist)
        self.playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    def get_num_links(self):
        return len(self.playlist.video_urls)

    def get_links(self):
        return self.playlist.video_urls

    def download(self, from_count, list_view):
        # physically downloading the audio track
        self.count = 0 # redundant
        for video in self.playlist.videos:
            if self.count >= from_count:
                list_view.addItems([str(self.count)+" "+self.down_rn])
                list_view.repaint()
                audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
                audioStream.download(output_path=self.download_dir)
                self.down_rn = self.playlist.video_urls[self.count]
            self.count+=1
        self.count = 0