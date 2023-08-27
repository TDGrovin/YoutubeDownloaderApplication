#Script to download Youtube videos
#It also updates the meta data of each video

from pytube import YouTube
from pytube import exceptions

def Download(**information):
    youtubeObject = YouTube(information["url"])
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    
    information.update({
        "title" : youtubeObject.title,
        "size" : youtubeObject.filesize_mb,
    })
    #Download can be changed below
    try:
        youtubeObject.download(output_path = "D:\Coding Projects\Python\Youtube Downloader\Downloads") 
    except:
        information.update({"status" : "Download Unsuccessfull"})
    information.update({"status" : "Download Successfull"})
    
    