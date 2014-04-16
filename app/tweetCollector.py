'''
Created on Apr 15, 2014

@author: spoyler
'''
import pickle
import library
import tweepy

_required_fields = ('text', 'created_at', 'user', 'entities', 'id',
                    'coordinates', 'favorite_count', 'favorited',
                    'in_reply_to_status_id',
                    'id_str', 'in_reply_to_screen_name',
                    'in_reply_to_status_id_str', 'in_reply_to_user_id',
                    'in_reply_to_user_id_str', 'lang', 'place',
                    'retweet_count',
                    'retweeted', 'source')


class TweetCollector(object):
  '''
  classdocs
  '''
  def __init__(self):
    '''
    collects tweets using rest API
    '''
    pass

  def search(self, term):
    handle = library.TweepyAPIs()
    term = term + ' -RT'

    results = []
    tweets = handle._api.search(q=term,
                               lang="en",
                               count=100)
    for tweet in tweets:
      if tweet.coordinates and tweet.text:
        data = {}
        for field in _required_fields:
          data[field] = getattr(tweet, field)
        results.append(data)


    term = term.rstrip(' -RT')
    print '%s: %s' % (term, len(results))
    with open('%s.txt' % term, 'w') as f:
      pickle.dump(results, f)


class TweetStream(object):
  '''
  collects tweets from the streaming API
  '''
  def __init__(self):
    '''
    Constructor
    '''
    self.APIcount = 0

  def stream(self,trend):
    handle = library.TweepyAPIs()
    self.results = handle.stream;
    self.results.filter(track=trend)
