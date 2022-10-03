import tweepy
from dotenv import load_dotenv 
import os
import time
from telegram import *
import requests

# setting up connection with twitter APi
load_dotenv()
bearer_token=os.getenv("BEARER_TOKEN")
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


def isSubstackContained(usernames):
    stringsubs = "substack"
    isContained = []

    for name in usernames:
        user = client.get_user(username=name, user_fields="entities,description")
        bio = user.data.description

        try:
            url = user.data.entities["url"]["urls"][0]["expanded_url"]  
        except KeyError:
            # print(KeyError)
            isContained.append(0)
            continue

        except TypeError:
            # print(TypeError)
            isContained.append(0)
            continue

        if stringsubs in url or stringsubs in bio:
            isContained.append(1)
        else:
            isContained.append(0)
    
    return isContained

idList = []
# idList.append(1449328468227932163) # 0xtoki
# # idList.append(1357391943026823168) # gorjan
# idList.append(2966287497) # tetracocf

idList.append(1485029520029765633) # @ghost93_x 1485029520029765633  
idList.append(1419715399713689606 ) # @smolcalls 1419715399713689606  
idList.append(1435224897299550217) # @ladyofcrypto1 1435224897299550217
idList.append(971586956)           # @jediblocmates  
idList.append(1401346770458669057) # @apeocloc
idList.append(1333380787505393665) # @sgallardo_9 
idList.append(1434717709464309761)  # @hpmex1 
idList.append(784068635958644736)  # @cryptodetweiler 
idList.append(1336191614356742144) # @tervoooo
idList.append(1511275956073287683) # @DegenSensei
idList.append(1397450323963252739) # @wassiecapital
idList.append(1353461821714403329) # @JoshTheMoonMan
idList.append(972290223316045824)  # @burstingbagel
idList.append(996294856078188544)  # @MacnBTC

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
    # print("entering main():")
    i = 0
    newFollowingList = []
    for x in mainMatrix:
        print(usernameList[i]," start")
        newFollowingList.append(client.get_users_following(idList[i]))

        # print("old list: ", getListName(mainMatrix[i]))
        # print("new list: ", getListName(newFollowingList[i]))

        toFollow = getNewFollows(mainMatrix[i], newFollowingList[i])
        # print("toFollow arr: ", toFollow)

        isContainSubstack = isSubstackContained(toFollow)
        
        # print("in main arr:", isContainSubstack)
        # print("Sending messages on Telegram..")
        sendMessage(toFollow, usernameList[i], isContainSubstack)
        # print("end messages")

        mainMatrix[i] = newFollowingList[i]
        # print("should return new list, if old has become new:")
        # print(getListName(mainMatrix[i]))

        i += 1
        # print("end loop...")

    # print("end main.....\n")



while True:
    # print("Entering while loop.. Follow now")
    time.sleep(910)
    main()
    
        
    
     
