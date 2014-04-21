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
import time

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
    self.apicount = 0
    pass

  def countTimeOut(self):
    start = time.time();
    current = time.time();
    print "Counting down...."
    while (current - start) < 900:
        print (current-start);
        current = time.time();
    #search(term);
    self.apicount = 0;

  def search(self, term):
    handle = library.TweepyAPIs()
    #term = term + ' -RT'

    results = []
    count = 0
    filename = "test/"+str(term)+".txt"
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    f = open(filename,"a")
    print term
    IDList = []
    while count < 50:
        tweets = handle._api.search(q=term,
                               lang="en",
                               count=100, 
                                since="2014-04-14", 
                                until="2014-04-16")
        #print tweets
        self.apicount += 1
        if self.apicount > 90:
            self.countTimeOut()
        for tweet in tweets:
          if tweet.coordinates and tweet.text and (tweet.id not in IDList):
            count += 1
            data = {}
            IDList.append(tweet.id);
            print IDList
            data["text"] = tweet.text
            data["created_at"] = str(tweet.created_at)
            #data['user'] = tweet.user
            #data['entities'] = tweet.entities
            data["id"] = tweet.id
            data["coordinates"] = tweet.coordinates
            #data['favorite_count'] = tweet.favorite_count
            #data['favorited'] = tweet.favorited
            #data['in_reply_to_status_id'] = tweet.in_reply_to_status_id
            #data['id_str'] = tweet.id_str
            #data['in_reply_to_screen_name'] = tweet.in_reply_to_screen_name
            #data['in_reply_to_status_id_str'] = tweet.in_reply_to_status_id_str
            #data['in_reply_to_user_id'] = tweet.in_reply_to_user_id
            #data['in_reply_to_user_id_str'] = tweet.in_reply_to_user_id_str
            data["lang"] = tweet.lang
            #data['place'] = tweet.place
            #data['retweet_count'] = tweet.retweet_count
            #data['retweeted'] = tweet.retweeted
            #data['source'] = tweet.source
            '''#tweet = json.loads(tweet)
            for field in _required_fields:
                data[field] = (getattr(tweet, field))
                if field == "created_at":
                  data[field] = str(getattr(tweet, field))
            #print data'''
            obj = json.dumps(data)
            #print data
            f.writelines(obj)
            f.writelines("\n")
            results.append(data)
    f.close()


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