Array = [['', i + 1] for i in range(9)] + [['', -1]]  # 10 slots, linked as free list
startPointer = -1
freePointer = 0

def insert(item):
    global startPointer
    global freePointer

    if freePointer == -1:
        print("List is full")
        return

    new_index = freePointer
    freePointer = Array[new_index][1]

    current = startPointer
    prev = -1
    while current != -1 and Array[current][0] < item:
        prev = current
        current = Array[current][1]

    Array[new_index] = [item, current]

    if prev == -1:
        startPointer = new_index
    else:
        Array[prev][1] = new_index

def delete(item):
    global startPointer
    global freePointer

    if startPointer == -1:
        print("The list is empty")
        return

    current = startPointer
    prev = -1
    while current != -1 and Array[current][0] < item:
        prev = current
        current = Array[current][1]

    if current == -1 or Array[current][0] != item:
        print("Item not found")
        return

    if prev == -1:
        startPointer = Array[current][1]
    else:
        Array[prev][1] = Array[current][1]

    Array[current] = ['', freePointer]
    freePointer = current

def search(item):
    current = startPointer
    while current != -1:
        if Array[current][0] == item:
            print("Item found at position", current)
            return
        current = Array[current][1]
    print("Item not found")
    return

delete(17)
insert(23)
insert(27)
insert(50)
insert(19)
insert(81)
insert(99)
insert(1)
insert(69)
insert(42)
insert(17)
insert(85)
delete(42)
insert(85)
print(Array)
search(69)
search(100)
