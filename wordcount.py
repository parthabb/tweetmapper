# main tweetmapper application

import re
import mrjob
from mrjob import job


class MRWordFrequencyCount(job.MRJob):

  INPUT_PROTOCOL = mrjob.protocol.PickleValueProtocol

  def init(self):
    self.inverse_dict = {}

  def read_tweet(self, _, tweet):
    for token in re.findall('[a-zA-Z0-9]+', tweet['text']):
      token = self._case_fold(token)
      if not token or token in []:
        continue
      self.inverse_dict[token] = self.inverse_dict.get(token, 0) + 1

  def get_words (self):
    for word, val in self.inverse_dict.iteritems():
      yield word, val

  def sum_words(self, word, counts):
    yield word, sum(counts)

  def steps(self):
    return [self.mr(mapper_init=self.init,
                    mapper=self.read_tweet,
                    mapper_final=self.get_words,
                    combiner=self.sum_words,
                    reducer=self.sum_words)]


if __name__ == '__main__':
    MRWordFrequencyCount.run()
