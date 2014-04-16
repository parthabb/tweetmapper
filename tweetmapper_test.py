# Test cases

import tweetmapper

def test_get_all_file_names():
  print """ =================== get_all_file_names ================== """
  print [trend.lstrip('tweets/').rstrip('.txt') for trend in tweetmapper.get_all_file_names()]
  print """ =================== get_all_file_names ================== """


if __name__ == '__main__':
  test_get_all_file_names()