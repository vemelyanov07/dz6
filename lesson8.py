class Student1:
    firstName = "Ivan"
    lastName = "Ivanov"
    groupNumbers = "03-14"
    age = 25
    
    def getFullName(self):
        print(f"Полное имя студента: {self.firstName} {self.lastName}")
    def getAge(self):
        print(f"Возраст студента: {self.age}")
    def getGroupMumber(self):
        print(f"Номер группы студента: {self.groupNumbers}")
    

a = Student1()
a.getFullName(), a.getAge(), a.getGroupMumber()


class Student2:
    firstName = "Vasia"
    lastName = "Vasiliev"
    groupNumbers = "04-14"
    age = 24
    
    def getFullName(self):
        print(f"Полное имя студента: {self.firstName} {self.lastName}")
    def getAge(self):
        print(f"Возраст студента: {self.age}")
    def getGroupMumber(self):
        print(f"Номер группы студента: {self.groupNumbers}")
    
    
    
a = Student2()
a.getFullName(), a.getAge(), a.getGroupMumber()


class Student3:
    firstName = "Petr"
    lastName = "Petrov"
    groupNumbers = "05-14"
    age = 26
    
    def getFullName(self):
        print(f"Полное имя студента: {self.firstName} {self.lastName}")
    def getAge(self):
        print(f"Возраст студента: {self.age}")
    def getGroupMumber(self):
        print(f"Номер группы студента: {self.groupNumbers}")

a = Student3()
a.getFullName(), a.getAge(), a.getGroupMumber()


class Student4:
    firstName = "Igor"
    lastName = "Igorevich"
    groupNumbers = "02-14"
    age = 22
    
    def getFullName(self):
        print(f"Полное имя студента: {self.firstName} {self.lastName}")
    def getAge(self):
        print(f"Возраст студента: {self.age}")
    def getGroupMumber(self):
        print(f"Номер группы студента: {self.groupNumbers}")

a = Student4()
a.getFullName(), a.getAge(), a.getGroupMumber()


class Student5:
    firstName = "Makar"
    lastName = "Makarevich"
    groupNumbers = "01-14"
    age = 25
    
    def getFullName(self):
        print(f"Полное имя студента: {self.firstName} {self.lastName}")
    def getAge(self):
        print(f"Возраст студента: {self.age}")
    def getGroupMumber(self):
        print(f"Номер группы студента: {self.groupNumbers}")

a = Student5()
a.getFullName(), a.getAge(), a.getGroupMumber()

class Student6:
    def __init__(self, firstName, lastName, groupNumbers):
        self.name = firstName
        self.lastName = lastName
        self.groupNumbers = groupNumbers
        
    def setNameAge(self):
        print(f"Полное имя студента: {self.name} {self.lastName}")
    def setGroupMumber(self):
        print(f"Номер группы студента: {self.groupNumbers}")
        
a = Student6("Петя", "Иванов", "08-14")
print(a.name, a.lastName, a.groupNumbers)




from abc import ABC, abstractmethod

class milk(ABC):
    color = "white"
    blond = 2
    fatpercentage = 5
    
    def characteristicprod(self):
        print(f"Продукт белого цвета, в котором процент белка составляет {self.blond}%, с долей жира {self.fatpercentage}%")

    @abstractmethod
    def characteristicprod2(self):
        pass
    
class product(milk):
    def characteristicprod2(self):
        print("Сроком годности на 14 суток.")

class yogurt(product):
    def characteristicprod3(self):
        print("Вкус второго продукта отличается от первого.")
           
class kefir(yogurt):
    def characteristicprod4(self):
        print("Вкус третьего продукта отличается от первого и второго.")

P1 = kefir()
P1.characteristicprod()
P1.characteristicprod3()
P1.characteristicprod4()
P2 = product()
P2.characteristicprod2()