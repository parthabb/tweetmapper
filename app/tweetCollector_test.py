import library
import tweetCollector

class TweetCollectorTest(object):
  def __init__(self):
    self.tc = tweetCollector.TweetCollector()

  def run(self):
    tas = library.TweepyAPIs()
    trends = tas.GetTrendsByLocation()[0].get('trends', [])
    for trend in trends:
      if trend.get('name'):
        self.tc.search(trend['name'])

if __name__ == '__main__':
  tct = TweetCollectorTest()
  tct.run()
