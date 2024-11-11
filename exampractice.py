class node:
    def __init__(self, D, N):
        self.data = D
        self.nextNode = N

linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
startPointer = 0
emptyList = 5

def outputNodes(array, spointer):
    while spointer != -1:
        print(array[spointer].data)
        spointer = array[spointer].nextNode

#outputNodes(linkedList, startPointer)

def addNode(array, spointer, epointer):
    if epointer < 0 or epointer > 9:
        return False
    data = int(input("Data to be added to linked list: "))
    new_node = node(data, -1)
    array[epointer] = new_node

    previous_pointer = 0
    while spointer != -1:
        previous_pointer = spointer
        spointer = array[spointer].nextNode
    array[previous_pointer].nextNode = epointer
    epointer = array[epointer].nextNode
    return True

outputNodes(linkedList, startPointer)
if addNode(linkedList, startPointer, emptyList) == False:
    print("List is full")
else:
    print("Item added successfully")
outputNodes(linkedList, startPointer)

