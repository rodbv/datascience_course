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

def process_tweets(tweets, sent_scores):
  return [calc_sentiment(t.get("text"), sent_scores) for t in tweets]

def calc_sentiment(tweet, sent_scores):
  if not tweet:
    return 0

  score = 0
  for term in tweet.split():
    if (sent_scores.get(term)):
      score += sent_scores.get(term)
  return score
 
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    sent_scores = load_sentiment_scores(sent_file)
    tweets = load_tweets(tweet_file)

    result = process_tweets(tweets, sent_scores)
    for item in result:
      print item

    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
