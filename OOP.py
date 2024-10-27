import random

class Character:
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.__health = 0
        self.experience = 0

    def print_basics(self):
        print("\nName:       ",self.name)
        print("Attack:     ",self.attack)
        print("Defence:    ",self.defence)
        print("Health:     ",self.__health)
        print("Experience: ",self.experience)

    def setter(self, name):
        self.name = name
        self.attack = random.randint(0, 50)
        self.defence = random.randint(0, 50)
        self.__health = random.randint(30, 50)

    def health_getter(self):
        return self.__health

    def print_me(self):
        self.print_basics()


class Wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.magic = 30

    def print_me(self):
        self.print_basics()
        print("Magic:      ",self.magic)

class Knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.armour = 30

    def print_me(self):
        self.print_basics()
        print("Armour:     ", self.armour)


character_name = input("What is your name? ")
chracter_class = input("Would you like to be a Wizard or Knight? W or K: ")

if chracter_class.upper() == "K":
    print("You are now a knight")
    player = Knight()
elif chracter_class.upper() == "W":
    print("You are now a wizard")
    player = Wizard()
else:
    print("No class selected. Default character created for you")
    player = Character()

player.setter(character_name)
player.print_me()
