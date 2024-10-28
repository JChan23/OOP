import random

Joke_array = []
def read_file():
    try:
        with open('DadJokes.txt') as file:
            for line in file:
                Joke_array.append(line.strip())
    except OSError:
        print("Sorry, could not find the file")
read_file()

class Jokes():
    def __init__(self):
        self.__prompt = ""
        self.__answer = ""

    def joke_setter(self):
        random_num = (random.randint(0, len(Joke_array)//2))*2
        self.__prompt = Joke_array[random_num]
        self.__answer = Joke_array[random_num+1]

    def prompt_getter(self):
        return self.__prompt

    def answer_getter(self):
        return self.__answer

joke = Jokes()
joke.joke_setter()
print(joke.prompt_getter())
input("Answer: ")
print(joke.answer_getter())
