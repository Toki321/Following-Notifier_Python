# Second id: -850874458
import requests
import tweepy
from dotenv import load_dotenv 
import os
import time

load_dotenv()

def sendMessage(hasFollowed, username, isContained):
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    chat_id = "-662738158"
    # username = "tetracocf"
    # hasFollowed = ["0xToki"]
    ii = 0
    for x in hasFollowed:
        if isContained[ii] == 0:
            print("sending message for: ", x)
            message = f"https://twitter.com/{username}"  + " has followed " + f"https://twitter.com/{x}" 
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(url).json()
        ii += 1    
        

    

# sendMessage(hasFollowed, username)