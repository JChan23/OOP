class CutestCats():
    #Name : STRING
    #Description : STRING
    #Weight : REAL
    #Length : REAL
    #LifeExpectancy : REAL
    #ImageUrl : STRING

    def __init__(self):
        self.__Name = ""
        self.__Description = ""
        self.__Weight = 0.0 #pounds
        self.__Length = 0.0 #cm
        self.__LifeExpectancy = 0.0
        self.__ImageUrl = ""

    def GetCatDetails(self):
        details = []
        details.append(self.__Name)
        details.append(self.__Description)
        details.append(self.__Weight)
        details.append(self.__Length)
        details.append(self.__LifeExpectancy)
        details.append(self.__ImageUrl)
        return tuple(details)

    def GetCatLife(self):
        return (self.__Name, self.__LifeExpectancy)

cat_data = []
def read_file():
    try:
        file = open('CutestCats.txt', "r")
        for line in file:
            pass
    except OSError:
        print("Sorry, could not find the file")


