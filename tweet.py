import tweepy
import os

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']

access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']

def tweet(message):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    api.update_status(message)

