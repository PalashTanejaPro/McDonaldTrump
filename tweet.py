import tweepy, time, sys
import markovify
#remove these keys, preferably putting them on a secured server only
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
model_json = open('sav1.json').read()
model = markovify.Text.from_json(model_json)

line = model.make_short_sentence(200)

api.update_status(line)
print("Tweet Made: ",line)
time.sleep(9000)#Tweet every 15 minutes
