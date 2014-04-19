import library
import tweetCollector

class TweetCollectorTest(object):
  def __init__(self):
    self.tc = tweetCollector.TweetStream()

  def run(self):
    tas = library.TweepyAPIs()
    trends = tas.GetTrendsByLocation()[0].get('trends', [])
    terms = [trend.get('name') for trend in trends]
    self.tc.stream(terms)
    
  def filter(self):
    fil = tweetCollector.Filter()
    dir = "data"
    fil.process(dir)

if __name__ == '__main__':
  tct = TweetCollectorTest()
  #tct.run()
  tct.filter()
