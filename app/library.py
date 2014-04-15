# Utility methods.

import tweepy
import sys


class TweepyAPIs (object):
  """Base class for all needed tweepy APIs"""
  def __init__ (self):
    # Put your twitter credentials here.
    consumer_key = "W48HuKv5qcEl9bryHwAjA"
    consumer_secret = "vf4M7dxlXQRuwdM1dASB0sg0ZkxnlMSWLWNc9B4"
    access_key = "596178706-6SvITfh1xSdjUkIv5cvCQuHr8b5aD8sX6WxAl6AU"
    access_secret = "IS0Wcplvg6WUwGVCFC53tdszsjoX850orNEmFSVDeWj6O"

    if not (consumer_key and consumer_secret and access_key and access_secret):
      print "Please enter all of your credentials."
      sys.exit()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    self._api = tweepy.API(auth, parser=tweepy.parsers.ModelParser())

  def GetTrends (self):
    """Retruns the available trends."""
    return self._api.trends_available()

  def GetTrendsByLocation (self, woeid=23424977):
    """Get trends based on the locations WOEID. Default is US."""
    return self._api.trends_place(woeid)

