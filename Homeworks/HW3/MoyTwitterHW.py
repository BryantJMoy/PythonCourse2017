# HW 3

#Layman: Less than 100
#Expert: 100-1000
#Celebrity: over 1000

import tweepy
import time
import operator #index, value = max(enumerate(my_list), key=operator.itemgetter(1))

Check the documentation page
http://docs.tweepy.org/en/v3.2.0/
Get access to API
auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret')
auth.set_access_token('your access token', 'your access token secret')    
api = tweepy.API(auth)


#See rate limit
api.rate_limit_status()

#Create user objects
bjm = api.get_user('bryantjmoy') #162 Followers

dir(bjm)

bjm.followers_ids() 

bjmFollowers= []
bjmFollowers_number_of_statuses = []
for ids in bjm.followers_ids():
	user = api.get_user(ids)
	bjmFollowers.append(user.screen_name)
	bjmFollowers_number_of_statuses.append(user.statuses_count)

# Most Active by Tweets: RWRCRadio, 108959 times 

def ActiveFollowerTweets(target):
	Followers = []
	Followers_number_of_statuses = []
	for ids in target.followers_ids():
		user = api.get_user(ids)
		Followers.append(user.screen_name)
		Followers_number_of_statuses.append(user.statuses_count)
    index, value = max(enumerate(Followers_number_of_statuses), key=operator.itemgetter(1))
    active_user = Followers[index]
    num_of_tweets = value
    return "The follower with the most tweets is %s. They have tweeted %s times." %(active_user, num_of_tweets)

# Most Popular by followers: Dambisamoyo, 174238 followers

def MostFollowers(target):
    Followers = []
    Followers_number_of_followers = []
    for ids in target.followers_ids():
        user = api.get_user(ids)
        Followers.append(user.screen_name)
        Followers_number_of_followers.append(user.followers_count)
    index, value = max(enumerate(Followers_number_of_followers), key=operator.itemgetter(1))
    active_user = Followers[index]
    num_of_followers = value
    return "The follower with the most followers is %s. They have %s followers." %(active_user, num_of_followers)


# Friends of target, who are the most active layman, expert, and celebrity
#Layman: Jess_Tark 4933
#Expert: JayNicoleB 28954
#Celeb: thehill 344913

def ActiveLEC(target):  
	layman_name=[]
	layman_num_of_statuses=[]
	expert_name=[]
	expert_num_of_statuses=[]
	celeb_name=[]
	celeb_num_of_statuses=[]
	for ids in api.friends_ids(target.screen_name):
		user = api.get_user(ids)
		if user.followers_count < 100: #101?
			layman_name.append(user.screen_name)
			layman_num_of_statuses.append(user.statuses_count)
		elif user.followers_count > 100 and user.followers_count < 1000:
			expert_name.append(user.screen_name)
			expert_num_of_statuses.append(user.statuses_count)
		else:# user.followers_count > 1000:
			celeb_name.append(user.screen_name)
			celeb_num_of_statuses.append(user.statuses_count)
	Lindex, Lvalue = max(enumerate(layman_num_of_statuses), key=operator.itemgetter(1))
	laymen = layman_name[Lindex]
	layman_count = Lvalue
	Eindex, Evalue = max(enumerate(expert_num_of_statuses), key=operator.itemgetter(1))
	expert = expert_name[Eindex]
	expert_count = Evalue
	Cindex, Cvalue = max(enumerate(celeb_num_of_statuses), key=operator.itemgetter(1))
	celeb = celeb_name[Cindex]
	celeb_count = Cvalue
	print "The most active layman friend of this account is %s. They have tweeted %s times. The most active expert friend of this account is %s. They have tweeted %s times. The most active celeb friend of this account is %s. They have tweeted %s times." %(laymen, layman_count, expert, expert_count, celeb, celeb_count)




# Friend of Target, most popular by number of followers
# BarackObama 628474

def ActiveFollowerFriend(target):
	FollowersFriend = []
	FollwersFriend_number_of_friends = []
	for ids in api.friends_ids(target.screen_name):
		user = api.get_user(ids)
		FollowersFriend.append(user.screen_name)
		FollwersFriend_number_of_friends.append(user.friends_count)
	index, value = max(enumerate(FollwersFriend_number_of_friends), key=operator.itemgetter(1))
	active_user = FollowersFriend[index]
	num_of_friends = value
	return "The follower's friend with the most followers is %s. They %s followers." %(active_user, num_of_friends)



##### Two Degrees of Separation ###############


#### Among the followers of your target and their followers, who is the most active?
# RWRCRadio 108962

def TwoDegreesActiveFollower(target):
    targets_followers = []
    targets_followers_names= []
    targets_followers_number_of_statuses = []
    for ids in target.followers_ids():
        user = api.get_user(ids)
        if user.followers_count < 100: #layman
            pass #skip
        else:
            targets_followers.append(user.id)
            targets_followers_number_of_statuses.append(user.statuses_count)
            targets_followers_names.append(user.screen_name)
    for follower in targets_followers:
        user = api.get_user(follower)
        if user.followers_count > 101: # Expert and Celbs
            pass
        else:
            targets_followers_number_of_statuses.append(user.statuses_count)
            targets_followers_names.append(user.screen_name)
    index, value = max(enumerate(targets_followers_number_of_statuses), key=operator.itemgetter(1))
    active_user = targets_followers_names[index]
    targets_followers_number_of_statuses = value
    return "The most active 2nd degree follower of your target is %s. They have tweeted %s times." %(active_user, targets_followers_number_of_statuses)



### Among the friends of your target and their friends, who is the most active?
# thehill 344921


def TwoDegreeActiveFriend(target):
    targets_friends = []
    targets_friends_names= []
    targets_friends_number_of_statuses = []
    for ids1 in api.friends_ids(target.screen_name):
        user = api.get_user(ids1)
        if user.friends_count < 100: #layman
            pass
        else:
            targets_friends.append(user.id)
            targets_friends_number_of_statuses.append(user.statuses_count)
            targets_friends_names.append(user.screen_name)
    for ids2 in targets_friends :
        user = api.get_user(ids2)
        if user.friends_count > 101: # Expert and Celbs
            pass
        else:
            targets_friends_number_of_statuses.append(user.statuses_count)
            targets_friends_names.append(user.screen_name)
    index, value = max(enumerate(targets_friends_number_of_statuses), key=operator.itemgetter(1))
    active_user = targets_friends_names[index]
    targets_friends_number_of_statuses = value
    return "The The most active 2nd degree friend of your target is %s. They have tweeted %s times." %(active_user, targets_friends_number_of_statuses)








