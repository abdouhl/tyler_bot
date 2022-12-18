import tweepy
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import os
load_dotenv(join(dirname(__file__), '.env'))




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


req = requests.get('https://api.quotable.io/random?tags=business|leadership')
data =req.json()
tweet = f'''"{data['content']}"--{data['author']}\n\n #{data['authorSlug'].replace('-','')} {"#"+" #".join(data['tags'])}'''[:280]
api.update_status(status=tweet)















