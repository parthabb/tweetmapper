import library
import tweetCollector
import json

class TweetCollectorTest(object):
  def __init__(self):
    self.tc = tweetCollector.TweetStream()
    self.ts = tweetCollector.TweetCollector()

  def run(self):
    tas = library.TweepyAPIs()
    trends = tas.GetTrendsByLocation()[0].get('trends', [])
    terms = [trend.get('name') for trend in trends]
    self.tc.stream(terms)
    '''terms = ["#tcot","#lnyhbt","#bundyranch","#teaparty","#hottieoftheweek",
             "#pjnet","#tgdn","#bloodmoon","#p2","#tlot"]
    terms = ["#bloodmoon"]
    for term in terms:
        self.ts.search(term)'''
    
  def filter(self):
    fil = tweetCollector.Filter()
    dir = "data/14"
    fil.process(dir)
    #dir = "test"
    #fil.process(dir)

if __name__ == '__main__':
  tct = TweetCollectorTest()
  #tct.run()
  tct.filter()
