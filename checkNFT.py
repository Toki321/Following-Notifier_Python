import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token)


def checkStringForNft(string):  #true if there is nft word, false if not
  str1 = "nfts"
  str2 = "nft"
  str3 = "NFT"
  str4 = "NFTs"

  if str1 in string or str2 in string or str3 in string or str4 in string:
    return True
  else:
    return False


def checkNftUsernamers(
    oneAccount
):  #false if no NFT, true if there is NFT word in username / name

  user = client.get_user(username=oneAccount)
  username = user.data
  fullName = user.data["name"]

  if checkStringForNft(username) or checkStringForNft(fullName):
    return True
  else:
    return False
