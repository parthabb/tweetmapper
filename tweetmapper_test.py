# Test cases

import tweetmapper
import json
from tweetmapper import TweetMapper

def test_get_all_file_names():
  print """ =================== get_all_file_names ================== """
  print [trend.lstrip('tweets/').rstrip('.txt') for trend in tweetmapper.get_all_file_names()]
  print """ =================== get_all_file_names ================== """

def test_scoring():
  print """ =================== read tweet from file ================== """
  tm = TweetMapper()
  tm.run()
  #print "classification : "+str(tm.city_vectors)
  f = open("classify.txt","w")
  #obj = json.dumps(tm.city_vectors)
  f.writelines(str(tm.city_vectors))
  f.close()
  print """ =================== get_all_file_names ================== """
  
if __name__ == '__main__':
  test_get_all_file_names()
  test_scoring()