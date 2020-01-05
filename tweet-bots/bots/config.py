import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("yOFrLYJZ9hyTJtQT3NxbT2yUK")
    consumer_secret = os.getenv("0RbjOnqEBnMbKjGfgDYeWulqBhipShe35i4q3S55Nq2J5TBvIF")
    access_token = os.getenv("1064994930404274178-DbqZy5BwUJCshvLuuSFaYE7GHpiYbA")
    access_token_secret = os.getenv("68k5WeFwKBzCm2dsnVodR3Z1JTEC1wnugDCWOph1hwh6o")
    #consumer_key = "yOFrLYJZ9hyTJtQT3NxbT2yUK" #APIkey
    #consumer_secret = "0RbjOnqEBnMbKjGfgDYeWulqBhipShe35i4q3S55Nq2J5TBvIF"#Apisecrectkey
    #access_token="1064994930404274178-DbqZy5BwUJCshvLuuSFaYE7GHpiYbA"
    #access_token_secret = "68k5WeFwKBzCm2dsnVodR3Z1JTEC1wnugDCWOph1hwh6o"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api