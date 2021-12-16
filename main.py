#import the package
from pytube import YouTube

url = "https://youtu.be/T2wCvfCFZlo"

my_video = YouTube(url)

print("******************Video Title*******************")

#set stream resolution 
my_video = my_video.streams.get_highest_resolution()


my_video.download()