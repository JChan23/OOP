class Employee:
    #self.__HourlyPay REAL
    #self.__EmployeeNumber STRING
    #self.__JobTitle STRING

    def __init__(self, pay, ID, title):
        self.__HourlyPay = pay
        self.__EmployeeNumber = ID
        self.__JobTitle = title
        self.__PayYear2022 = [] #array of 52 elements of type REAL
        for i in range(52):
            self.__PayYear2022.append(0.00)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNum, HoursWorked):
        TotalPay = self.__HourlyPay*HoursWorked
        self.__PayYear2022[WeekNum-1] = TotalPay

    def GetTotalPay(self):
        return sum(self.__PayYear2022)


class Manager(Employee):
    #self.__BonusValue REAL

    def __init__(self, pay, ID, title, bonus):
        Employee.__init__(pay, ID, title)
        self.__BonusValue = bonus

    def SetPay(self, WeekNum, HoursWorked):
        HoursWorked = HoursWorked*(1+(self.__BonusValue/100))
        self.SetPay(WeekNum, HoursWorked)
