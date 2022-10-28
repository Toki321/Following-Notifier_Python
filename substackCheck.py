import tweepy
from dotenv import load_dotenv
import os
from urlCheck import check

load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token)


def checkNOTSubstack(string):
    substack = 'substack'
    if substack in string:
        return False
    else:
        return True

    
def isSubstackContained(usernames):
   stringsubs = "substack"
   isContained = []
   str1 = "NFT"
   str2 = "NFTs"

   for name in usernames:
      user = client.get_user(username=name, user_fields="entities,description")
      bio = user.data.description
      print("does link exist: ", check(bio))

      try:
        url = user.data.entities["url"]["urls"][0]["expanded_url"]
      except KeyError:
        print(KeyError)
        if check(bio):
          if checkNOTSubstack(bio):  #true if no substack link
            isContained.append(0)
          else:
            isContained.append(1)
        else:
          isContained.append(1)
        continue

      except TypeError:
        print(TypeError)
        if check(bio):
          if checkNOTSubstack(bio):  #true if no substack link
            isContained.append(0)
          else:
            isContained.append(1)
        else:
          isContained.append(1)
        continue

      if stringsubs in url or stringsubs in bio or str1 in url or str1 in bio or str2 in url or str2 in bio:
        isContained.append(1)
      else:
        isContained.append(0)

   return isContained
