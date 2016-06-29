#!/usr/local/bin/python3.5

import tweepy

# Keys for script
consumer_key = 'PMJPxbSffY8VKyAdMZxbi1c30'
consumer_secret = 'jgTdyXyRUDjDJBl53mepa24z7Dn0UzIt4cwKjIOjGVtw5VL39D'
access_token = '747900423286165505-d4HDnG8WEDOmLwGl9exJYQHRV0HH52Z'
access_token_secret = 'cW0FDtFwG4b8IJgCBhRA0M8lHl80X3tBcu98co4xhFr4N'

#Authorize the script
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Get the api object and set name 
api = tweepy.API(auth)
handle = "CillaryHancer"

#Read id from file and timeline
lastID = int(readID())
tweetID = getTweetID(api, handle)

if lastID < tweetID:
    respond(api, tweetID)
    writeID(tweetID)
    
def readID():
    file = open('lastid', 'r')
    str = file.read()
    file.close()
    
    return str

def writeID(newID):
    file = open('lastid', 'w')
    file.write(newID)
    file.close
    
def respond(api, tweetID):
    #Read random fact
    api.update_status("@CillaryHancer Bad " +  str(tweetID), in_reply_to_status_id = tweetID)

def getTweetID(api, handle):
    timeline = api.user_timeline(handle, count = 1)
    return timeline[0].id
