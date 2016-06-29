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

#Get the api object and timestamp
api = tweepy.API(auth)
timeline = api.user_timeline("HillaryClinton")


