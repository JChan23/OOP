class Wrexham():
    #PlayerNumber : STRING
    #Forename : STRING
    #Surname : STRING
    #Position : STRING
    #CommunityInvolvement : REAL
    #Injured : BOOLEAN

    def __init__(self, Pnumber, Fname, Sname, Pos):
        self.__PlayerNumber = Pnumber
        self.__Forename = Fname
        self.__Surname = Sname
        self.__Position = Pos
        self.__CommunityInvolvement = 0.0
        self.__Injured = False

    def GetPlayerInfo(self):
        return (self.__Forename, self.__PlayerNumber)

    def GetCommunityInvolvement(self):
        return self.__CommunityInvolvement

    def GetInjured(self):
        return self.__Injured

    def ChangeCommunityInvolvement(self, change):
        self.__CommunityInvolvement = self.__CommunityInvolvement + change

    def ChangeInjured(self):
        self.__Injured = not self.__Injured

player_data = []
def read_file():
    try:
        file = open('wrexham.txt', "r")
        count = 0
        for line in file:
            if count % 4 == 0:
                number = line.split()
            elif count % 4 == 1:
                first_name = line.split()
            elif count % 4 == 2:
                last_name = line.split()
            elif count % 4 == 3:
                position = line.split()
                player_data.append(Wrexham(number, first_name, last_name, position))
            count = count + 1
    except OSError:
        print("Sorry, could not find the file")
read_file()

print(player_data[0].GetPlayerInfo())
player_data[0].ChangeCommunityInvolvement(100)
print(player_data[0].GetCommunityInvolvement())
player_data[0].ChangeCommunityInvolvement(50.25)
print(player_data[0].GetCommunityInvolvement())

print(player_data[1].GetPlayerInfo())
player_data[1].ChangeInjured()
print(player_data[1].GetInjured())
player_data[1].ChangeInjured()
print(player_data[1].GetInjured())
