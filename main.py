import tweepy
from dotenv import load_dotenv
import os
import time
from telegram import *
import requests
import keep_alive
from urlCheck import check
import re

# use gorjanilijevski02 (baam) as dev acc

# setting up connection with twitter APi
load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token)

# FUNCTIONS


# Returns a list of usernames from a given array of user objects
def getListName(followingList):
  index = 0
  nameList = []
  for x in followingList.data:
    nameList.append(str(followingList.data[index]))
    index += 1

  return nameList


# Returns the usernames of the new follows
def getNewFollows(oldFollowingList, newFollowingList):
  nameListOld = getListName(oldFollowingList)
  nameListNew = getListName(newFollowingList)

  nameNewFollows = list(set(nameListNew) - set(nameListOld))

  return nameNewFollows


def checkNOTSubstack(string):
    substack = 'substack'
    if substack in string:
        return False
    else:
        return True

def isSubstackContained(usernames):
  stringsubs = "substack"
  isContained = []

  for name in usernames:
    user = client.get_user(username=name, user_fields="entities,description")
    bio = user.data.description
    print("does link exist: ", check(bio))

    try:
      url = user.data.entities["url"]["urls"][0]["expanded_url"]
    except KeyError:
      print(KeyError)
      if check(bio):
        if checkNOTSubstack(bio): #true if no substack link
            isContained.append(0)
        else:
            isContained.append(1)
      else:
        isContained.append(1)
      continue

    except TypeError:
      print(TypeError)
      if check(bio):
        if checkNOTSubstack(bio): #true if no substack link
            isContained.append(0)
        else:
            isContained.append(1)
      else:
        isContained.append(1)
      continue

    if stringsubs in url or stringsubs in bio:
      isContained.append(1)
    else:
      isContained.append(0)

  return isContained


idList = []
# idList.append(1449328468227932163) # 0xtoki
# idList.append(1357391943026823168) # gorjan
# idList.append(2966287497) # tetracocf

idList.append(1456327895866314753)  # @tree_of_alpha
idList.append(1440614291103571975)  # @BarryFried1
idList.append(189184866)  # @Fiskantes
idList.append(1374376169273843716)  # @defi_educator
idList.append(330533467)  # @phtevenstrong
idList.append(1424441728770220037)  # @crypto_condom
idList.append(1297920445979807744)  # @ZoomerOracle
idList.append(1425645020262977540)  # @blocmatesdotcom
idList.append(1470955425084235780)  # @rektdiomedes
idList.append(1249460237913874433)  # @statelayer
idList.append(1387564294489923584)  # @dexcobra
idList.append(1347128398427013122)  # @rektfoodfarmer
idList.append(1480297433020215297)  # @thedefiedge
idList.append(1356925149581242370)  # @Cov_duk

# listFollows1 = client.get_users_following(1357391943026823168)
# listFollows2 = client.get_users_following(2966287497)
# finalList = getNewFollows(listFollows1, listFollows2)
# print(finalList)

mainMatrix = []
usernameList = []

index = 0

for id in idList:
  # print("we re in interation number: ", index)
  mainMatrix.append(client.get_users_following(id))

  usernameList.append(client.get_user(id=id).data)
  # print(usernameList[index])

  # print("does it contain substack: ", containsSubstack)
  # print("url: ", url)
  # print("bio: ", bio)
  index += 1

# print("is contained first array:",isSubstackContained(usernameList))
# print("main matrix : ", mainMatrix)


def main():
  print("entering main():")
  i = 0
  newFollowingList = []
  for x in mainMatrix:
    print(usernameList[i], " start")
    newFollowingList.append(client.get_users_following(idList[i]))

    # print("old list: ", getListName(mainMatrix[i]))
    # print("new list: ", getListName(newFollowingList[i]))

    toFollow = getNewFollows(mainMatrix[i], newFollowingList[i])
    print("toFollow arr: ", toFollow)

    isContainSubstack = isSubstackContained(toFollow)

    print("in main arr:", isContainSubstack)
    print("Sending messages on Telegram..")
    sendMessage(toFollow, usernameList[i], isContainSubstack)
    print("end messages")

    mainMatrix[i] = newFollowingList[i]
    # print("should return new list, if old has become new:")
    # print(getListName(mainMatrix[i]))

    i += 1
    print("end loop...")

  print("end main.....\n")


keep_alive.keep_alive()

while True:
  print("Entering while loop.. Follow now")
  time.sleep(900)
  main()
