'''
Created on Apr 15, 2014

@author: spoyler
'''
import library
import pickle
import tweepy
import fnmatch
import os
import json
import cjson

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
    test = {}
    for tr in trend:
        if tr.strip() != "":
            handle = library.TweepyAPIs(tr)
            self.results = handle.stream;
            print tr
            #f = open("test_tweets.txt","a")
            #f.writelines("{"+tr+":")
            #f.writelines("[")
            tr = [tr]
            #f.close()
            self.results.filter(track=tr, languages=['en'], locations=[-180,-90,180,90])
            #f = open("test_tweets.txt","a")
            #f.writelines("]")
            #f.writelines("}")
            #f.close()

class Filter(object):
    '''
    Filter tweets according to language and location
    '''
    def process(self,dr):
        '''assumes nsf-awards-abstracts is in the python folder'''
        for dirpath, dirs, files in os.walk(dr):
            for eFile in fnmatch.filter(files, '*.txt'):
                fle = dirpath+"/"+eFile
                newfile = dirpath+"/"+"new.txt"
                f = open(newfile,"w")
                #print fle
                if os.path.isfile(fle) and fle != None:
                  with open(fle,'r') as myfile:
                    for line in myfile:
                        print line
                        line = cjson.decode(line)
                        if "text" in line:
                            tweet = {}
                            #myfile = json.loads(myfile)
                            tweet["text"] = line["text"]
                            tweet["coordinates"] = line["coordinates"]
                            if line["lang"] and line["coordinates"]:
                                if line["lang"] == "en" and line["coordinates"]["type"] == "Point":
                                    if float(tweet["coordinates"]["coordinates"][0]) > -157 and float(tweet["coordinates"]["coordinates"][0]) < -66 and float(tweet["coordinates"]["coordinates"][1]) < 64 and float(tweet["coordinates"]["coordinates"][1]) >20:
                                        tweet = json.dumps(tweet)
                                        f.writelines(tweet)
                                        f.write("\n")
                os.rename(newfile, fle)
                #os.remove(newfile)