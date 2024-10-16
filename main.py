import os
import tweepy
import time
import random

# Twitter API credentials
consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# List of countries (you can expand this list)
countries = ["France", "Germany", "Spain", "Italy", "UK", "USA", "Canada", "Japan", "Australia", "Brazil"]

def tweet_message(country):
    message = f"Hello, {country}! #WorldGreetings"
    try:
        api.update_status(message)
        print(f"Tweeted: {message}")
    except tweepy.errors.Forbidden as e:
        print(f"Error tweeting: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Main loop
while True:
    for country in countries:
        tweet_message(country)
        time.sleep(1800)  # Wait for 30 minutes (1800 seconds)
    
    # Shuffle the list for next round
    random.shuffle(countries)
