#!/usr/bin/python
import tweepy
import api_keys
import simplejson
import subprocess

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

DONALD_TRUMP_USER_ID = 25073877

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_status(self, status):
        # Ignore tweets by anyone other than Trump.
        if status.author.id != DONALD_TRUMP_USER_ID:
            return True
        tweet_text = status.text.encode('ascii', 'ignore')
        # Ignore retweets.
        if  'RT @' in tweet_text:
            return True
        print tweet_text        
        ps = subprocess.Popen(('echo', tweet_text), stdout=subprocess.PIPE)
        subprocess.call(('say'), stdin=ps.stdout)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(api_keys.consumer_key, api_keys.consumer_secret)
    auth.set_access_token(api_keys.access_token, api_keys.access_token_secret)
    stream = Stream(auth, l)
    
    # Filter to only Donald Trump's tweets.
    stream.filter(follow=[str(DONALD_TRUMP_USER_ID)])
