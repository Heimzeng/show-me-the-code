

def AStarFindPath(begin, destinations, mapNodes, blackList):
    # data error
    if begin not in mapNodes or destinations not in mapNodes or begin in blackList or begin in blackList:
        print("data error")
        return
    openSet = []
    closedSet = []
    