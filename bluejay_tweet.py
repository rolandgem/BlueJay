import tweepy
from time import sleep
from credentials import * # Import your Twitter API credentials from credentials.py

# BlueJay bot sleep time setting in seconds. Ex: SLEEP_TIME = 300 means 5 minutes sleep time. This will put the bot to sleep to avoid too many API requests and being banned.
SLEEP_TIME = 300

# Authenticate access to your Twitter account via API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Read in your text Tweets 
my_file=open('my_tweets.txt','r')
file_lines=my_file.readlines()
my_file.close()

# Create a loop to iterate over each line
for line in file_lines:
# Add try/except to flag any errors
    try:
        print(line)
        # Add if statement to make sure that blank lines are skipped
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(SLEEP_TIME) # Sleep time in seconds. This will put the bot to sleep before it goes to Tweet the next line in my_tweets.txt
