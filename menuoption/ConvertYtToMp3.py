from pytube import YouTube
from .MenuOption import MenuOption

def download_youtube_as_audio():
    url = input("Please enter a url: ")
    filename = input("Please enter a full path and filename: ")

    yt = YouTube(url)

    # Find the best audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio track
    audio_stream.download(filename=filename)

# download_youtube_as_audio("https://www.youtube.com/watch?v=Hl-XsneiGHo", "August 10.mp3")

def getMenuOption():
  mo = MenuOption("Convert Youtube", download_youtube_as_audio)
  return mo