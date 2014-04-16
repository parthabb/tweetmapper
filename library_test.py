import library

class TweepyAPIsTest(object):
  def __init__ (self):
    self.tweets_apis = library.TweepyAPIs()

  def testTrends(self):
    print '============ Top Trends ================'
    print self.tweets_apis.GetTrends()
    print '============ Top Trends ================'

  def testTrendsByLocation(self):
    print '============ Top Trends by location ================'
    print self.tweets_apis.GetTrendsByLocation()
    print '============ Top Trends by location ================'

  def run(self):
    self.testTrends()
    self.testTrendsByLocation()


if __name__ == '__main__':
  tat = TweepyAPIsTest()
  tat.run()
