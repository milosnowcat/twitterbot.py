# TODO make a twitter bot that tweets a quote from quote.py

import os
import tweepy
from dotenv import load_dotenv
import utils

def api():
    load_dotenv()
    
    api_key = os.environ.get('Api_Key')
    api_secret = os.environ.get('Api_Secret')
    token = os.environ.get('Access_Token')
    token_secret = os.environ.get('Access_Token_Secret')
    
    auth = tweepy.OAuthHandler(
        consumer_key=api_key,
        consumer_secret=api_secret
    )

    auth.set_access_token(token, token_secret)
    
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str):
    api.update_status(message)
    print('Tweeted successfully! ')

def main():
    quote, author = utils.get_quote()
    tweet(api(), f'{quote} ~ {author}')

main()
