import tweepy
from secrets import *

# Consumer keys and access tokens, used for OAuth
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

# OAuth process, using the keys and tokens

# # Creation of the actual interface, using authentication
# api = tweepy.API(auth)
# # Sample method, used to update a status
# api.update_status('Testier')

# method to answer to the hashtag "askYP"
def parseForYP():
    for t in tweepy.Cursor(api.search, q='#findmecool').items(4):
        # obtain the ID from the original tweet so it can be replied to.
        tweetID = (t.id)
        # obtain the user ID so it can reply it
        user = (t.user.screen_name)
        # generate the message
        message = "@" + user + " " + str(count)
        # reply to the user
        t2 = api.update_status(message, tweetID)
        count+=1
        return t2

def parseTwitter(query):
    for t in tweepy.Cursor(api.search, q=query).items(4):
        t["statuses"]




i = input("input")
parseTwitter(i)
