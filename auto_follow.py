import tweepy
import os




CONSUMER_KEY=os.environ.get('Ckey')
CONSUMER_SELECT=os.environ.get('Csecret')
ACCESS_TOKEN=os.environ.get('Akey')
ACCESS_SELECT=os.environ.get('Asecret')

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SELECT)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SELECT)

api=tweepy.API(auth)


