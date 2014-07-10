import sys
import json 

def load_sentiment_scores(sent_file):
  scores = {} # initialize an empty dictionary
  for line in sent_file:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  return scores

def load_tweets(tweets_file):
  return [json.loads(line) for line in tweets_file]

def process_terms(tweets, sent_scores):
  words = {}
  for tweet in tweets:
    score = calc_sentiment(tweet, sent_scores)
    if tweet.get("text") != None:
      terms = tweet.get("text").split()
      for term in terms:
        if not term in words:
          words[term] = 0
        words[term] += score
  return words
        
def print_results(words):
  for key in words:
    print "%s\t%s" % (key, words[key])


def calc_sentiment(tweet, sent_scores):
  if not tweet:
    return 0
  if not tweet.get("text"):
    return 0

  score = 0

  for term in tweet.get("text").split():
    if (sent_scores.get(term)):
      score += sent_scores.get(term)
  return score
 


def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  
  sent_scores = load_sentiment_scores(sent_file)
  tweets = load_tweets(tweet_file)

  words = process_terms(tweets, sent_scores)
  print_results(words)

if __name__ == '__main__':
    main()
