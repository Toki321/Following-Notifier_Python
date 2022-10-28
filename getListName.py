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