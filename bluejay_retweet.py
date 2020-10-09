import tweepy
from time import sleep
from credentials import * # Import your Twitter API credentials from credentials.py


## Configuration settings for querying hashtags, liking Tweets, and following Tweeters.
# This is hastag which BlueJay will search for and retweet. ex: '#birds'
QUERY = '#BlueJay_bot'
# BlueJay bot setting for liking Tweets. If 'True', BlueJay Bot will like the searched Tweet. If 'False', it will not like it.
LIKE = True 
# BlueJay bot setting for following the user who tweeted. If 'True', BlueJay bot will follow the user who tweeted, otherwise it will not.
FOLLOW = False
# BlueJay bot sleep time setting in seconds. Ex: SLEEP_TIME = 300 means 5 minutes sleep time. This will put the bot to sleep to avoid too many API requests and being banned.
SLEEP_TIME = 300

# Authenticate access to your Twitter account via API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("BlueJay bot for retweets, likes and follows")
print("BlueJay Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('BlueJay has retweeted the tweet')

        # Favorite the tweet
        if LIKE:
            tweet.favorite()
            print('BlueJay has favorited the tweet')

        # Follow the user who tweeted
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('BlueJay has followed the user')

        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
