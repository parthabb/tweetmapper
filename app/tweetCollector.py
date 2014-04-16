'''
Created on Apr 15, 2014

@author: spoyler
'''
from library import TweepyAPIs
import time
import json

class TweetCollector(object):
    '''
    classdocs
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
            #print (current-start);
            current = time.time();
    #search(term);
        self.APIcount = 0;
        
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
        handle = TweepyAPIs()
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
         
ts = TweetStream()
list = ["KatyPerry"]
ts.stream(list)
        