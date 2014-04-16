# Utility methods.

import tweepy
import sys
from tweepy.streaming import StreamListener

class listener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

class TweepyAPIs (object):
  """Base class for all needed tweepy APIs"""
  def __init__ (self):
    # Put your twitter credentials here.
    consumer_key = "sLA3Hp02Fki2vUWufjNAi1kpS"
    consumer_secret = "hZImLluULkLwPXjunalcVkKT49AuQkxcRrAH4YmdxRfGHJrHLy"
    access_key = "1243936562-e9Q0mpNRpoMS2ksYwE0dNtrMsCYt6ZR4z70lYBy"
    access_secret = "recB79Pd2ZixUoPzXufkkRyeuXbRybcM7gycLMGK3cEds"
  
    if not (consumer_key and consumer_secret and access_key and access_secret):
        print "Please enter all of your credentials."
        sys.exit()
  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    self._api = tweepy.API(auth, parser=tweepy.parsers.ModelParser())
    self.stream =  tweepy.Stream(auth, listener())

  def GetTrends (self):
    """Retruns the available trends."""
    return self._api.trends_available()

  def GetTrendsByLocation (self, woeid=23424977):
    """Get trends based on the locations WOEID. Default is US."""
    return self._api.trends_place(woeid)

