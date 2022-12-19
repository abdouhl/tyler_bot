import tweepy
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import os
from deta import Deta

load_dotenv(join(dirname(__file__), '.env'))

deta = Deta(os.environ.get("DETA_KEY"))
done_tyler_likes = deta.Base("done_tyler_likes")


twitter_auth_keys = {
	"consumer_key"        : os.environ.get("TYLER_BOT_CONSUMER_KEY"),
	"consumer_secret"     : os.environ.get("TYLER_BOT_CONSUMER_SECRET"),
	"access_token"        : os.environ.get("TYLER_BOT_ACCESS_TOKEN"),
	"access_token_secret" : os.environ.get("TYLER_BOT_ACCESS_TOKEN_SECRET")
}

auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
        )
auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
        )
api = tweepy.API(auth)

influencers = ["GreatestQuotes","BrainyQuote","MakeItAQuote"]
done=0
for influencer in influencers:
	for tweet in tweepy.Cursor(api.search_tweets, q=f'to:{influencer}',result_type='recent').items(200):
		p = done_tyler_likes.fetch({"value": tweet.id_str})
		if p.count != 0:
			continue
		try:
			api.create_favorite(tweet.id_str)
		except:
			continue
		print('tweet',tweet.id_str)
		done_tyler_likes.put(tweet.id_str)
		done=1
		break
	if done ==1:
	    break











