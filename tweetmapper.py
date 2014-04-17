# main tweetmapper application


import math
import nltk
import os
import re
import pickle

from app import tweetClassify

city_coordinates = [coordinates[2] for coordinates in tweetClassify.cities]

TOTAL_CITIES = 50


def classify_city_id(geocode):
  nearest_city_id = 0
  identifier = 0
  minimum = math.sqrt(math.pow(city_coordinates[0][0] - geocode[0], 2) +
                  math.pow(city_coordinates[0][1] - geocode[1], 2))
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
    self.traing_data = []
    self.target = []
    self.city_vectors = {}
    self.city_vectors_magnitude = {}

  def read_tweet_from_file(self):
    filenames = get_all_file_names()

    for trending_tweet_file in filenames:
      tweets = []
      with open(trending_tweet_file, 'r') as f:
        #print f.read()
        tweets = pickle.load(f)

      for tweet in tweets:
        self._construct_inverse_map(tweet)

  def calculate_tfidf(self):
    """Calculate the TF-IDF."""
    for _, posting in self.inverse_term_matrix.iteritems():
      idf = math.log10(50.0/float(len(posting.keys())))
      for city, tf in posting.iteritems():
        tfidf = float(1.0 + math.log10(tf)) * idf
        posting[city] = tfidf

  def _case_fold (self, text):
    """Case the given word."""
    return text.lower()

  def _construct_inverse_map (self, tweet):
    """Construct an inverse term dictionary."""
    tweet_city = classify_city_id(tweet['coordinates']['coordinates'])

    for token in re.findall('[a-zA-Z0-9]+', tweet['text']):
      token = self._case_fold(token)
      if not token or token in nltk.corpus.stopwords.words('english'):
        continue
      token = nltk.WordNetLemmatizer().lemmatize(token)
      postings = self.inverse_term_matrix.get(token, {tweet_city: 0.0})
      postings[tweet_city] = postings.get(tweet_city, 0.0) + 1.0
      self.inverse_term_matrix[token] = postings

  def generate_city_vectors (self):
    for term, postings in self.inverse_term_matrix.iteritems():
      for city, tfidf in postings.iteritems():
        words = self.city_vectors.get(city, {})
        words[term] = tfidf
        self.city_vectors[city] = words

    self.calculate_city_vectors_magnitude()

  def calculate_city_vectors_magnitude(self):
    for city, vector in self.city_vectors.iteritems():
      self.city_vectors_magnitude[city] = math.sqrt(
          math.fsum([math.pow(tfidf, 2) for tfidf in vector.values()]))

  def calculate_cosine_similarity (self, tweets_of_a_trend):  # tweets are in a list.
    """Return the most similar cities for the trend."""
    if not tweets_of_a_trend:
      print 'No tweets to classify.'
      return
    query_term_vector = {}
    for tweet in tweets_of_a_trend:
      for token in re.findall('[a-zA-Z0-9]+', tweet['text']):
        token = self._case_fold(token)
        if not token or token in nltk.corpus.stopwords.words('english'):
          continue
        token = nltk.WordNetLemmatizer().lemmatize(token)
        query_term_vector[token] += query_term_vector.get(token, 0.0) + 1
    query_magnitude = math.sqrt(
        math.fsum([math.pow(count, 2) for count in query_term_vector.values()]))

    # Calculate cosine scores.
    cosine_scores = {}
    for city, postings in self.city_vectors.iteritems():
      for word in query_term_vector.keys():
        cosine_scores[city] = cosine_scores.get(city, 0.0) + (
            query_term_vector[word] * postings.get(word, 0.0))
      cosine_scores[city] = cosine_scores[city] / (
          self.city_vectors_magnitude[city] * query_magnitude)

    return sorted(cosine_scores.iteritems(),
                  key=lambda x: x[1],
                  reverse=True
                 )[:10]

  def run(self):
    self.read_tweet_from_file()
    self.calculate_tfidf()
    self.generate_city_vectors()
    tweets_of_a_trend = []
    self.calculate_cosine_similarity(tweets_of_a_trend)
