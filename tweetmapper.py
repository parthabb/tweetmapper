# main tweetmapper application


import math
import os
import re
import pickle


city_coordinates = [(0,0)]
stopwords = ()
TOTAL_CITIES = 50


def classify_city_id(geocode):
  nearest_city_id = 0
  identifier = 0
  minimum = math.sqrt(math.pow(city_coordinates[0](0) - geocode(0), 2) +
                  math.pow(city_coordinates[0](1) - geocode(1), 2))
  for city in city_coordinates[1:]:
    identifier += 1
    temp = math.sqrt(math.pow(city(0) - geocode(0), 2) +
                     math.pow(city(1) - geocode(1), 2))
    if temp < minimum:
      nearest_city_id = id
  return nearest_city_id


def get_all_file_names():
  """Lists of all file names ending with 'endswith' in dir_name and its children

  Returns:
    A list of all files in directory tweets ending with '.txt'.
  """
  all_txt_files = []
  for root, _, files in os.walk('tweets'):
    for f in files:
      if f.endswith('.txt'):
        all_txt_files.append(os.path.join(root, f))
  return all_txt_files


class TweetMapper (object):
  """Main tweetmapper application."""
  def __init__ (self):
    self.inverse_term_matrix = {}
    self._total_docs = 0
    self.data = []

  def read_tweet_from_file(self):
    filenames = get_all_file_names()
    self._total_docs = len(filenames)

    for trending_tweet_file in filenames:

      tweets = []

      with open(trending_tweet_file, 'r') as f:
        tweets = pickle.load(f.read())

      for tweet in tweets:
        self._construct_inverse_map(tweet)

  def calculate_tfidf(self):
    """Calculate the TF-IDF."""
    for _, posting in self.inverse_term_matrix.iteritems():
      idf = math.log10(float(self._total_docs)/float(len(posting.keys())))
      for city, tf in posting.iteritems():
        tfidf = float(1 + math.log10(tf)) * idf
        posting[city] = tfidf

  def _case_fold (self, text):
    """Case the given word."""
    return text.lower()

  def _construct_inverse_map(self, tweet):
    """Construct an inverse term dictionary."""
    tweet_city = classify_city_id(tweet['coordinates']['coordinates'])

    for token in re.findall('[a-zA-Z0-9]+', tweet['text']):
      if token:
        token = self._case_fold(token)
        if token in stopwords:
          continue
        postings = self.inverse_term_matrix.get(token, {tweet_city: 0})
        postings[tweet_city] = postings.get(tweet_city, 0) + 1
        self.inverse_term_matrix[token] = postings

  def contruct_training_data(self):
    """Construct a representation of the data to be used in classification."""
    for city_id in xrange(TOTAL_CITIES):
      temp = [city_id]
      for postings in self.inverse_term_matrix.values():
        temp.append(postings.get(city_id, 0))
      self.data.append(','.join(temp))
