# Baixa videos da playlist
from pytube import Playlist, YouTube

playlist = Playlist("https://www.youtube.com/watch?v=Zl_-LrT5uxg&list=PL6V_jTjwqA9nrYJ8SyYkcxZI6t5G-vmdZ")

for video in playlist:
    youtube = YouTube(video)

    youtube.streams.get_highest_resolution().download()