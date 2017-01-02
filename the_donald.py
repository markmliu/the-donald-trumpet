import tweepy
import api_keys
import simplejson
import os

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet_text =  simplejson.loads(data)["text"]
        os.system("echo '{}' | say ".format(tweet_text))
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
    stream.filter(follow=['25073877'])
    
