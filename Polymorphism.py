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
