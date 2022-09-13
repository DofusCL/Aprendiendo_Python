import tweepy

consumer_key = '46qg1HnLazDbKJhri9SG2Nuwz'
consumer_secret ='8AhAF2no3pVUdL87C3jEmGKoX14qG0fBNzNfW8oxqhfM5qPJPd' 
access_token = '1007255574944378882-0n1qOB52KDouC6hoEKtYhtNOKzjQpN'
access_token_secret = 'fPhk1p4Z4Sj50sXwZBg6Q8wWEJOVfVdV7ArLiFWKjHEoE'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)