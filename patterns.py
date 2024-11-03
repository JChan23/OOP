import turtle

class pattern():
    #angle as integer
    #times as integer

    def __init__(self, a, t):
        self.__angle = a
        self.__times = t

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.speed(0)
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()

pattern_data = []
def read_file():
    try:
        with open('patterns.txt') as file:
            for line in file:
                pattern_data.append(int(line.strip()))
    except OSError:
        print("Sorry, could not find the file")

read_file()
for i in range(5):
    mypattern = pattern(pattern_data[2*i], pattern_data[2*i+1])
    mypattern.draw_pattern()
