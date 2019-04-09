import tweepy
key1 = "#"
key11 = "#"
key2 = "#"
key22 = "#"

auth = tweepy.OAuthHandler(key1,key11)
auth.set_access_token(key2,key22)
api = tweepy.API(auth)
public_tweets = api.home_timeline()


name="nytimes"
tweetCount = 5
results = api.user_timeline(id=name, count=tweetCount)

for tweet in results:
      print (tweet.text)
