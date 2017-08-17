# HW 3

#Layman: Less than 100
#Expert: 100-1000
#Celebrity: over 1000

#1st degree of separation
#Most active
#Most Popular
#Among the friends of your target, i.e. the users she is following, who are the most active layman, expert and celebrity?
#Among the friends of your target who is the most popular?

import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/
#Get access to API
#auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret')
#auth.set_access_token('your access token', 'your access token secret')    
#api = tweepy.API(auth)

auth = tweepy.OAuthHandler(
auth.set_access_token(
api = tweepy.API(auth)



#See rate limit
api.rate_limit_status()

#Create user objects
mig = api.get_user('miguelmaria') #49
#seth = api.get_user('seth_j_hill') #990
#andrew = api.get_user('ajreeves') #1,190

dir(mig)

mig.followers_ids() 

migFollowers= []
for follower_id in mig.followers_ids():
	user = api.get_user(follower_id)
	migFollowers.append(user.screen_name)







