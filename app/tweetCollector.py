'''
Created on Apr 15, 2014

@author: spoyler
'''
from library import TweepyAPIs
import time
import json

class TweetCollector(object):
    '''
    collects tweets using rest API
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.APIcount = 0
        
    def search(self, term):
        handle = TweepyAPIs()
        if self.APIcount < 90:
            self.results = handle._api.search(q=term,lang="en",count=100,include_rts="true");
            self.APIcount = self.APIcount + 1
            print self.results
        else:
            self.countDown()

    def countDown(self):
        start = time.time();
        current = time.time();
        print "Counting down...."
        while (current - start) < 900:
            current = time.time();
        self.APIcount = 0;
        
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
        handle = TweepyAPIs()
        self.results = handle.stream;
        self.results.filter(track=trend)

    def countDown(self):
        start = time.time();
        current = time.time();
        print "Counting down...."
        while (current - start) < 900:
            current = time.time();
        self.APIcount = 0;
    
         
ts = TweetStream()
lst = ["KatyPerry"]
ts.stream(lst)
        