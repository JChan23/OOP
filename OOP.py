import random

class Character:
    def __init__(self):
        self.name = ""
        self.attack = random.randint(0, 100)
        self.defence = random.randint(0, 100)
        self.health = random.randint(0, 100)
        self.experience = 0

    def print_basics(self):
        print("Name:       ",self.name)
        print("Attack:     ",self.attack)
        print("Defence:    ",self.defence)
        print("Health:     ",self.health)
        print("Experience: ",self.experience)

    def print_me(self):
        self.print_basics()

    def print_intro(self):
        print("This is an exciting story!")

class Wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.magic = random.randint(0, 100)

    def print_me(self):
        self.print_basics()
        print("Magic:      ",self.magic)

class Knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.armour = random.randint(0, 100)

    def setter(self, name):
        self.name = name
        self.attack = random.randint(0, 50)
        self.defence = random.randint(0, 50)
        self.__health = random.randint(0, 50)
        self.armour = 30

    def health_getter(self):
        return self.__health

    def print_me(self):
        self.print_basics()
        print("armour ", self.armour)

    class weapon:
        def attack(self):
            print('Sword')


Alex = Character()
Alex.name = "Alex"
Alex.print_me()

Shunto = Wizard()
Shunto.name = "Shunto"
Shunto.print_me()

Ayaan = Knight()
Ayaan.name = "Ayaan"
Ayaan.print_me()

print(vars(Shunto))
