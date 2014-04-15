# Utility methods.

import tweepy
import sys


class TweepyAPIs (object):
  """Base class for all needed tweepy APIs"""
  _trends_type = {
      'current': 'trends_current',
      'daily': 'trends_daily',
      'weekly': 'trends_weekly',
  }

  def __init__ (self):
    # Put your twitter credentials here.
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""
  
    if not (consumer_key and consumer_secret and access_key and access_secret):
      print "Please enter all of your credentials."
      sys.exit()
  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    self._api = tweepy.API(auth, parser=tweepy.parsers.ModelParser())

  def GetTrends (self, trend_type='default'):
    return getattr(self._api, TweepyAPIs._trends_type.get(trend_type,
                                                          'trends'))()

  def GetTrendsByLocation (self, woeid=23424977):
    return self._api.trends_location(woeid)
