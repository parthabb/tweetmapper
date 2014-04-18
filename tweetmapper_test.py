# Test cases

import tweetmapper
from tweetmapper import TweetMapper

def test_get_all_file_names():
  print """ =================== get_all_file_names ================== """
  print [trend.lstrip('tweets/').rstrip('.txt') for trend in tweetmapper.get_all_file_names()]
  print """ =================== get_all_file_names ================== """

def test_scoring():
  print """ =================== read tweet from file ================== """
  tm = TweetMapper()
  tm.run()
  print "classification : "+str(tm.city_vectors)
  print """ =================== get_all_file_names ================== """
  
if __name__ == '__main__':
  test_get_all_file_names()
  test_scoring()