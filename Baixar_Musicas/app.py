# Baixa em mp3

from pytube import YouTube, Playlist
import moviepy.editor as mp
import re
import os

# Digite o link
link = ("https://www.youtube.com/watch?v=t8lGXi7Rq9A&list=PLVzf-l752lZprUq0y2FPm_QKtus29Jafx")
path = 'musicas'
yt = YouTube(link)

# Começa o download
print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download Completo!")

# Converte mp4 para mp3
print("Convertendo arquivo...")
for file in os.listdir(path):
    if re.search('mp4',file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)

print('Sucesso!')


