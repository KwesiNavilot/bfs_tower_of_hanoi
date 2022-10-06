#Assignment submitted by Andrews Kwesi Ankomahene (PS/MCS/21/0008)'
from copy import deepcopy

class Node:
  def __init__(self):
    self.state = [[],[],[]]
    self.nodeNumber = 0
    self.status = 'idle'
    self.neighbours = []
    self.parent = None
    self.children = []
    self.point = 10


def evalFunc(node):
    largestDisk = 0
    diskList=[]

    for peg in initialState:
        if len(peg) > 0:
            diskList.append(max(peg))
    
    # get largest item in set
    largestDisk = max(diskList)
    
    # print largestDisk node
    node.point = 10

    setPnts(node, largestDisk)

def setPnts(node, largestDisk):
    global finalState
    # print '\n starting setpnts with largestDisk= ',largestDisk,' nodestate=',node.state
    if largestDisk>0:
        for fpeg in finalState:
            if largestDisk in fpeg:
                
                # get the final positionition
                position = finalState.index(fpeg)

                #print largestDisk, 'the largestDisk is on peg no ', position ,fpeg,' in finalstate. finalstate[position]='#,finalstate[position]
                if largestDisk in node.state[position]:
                    # print largestDisk, 'the largestDisk is on peg no ', position ,' in node.state. node.state[position]=',node.state[position]
                    # print 'reducing point from ', node.point, ' to ', (node.point-1)
                    node.point = node.point - 1

                    # print 'starting recursive with largestDisk as ', largestDisk-1
                    setPnts(node,largestDisk-1)

def move(st1,st2):
    s1 = st1[:]

    s2 = st2[:]

    if len(s1) > 0:
        topDisc = s1[len(s1)-1]
        lastofS2 = len(s2)-1

        if len(s2) == 0 or s2[lastofS2] > topDisc:
            s2.append(topDisc)
            s1.pop()

            return s1, s2
        else:
            return None
    else:
        return None


def moveDisc(n):
    global noOfPegs

    stacks = []

    for x in range(0, noOfPegs):
        for y in range(0,noOfPegs):

            stacks = move(n.state[x],n.state[y])

            if stacks!= None:
                # print 'states after move', states
                nextNode = Node()
                nextNode = deepcopy(n)
                nextNode.state[x]= deepcopy(stacks[0])
                nextNode.state[y]= deepcopy(stacks[1])

                # print 'states', states
                # print '\n'
                # print 'next node',nextNode.state
                if nextNode.state  in states:
                    #print 'nextNode in states'
                    a=1
                else:
                    nodenumber = nextNode.nodeNumber

                    # print nextNode.state, 'next not in states'
                    states.append(nextNode.state)

                    return nextNode
    #print 'DEAD END'
    return None

def printPath(node):
    print('\nTracing back the Path')
    while True:
        print('Node number: ', node.nodeNumber,'  State:  ', node.state)

        if node.parent != None:
            node = node.parent
        else:
            break


def breathFirstSearch(node):
    global parentList, nodeNumber, childList, targetFound, step

    print ('\n STEP : ', step)

    step+=1

    for node in parentList:
        if targetFound == False :
            print ('Parent Node:', node.nodeNumber,' State :', node.state)
            exhausted = False
            parent = deepcopy(node)

            counter = 1
            while exhausted==False :

                counter += 1
                childNode = moveDisc(node)

                if childNode != None:
                    nodeNumber += 1

                    childNode.nodeNumber = nodeNumber
                    childNode.parent=node
                    parent.children.append(childNode)
                    childList.append(childNode)

                    print ('Child Node:',childNode.nodeNumber,'State:', childNode.state)

                    #print 'states', states
                    if childNode.state==finalState:
                        print ('\nFinal target reached')
                        print("Number of nodes expanded is ", childNode.nodeNumber)
                        printPath(childNode)

                        targetFound = True
                else:
                    exhausted = True

    parentList = deepcopy(childList)

    childList = []

    if targetFound == False :
        breathFirstSearch(parentList)


def readState():
    global noOfPegs
    state=[]

    for x in range(0, noOfPegs):
        print ('Discs in Peg', x+1, ' : ',)
        a = [int(x) for x in input().split()]
        state.append(a)

    return state


# FIRE THE APPLICATION
noOfPegs=3

print ('\nWelcome To Tower of Hanoi using breathFirstSearch')
print('\nInstructions for input:') 
print('-->An example input for discs in a peg >>> 3 2 1')
print( '-->This means your peg have 3 discs with disc of size 3 at bottom and disc of size 1 at top')
print( '-->If the peg is empty, just click ENTER; Do not input anything in that case')

noOfPegs = int(input("\nEnter number of pegs--> "))

print('\nEnter details for initial State') 
initialState = readState()
print('\nEnter details for final State') 
finalState = readState()

print ('\nInitial state: ',initialState)
print ('Final states: ',finalState)

# set initial states
states = []

nodeNumber = 1
time = 1
targetFound = False

node = Node()
node.state = initialState
node.nodeNumber = nodeNumber
parentList = [node]
childList = []
targetFound = False
largestDiskInTarget = False

step = 1

parentList = [node]
childList = []

breathFirstSearch(node)