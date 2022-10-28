import requests
from dotenv import load_dotenv
import os
from checkNFT import checkNftUsernamers


load_dotenv()

def sendMessage(hasFollowed, username, isContained):
  TOKEN = os.getenv("TELEGRAM_TOKEN")
  chat_id = "-662738158"
  ii = 0
  for x in hasFollowed:
    if isContained[ii] == 0:
      if checkNftUsernamers(x) == False:
        print("sending message for: ", x)
        message = f"https://twitter.com/{username}" + " has followed " + f"https://twitter.com/{x}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()
    ii += 1


