import os

monster_collection = []


class Monster():
    def __init__(self):
        self.__id = 0
        self.__Name = ""
        self.__Origin = ""
        self.__Description = ""
        self.__Attack = 0
        self.__Magical_Force = 0
        self.__Magical_Defence = 0
        self.__Defence = 0
        self.__Intelligence = 0
        self.__Health = 0
        self.__Mass = 0

    def monster_setter(self, id, Name, Origin, Description, Attack, Magical_Force, Magical_Defence, Defence,
                       Intelligence, Health, Mass):
        self.__id = id
        self.__Name = Name
        self.__Origin = Origin
        self.__Description = Description
        self.__Attack = Attack
        self.__Magical_Force = Magical_Force
        self.__Magical_Defence = Magical_Defence
        self.__Defence = Defence
        self.__Intelligence = Intelligence
        self.__Health = Health
        self.__Mass = Mass

    def name_getter(self):
        return self.__Name


mymonsters = Monster()


def read_monsters():
    try:
        with (open('Monsters.txt') as file):
            count = 0
            for line in file:
                parts = line.split(",")
                mymonsters.monster_setter(int(parts[0]), parts[1], parts[2], parts[3], int(parts[4]), int(parts[5]),
                                          int(parts[6]), int(parts[7]), int(parts[8]), int(parts[9]), int(parts[10]))
                monster_collection.append(mymonsters)
                print(monster_collection[count].name_getter())
                count = count + 1
    except OSError:
        print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",
              os.getcwd())


read_monsters()
