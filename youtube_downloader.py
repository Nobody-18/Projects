from pytube import YouTube
from sys import argv

link = argv[1]
resolution = argv[2]
yt = YouTube(link)
print(f'Title: {yt.title}')
print(f"{yt.__sizeof__()}")
yd = yt.streams.get_highest_resolution()
yd.download('/home/ajulanilkumar/Downloads/Youtube_Downloads')

   



