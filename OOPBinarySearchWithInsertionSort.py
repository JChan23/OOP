class Person:
    def __init__(self, n, a):
        self.__name = n
        self.__age = a

    def NameGetter(self):
        return self.__name

    def AgeGetter(self):
        return self.__age

People = [
    Person("Frank", 28),
    Person("Ivy", 26),
    Person("Charlie", 40),
    Person("Alice", 30),
    Person("Jack", 38),
    Person("David", 22),
    Person("Emma", 35),
    Person("Hank", 45),
    Person("Bob", 25),
    Person("Grace", 33),
]

#sort people alphabetically
def insertionSort(alist):
    for i in range(1, len(alist)):
        position = i - 1
        currentvalue = alist[i]
        currentname = alist[i].NameGetter()
        while position >= 0 and alist[position].NameGetter() > currentname:
            alist[position+1] = alist[position]
            position = position - 1
        alist[position+1] = currentvalue

def binarysearch(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (high+low)//2
        if array[mid].NameGetter() == target:
            return mid
        elif array[mid].NameGetter() < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

insertionSort(People)
item = input('Enter a person to search for in the array: ')
result = binarysearch(People, item)
if result == -1:
    print("Can't Find it!")
else:
    print("Found it at position", result)
