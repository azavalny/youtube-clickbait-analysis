from googleapiclient.discovery import build
import urllib.request
import csv
import json

youtube_api_key = ''

youtube = build('youtube','v3' , developerKey=youtube_api_key)

class videoDataCollector:
    
    def __init__(self):
        pass

    def download_video_thumbnail(self, ID, fileName):
        """Saves the thumbnail of YouTube video of @id to the local directory with name @fileName"""
        urllib.request.urlretrieve('https://img.youtube.com/vi/{id}/mqdefault.jpg'.format(id=ID), fileName)

    def get_video_title(self, ID):
        """Returns the title of a YouTube video with ID"""
        snippet_request = youtube.videos().list(part='snippet', id= ID)
        response = snippet_request.execute()
        return response['items'][0]['snippet']['title']

    def get_video_stats(self, ID):
        """Returns the numerical statistics of a YouTube video with ID"""
        stat_request = youtube.videos().list(part='statistics', id= ID)
        response = stat_request.execute()
        return response['items'][0]['statistics']

#############
##Clickbait##
#############

ID ='sESRuTyfsEk'
collector = videoDataCollector()

title = collector.get_video_title(ID)
stats = collector.get_video_stats(ID)
collector.download_video_thumbnail(ID, fileName = str(ID + ";;" + str(title) +".jpg"))

row = (ID, title, stats['viewCount'], stats['likeCount'], stats['dislikeCount'], stats['favoriteCount'])

f = open('clickbait.csv', 'a', newline='')

csvwriter = csv.writer(f)
csvwriter.writerow(row)
f.close()

#################
##Non-Clickbait##
#################
#The YouTube API's web platform was used to make a request of the 100 most popular videos in the United States, which were saved to response.json,
#and each video was checked by a human to make sure they weren't clickbait

videos_1 = ""
videos_2 = ""
with open('response_1.json', 'r') as r:
    response = r.read()
    videos_1 = json.loads(response)
with open('response_2.json', 'r') as f:
    response = f.read()
    videos_2 = json.loads(response)

#Getting a list of id's of these videos, so I can get their data similarily to the clickbait videos
nonClickBaitIDs = []
for i in range(49):
    nonClickBaitIDs.append(videos_1["items"][i]['id'])
    nonClickBaitIDs.append(videos_2["items"][i]['id'])

for video in nonClickBaitIDs:
    collector = videoDataCollector()

    title = collector.get_video_title(video)

    for c in title:
        if(not c.isascii() or c =="|" or c =="/" or c==":" or c=="?" or c=="*" or c=='"'):
            title = title.replace(c, '')

    stats = collector.get_video_stats(video)

    file = str(video + ";;" + str(title) +".jpg")

    collector.download_video_thumbnail(video, fileName = file)

    row = (video, title, stats['viewCount'], stats['likeCount'], stats['dislikeCount'], stats['favoriteCount'])

    f = open('notClickbait.csv', 'a', newline='')

    csvwriter = csv.writer(f)
    csvwriter.writerow(row)
    f.close()
