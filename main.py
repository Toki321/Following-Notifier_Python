import tweepy
from dotenv import load_dotenv
import os
import time

from getListName import getNewFollows
from substackCheck import isSubstackContained
from telegram import sendMessage

# import keep_alive


# use gorjanilijevski02 (baam) as dev acc


load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token)


idList = []
# idList.append(1449328468227932163) # 0xtoki
# idList.append(1357391943026823168) # gorjan
# idList.append(2966287497) # tetracocf

# idList.append(1456327895866314753)  # @tree_of_alpha
# idList.append(1440614291103571975)  # @BarryFried1
# idList.append(189184866)  # @Fiskantes
# idList.append(1374376169273843716)  # @defi_educator
# idList.append(330533467)  # @phtevenstrong
# idList.append(1424441728770220037)  # @crypto_condom
# idList.append(1297920445979807744)  # @ZoomerOracle
# idList.append(1425645020262977540)  # @blocmatesdotcom
# idList.append(1470955425084235780)  # @rektdiomedes
# idList.append(1249460237913874433)  # @statelayer
# idList.append(1387564294489923584)  # @dexcobra
# idList.append(1347128398427013122)  # @rektfoodfarmer
# idList.append(1480297433020215297)  # @thedefiedge
# idList.append(1356925149581242370)  # @Cov_duk


mainMatrix = []
usernameList = []
index = 0

for id in idList:
  mainMatrix.append(client.get_users_following(id))
  usernameList.append(client.get_user(id=id).data)
  index += 1

def main():
  print("entering main():")
  i = 0
  newFollowingList = []
  for x in mainMatrix:
    print(usernameList[i], " start")
    newFollowingList.append(client.get_users_following(idList[i]))

    toFollow = getNewFollows(mainMatrix[i], newFollowingList[i])
    print("toFollow arr: ", toFollow)

    isContainSubstack = isSubstackContained(toFollow)

    print("in main arr:", isContainSubstack)
    print("Sending messages on Telegram..")
    sendMessage(toFollow, usernameList[i], isContainSubstack)
    print("end messages")

    mainMatrix[i] = newFollowingList[i]

    i += 1
    print("end loop...")

  print("end main.....\n")

# keep_alive.keep_alive()

while True:
  print("Entering while loop.. Follow now"  )
  time.sleep(30)
  main()
