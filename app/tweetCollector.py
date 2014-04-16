'''
Created on Apr 15, 2014

@author: spoyler
'''
import pickle
import library
import time
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
    Constructor
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
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.APIcount = 0

    def stream(self,trend):
        handle = library.TweepyAPIs()
        if self.APIcount < 90:
            self.results = handle.stream;
            self.APIcount = self.APIcount + 1
            #print json.dumps(self.results)
            #trend = "["+trend+"]"
            self.results.filter(track=list)
        else:
            self.countDown()

    def countDown(self):
        start = time.time();
        current = time.time();
        print "Counting down...."
        while (current - start) < 900:
            #print (current-start);
            current = time.time();
    #search(term);
        self.APIcount = 0;
