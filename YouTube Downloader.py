from pytube import YouTube

# Path: YouTube Downloader.py

link = input("Enter the link(URL) of YouTube video you want to download:  ")
yt_dn = pytube.YouTube(link)
yt_dn.streams.first().download()
print("Download completed!!")
