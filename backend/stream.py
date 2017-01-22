
#Import the necessary methods from tweepy library
import argparse

from google.cloud import language
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from secrets import *

import json

positives = 0
negatives = 0
neutrals = 0
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        json_strings = json.loads(data)
        tweetText = json_strings["text"]
        analyze(tweetText)
        return True

    def on_error(self, status):
        print (status)


def analyze(tweet):
    """Run a sentiment analysis request on text within a passed filename."""
    print("analyzing")
    language_client = language.Client()
    document = language_client.document_from_text(tweet)

    # Detects sentiment in the document.
    annotations = document.annotate_text(include_sentiment=True,
                                            include_syntax=False,
                                            include_entities=False)

    # Print the results
    print_result(annotations)

def print_result(annotations):
    global positives
    global neutrals
    global negatives
    score = annotations.sentiment.score
    magnitude = annotations.sentiment.magnitude

    if(score > -0.1 and score <0.1):
        neutrals = neutrals+1
    elif(score > 0.1):
        positives = positives +1
    else:
        negatives = negatives + 1

    print("Positives: "+str(positives)+", negatives: "+str(negatives)+", neutrals: " + str(neutrals))
    return 0

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Trump'])