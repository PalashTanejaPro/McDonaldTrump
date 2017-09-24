import tweepy, time, sys
import markovify

 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '718SuvNagyr8ssNhK2UVNuDFX'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Est3Zj0ijr2JYi3TSZkyDMzHlFadXpPvqIf8EXvh7AfdsOOGK5'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '911848230937255936-vUIwY51y8IVW0WIFtSS1q8tU4USEl2c'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'bdzTHNFIZCrDsmgF8qqZn7Hda7F2mG3SB7RZim13kM5Mx'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
model_json = open('sav1.json').read()
model = markovify.Text.from_json(model_json)

line = model.make_short_sentence(200)

api.update_status(line)
print("Tweet Made: ",line)
time.sleep(900)#Tweet every 15 minutes