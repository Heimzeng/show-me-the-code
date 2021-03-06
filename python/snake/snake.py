import pygame,sys
from pygame.locals import *
from random import randrange
import random
from math import *
import copy

SCREEN_SIZE = (400,400)
BFS_ENABLE = False
DFS_ENABLE = False
ASTAR_ENABLE = True

NEW_METHOD = True

bb = False

class snake():
    """
    a snake can eat food and grow up
    """
    def __init__(self):
        self.s = [(5,5),(5,6),(5,7),(5,8),(5,9)]
        self.direction = (1,0)
        print("snake inited")
    def run(self,key):
        if key=='Up':
            self.direction = (0,-1)
        elif key=='Right':
            self.direction = (1,0)
        elif key == 'Down':
            self.direction = (0,1)
        elif key == 'Left':
            self.direction = (-1,0)
        self.s.pop()
        self.s.insert(0, (self.s[0][0]+self.direction[0],self.s[0][1]+self.direction[1]))
    def grow(self, last1_tail, last2_tail):
        self.s.append(last2_tail)
        self.s.append(last1_tail)
    def getDirection(self):
        if self.direction == (0,-1):
            return 'Up'
        elif self.direction == (1,0):
            return 'Right'
        elif self.direction == (-1,0):
            return 'Left'
        elif self.direction == (0,1):
            return 'Down'

class food():
    """docstring for food"""
    def __init__(self):
        position = (SCREEN_SIZE[0]/10,SCREEN_SIZE[1]/10)
        self.x = randrange(1,position[0],2)
        self.y = randrange(1,position[1],2)
        self.position = (self.x,self.y)
        print("food inited")
    def getPosition(self):
        return self.position
    def newFood(self):
        position = (SCREEN_SIZE[0]/10,SCREEN_SIZE[1]/10)
        self.x = randrange(1,position[0],2)
        self.y = randrange(1,position[1],2)
        self.position = (self.x,self.y)
        print("new food: " + str(self.position))
        return self.position

def getNeibor(node):
    nodelist = []
    if node[0]-2 > 0:
        r = random.randint(0, len(nodelist))
        nodelist.insert(r, (node[0]-2,node[1]))
    if node[0]+2 < SCREEN_SIZE[0]/10:
        r = random.randint(0, len(nodelist))
        nodelist.insert(r, (node[0]+2,node[1]))
    if node[1]-2 > 0:
        r = random.randint(0, len(nodelist))
        nodelist.insert(r, (node[0],node[1]-2))
    if node[1]+2 < SCREEN_SIZE[1]/10:
        r = random.randint(0, len(nodelist))
        nodelist.insert(r, (node[0],node[1]+2))
    return nodelist

def BFS(head,body,end):
    queue = []
    visited = []
    path = []
    parent = [[(0,0) for i in range(1,int(SCREEN_SIZE[0]))]for j in range(1,int(SCREEN_SIZE[1]))]
    queue.append(head)
    if head == fd.getPosition():
        head = body[0]
        end = body[-1]
        body = body[:-1]
    if end == sk.s[-1]:
        body = body[:-1]
    while queue!=[]:
        current = queue[0]
        if (current == end):
            path.insert(0,current)
            while parent[current[0]][current[1]]!=head:
                current = parent[current[0]][current[1]]
                path.insert(0,current)
            path.insert(0,parent[current[0]][current[1]])
            break
        currentcopy = (current[0], current[1])
        path_maybe = []
        if currentcopy != head:
            path_maybe.insert(0,currentcopy)
            while parent[currentcopy[0]][currentcopy[1]]!=head:
                currentcopy = parent[currentcopy[0]][currentcopy[1]]
                path_maybe.insert(0,currentcopy)
            path_maybe.insert(0,parent[currentcopy[0]][currentcopy[1]])
        level = len(path_maybe) - 1
        print(head, end, fd.getPosition(), path_maybe)

        newpath = path_maybe[::-1]
        newnewpath = []
        for i in range(len(newpath)-1):
            newnewpath.append(newpath[i])
            newnewpath.append((int((newpath[i][0] + newpath[i+1][0] )/ 2), int((newpath[i][1] + newpath[i+1][1] )/ 2)))
        if len(newpath) > 0:
            newnewpath.append(newpath[-1])
        newnewpath[len(newnewpath):] = body[1:]
        newbody = newnewpath[0:(len(body))]

        neibor = getNeibor(current)
        for items in neibor:
            if items not in newbody and items not in visited:
                queue.append(items)
                visited.append(items)
                parent[items[0]][items[1]] = current
        visited.append(current)
        queue.pop(0)

    return path
def DFS(current,visited,parent):
    end = fd.getPosition()
    if (current == end):
        path = []
        path.insert(0,current)
        while parent[current[0]][current[1]]!=sk.s[0]:
            current = parent[current[0]][current[1]]
            path.insert(0,current)
        path.insert(0,parent[current[0]][current[1]])
        print (path)
        return path
    neibor = getNeibor(current)
    cou = 0
    for items in neibor:
        if items not in sk.s and items not in visited:
            cou += 1
    if cou == 0:
        return DFS(parent[current[0]][current[1]],visited,parent)
    else:
        for items in neibor:
            if items not in sk.s and items not in visited:
                visited.append(items)
                parent[items[0]][items[1]] = current
                return DFS(items,visited,parent)

def jj(path, end):
    if ASTAR_ENABLE or BFS_ENABLE or DFS_ENABLE:
        if len(path) == 0:
            print("path not work1")
            return False
        newpath = path[::-1]
        print("new1", newpath)
        newnewpath = []
        for i in range(len(newpath)-1):
            newnewpath.append(newpath[i])
            newnewpath.append((int((newpath[i][0] + newpath[i+1][0] )/ 2), int((newpath[i][1] + newpath[i+1][1] )/ 2)))
        newnewpath.append(newpath[-1])
        print("newnewpath: ", newnewpath)
        newnewpath[len(newnewpath):] = sk.s[1:]
        print("new2", newnewpath)
        newbody = newnewpath[0:(len(sk.s)+2)]
        if end != fd.getPosition():
            newbody.pop()
            newbody.pop()
        print("newbody: ", newbody)
        pathcpl = BFS(end,newbody, newbody[-1])
        # print("food: ", fd.getPosition())
        print ("pathcpl: ", pathcpl)
        print("newbody", newbody)
        if len(pathcpl) == 0:
            print("path not work")
            return False
            #getPath()
            # numbercount = 0
            # path = BFS(sk.s[0], sk.s, sk.s[-1])
            # istracetail = True
            # print("newpath", path)
        else:
            return True

def AStar():
    queue = []
    path = []
    visited = [sk.s[0]]
    parent = [[(0,0) for i in range(1,int(SCREEN_SIZE[0]))]for j in range(1,int(SCREEN_SIZE[1]))]
    queue.append(sk.s[0])
    end = fd.getPosition()

    snakecopy = copy.deepcopy(sk)
    print("body: " + str(sk.s))
    while queue!=[]:
        current = queue[0]
        if (current == end):
            path.insert(0,current)
            while parent[current[0]][current[1]]!=snakecopy.s[0]:
                current = parent[current[0]][current[1]]
                path.insert(0,current)
            path.insert(0,parent[current[0]][current[1]])
            break
        neibor = getNeibor(current)
        less = 999999
        index = -1
        for i in range(0,len(neibor)):
            if neibor[i] not in snakecopy.s and neibor[i] not in visited:
                if ((neibor[i][0]-end[0])**2+(neibor[i][1]-end[1])**2)<=less:
                    index = i
                    less = (neibor[i][0]-end[0])**2+(neibor[i][1]-end[1])**2
        if index != -1:
            queue.append(neibor[index])
            visited.append(neibor[index])
            print("visited: " + str(visited))
            parent[neibor[index][0]][neibor[index][1]] = current
        else:
            print("index -1 1, size: " + str(len(neibor)))
            # print("visited: " + str(visited))
        queue.pop(0)
    if len(path) == 0 or jj(path, end) == False:
        mmm = 0
        index = -1
        neibor = getNeibor(sk.s[0])
        ll = []
        for i in range(0,len(neibor)):
            if neibor[i] not in sk.s:
                pp = []
                pp.insert(0, neibor[i])
                pp.insert(0, sk.s[0])
                if jj(pp, neibor[i]) == True:
                    ll.append(neibor[i])
        for i in range(0,len(ll)):
            if ((ll[i][0]-end[0])**2+(ll[i][1]-end[1])**2)>=mmm:
                index = i
                mmm = (ll[i][0]-end[0])**2+(ll[i][1]-end[1])**2
        if index != -1:
            path.insert(0, ll[index])
            path.insert(0, sk.s[0])
            global bb
            bb = True
            print("index not -1 2")
        else:
            print("index -1 2")
    return path



def getPath():
    if BFS_ENABLE:
        path = BFS(sk.s[0],sk.s, fd.getPosition())
    elif DFS_ENABLE:
        path = DFS(sk.s[0],[sk.s[0]],[[(0,0) for i in range(1,int(SCREEN_SIZE[0]))]for j in range(1,int(SCREEN_SIZE[1]))])
    elif ASTAR_ENABLE:
        path = AStar()
    
    print("path: ", path)
    return path
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.mouse.set_visible(0)
    screentitle = pygame.display.set_caption('snake')
    clock = pygame.time.Clock()
    fd = food()
    sk = snake()
    key = 'Right'
    run = True

    numbercount = 0
    istracetail = False
    target = []
    if BFS_ENABLE or DFS_ENABLE or ASTAR_ENABLE:
        path = getPath()

    while run:
        skrect = []
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if sk.getDirection()!='Down':
                        key = 'Up'
                if event.key == pygame.K_DOWN:
                    if sk.getDirection()!='Up':
                        key = 'Down'
                if event.key == pygame.K_LEFT:
                    if sk.getDirection()!='Right':
                        key = 'Left'
                if event.key == pygame.K_RIGHT:
                    if sk.getDirection()!='Left':
                        key = 'Right'
        screen.fill((0,0,0))
        fdrect = pygame.draw.circle(screen,(255,255,255),(fd.getPosition()[0]*10,fd.getPosition()[1]*10),5,2)
        for block in sk.s:
            skrect.append(pygame.draw.rect(screen,(255,255,255),(block[0]*10-5,block[1]*10-5,10,10)))
        if istracetail == True:
            target.append(sk.s[-1])
            istracetail = False
        if bb == True:
            bb = False
            print("bbTrue")
            path = getPath()
            numbercount = 0
        if fdrect.colliderect(skrect[0]):
            sk.grow(last1_tail, last2_tail)
            while True:
                if fd.newFood() not in sk.s:
                    if BFS_ENABLE or DFS_ENABLE or ASTAR_ENABLE:
                        path = getPath()
                    numbercount = 0
                    break
        if len(target) > 0:
            if target[0] == sk.s[0]:
                if BFS_ENABLE or DFS_ENABLE or ASTAR_ENABLE:
                    path = getPath()
                numbercount = 0
                target = []
        pygame.display.update()
        numbercount = numbercount + 1
        if clock.tick(100):
            # print("thispath: ", path)
            print(numbercount)
            if (BFS_ENABLE or DFS_ENABLE or ASTAR_ENABLE) and numbercount < len(path):
                if (path[numbercount][0]-path[numbercount-1][0],path[numbercount][1]-path[numbercount-1][1]) == (0,2):
                    key = 'Down'
                elif (path[numbercount][0]-path[numbercount-1][0],path[numbercount][1]-path[numbercount-1][1]) == (0,-2):
                    key = 'Up'
                elif (path[numbercount][0]-path[numbercount-1][0],path[numbercount][1]-path[numbercount-1][1]) == (-2,0):
                    key = 'Left'
                elif (path[numbercount][0]-path[numbercount-1][0],path[numbercount][1]-path[numbercount-1][1]) == (2,0):
                    key = 'Right'
            last1_tail = sk.s[-1]
            last2_tail = sk.s[-2]
            sk.run(key)
            sk.run(key)
        
        if sk.s[0][0]*10-5 < -10 or sk.s[0][1]*10-5 < -10 or sk.s[0][0] > SCREEN_SIZE[0]/10 -1 or sk.s[0][1] > SCREEN_SIZE[1]/10 -1:
            run = False
            print("kaka")
            break
        count = len(skrect) - 1
        while count > 1 and run:
            if skrect[0].colliderect(skrect[count-1]):
                print("kaka2")
                run = False
                break
            count -= 1
    sys.exit()