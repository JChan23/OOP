import os

class Monster:
    def __init__(self, id, Name, Origin, Description, Attack, Magical_Force, Magical_Defence, Defence, Intelligence, Health, Mass):
        self.id = id
        self.Name = Name
        self.Origin = Origin
        self.Description = Description
        self.Attack = Attack
        self.Magical_Force = Magical_Force
        self.Magical_Defence = Magical_Defence
        self.Defence = Defence
        self.Intelligence = Intelligence
        self.Health = Health
        self.Mass = Mass

    def __repr__(self):
        return self.Name

    def name_getter(self):
        return self.Name

monster_collection = []
def read_monsters():
    try:
        with (open('Monsters.txt') as file):
            for line in file:
                parts = line.split(",")
                monster_collection.append(Monster(int(parts[0]),parts[1],parts[2],parts[3],int(parts[4]),int(parts[5]),int(parts[6]),int(parts[7]),int(parts[8]),int(parts[9]),int(parts[10])))
    except OSError:
        print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())


read_monsters()
for i in range(len(monster_collection)):
    print(monster_collection[i].name_getter())
