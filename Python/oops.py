class Car:
    def __init__(self,name,color,price) :
        self.name = name
        self.color = color
        self.price = price

    def start(self):
        print(self.name + " engine started ")

p1 = Car("Maruthi","Red",10000)
p2 = Car("Tata","white",20000)
print(p1.name,p1.color,p1.price)
print(p2.name,p2.color,p2.price)
p1.start()



class Person:
     def __init__(self,nam,numb):
        self.nam=nam
        self.numb=numb
     def address(self):
        print(self.nam, self.numb);
class Doctor(Person):
    pass
class Paient(Person):
    pass
Doc = Doctor("Ajax",223333)
Pat = Paient("Shibu",983742)

Doc.address()
Pat.address()


class Names:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def join(self):
        print(self.firstname, self.lastname)
class Verification(Names):
    pass
first = Verification("Jibi","Thomas")
first.join()