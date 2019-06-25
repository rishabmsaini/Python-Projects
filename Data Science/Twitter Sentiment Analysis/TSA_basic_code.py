import tweepy
from textblob import TextBlob

consumer_key='ENTER YOUR CONSUMER KEY HERE'
consumer_secret='ENTER YOUR CONSUMER SECRET HERE'

access_token='ENTER YOUR ACCESS TOKEN HERE'
access_token_secret='ENTER YOUR ACCESS TOKEN SECRET HERE'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

word=input('Enter a topic : ')
public_tweets=api.search(word)

for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)
	print('')
