#oop in python
#to map with real world scenarios,we use objects in code

#class is blueprint for creating objects
#creating class
class Students:
    name="Janvi Yadav"

#creating object
s1=Students()
print(s1.name)

s2=Students()
print(s2.name)

#constructor
class Cars:
    #default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        print("New Cars in the market..")

c1 = Cars("BMW","Black")
print(c1.brand, c1.color)

c2 = Cars("Mercedes","white")
print(c2.brand, c2.color)

#class attribute and object attribute
#object attribute has higher preference than class object
class Students:
    College_name="Ajeenkya DY Patil" #class sttribute , same for every object
    name="none" #use when no name data is given 
    def __init__(self,name,marks):
        self.name=name #object attribute
        self.marks=marks

s1=Students("Janvi",9.33)
s2=Students("Tanushri",9.78)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s1.College_name) 

#methods= functions that belongs to objects
class Students:
    college_name="adypsoe"

    #constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    #methods
    def welcome(self):
        print("welcome,",self.name)

    def get_marks(self): 
        return self.marks

s1=Students("Janvi",9.33)
s1.welcome()
print(s1.get_marks())

#qs1
class Employees:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get_avg(self):
        sum=0
        for val in self.salary:
            sum+=val
        print(e1.name,"Avg salary is,",sum/3)

e1=Employees("Tanushri",[40000,50000,55000])
print(e1.get_avg())

#static methods = methods that dont use self parameter , works at class level
class Students:
    college_name="adypsoe"

    #constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    #static methods
    @staticmethod  #decorator
    def welcome():
        print("welcome")

    def get_marks(self): 
        return self.marks

s1=Students("Janvi",9.33)
s1.welcome()

#ABSTRACTION = hiding unneseccery details and showing only essential information
#ENCAPSULATION = wrapping data and functions into a single unit called object
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        #unnecessery details r hidden
        self.clutch=True 
        self.acc=True
        print("car started..")
        
car1 = Car()
car1.start() #necessery details

#qs2
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.acc_no=acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"Debited feom your acc,",self.acc_no)
        print("Remaining balance is",self.balance)

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"Credited feom your acc,",self.acc_no)
        print("Current balance is",self.balance)

    def get_bal(self):
        print(self.balance)

acc1=Account(40000,12345)
acc1.credit(40000)
acc1.debit(10000)
acc1.get_bal()

#INHERITANCE = when one class (child/derived) inherits the properties of another class (parent/base)
#single inheritance = one child, one parent
#Multi-level inheritance
#multiple inheritance

class Car:
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("car stopped.")

class Bmw(Car):
    def __init__(self,name):
        self.name=name
car1=Bmw("M5")
car2=Bmw("M4")

print(car1.start())
print(car1.stop())

#qs3 multiple inheritance
class A:
    valA="Welcome to class A"

class B:
    valB="Welcome to class B"

class C(A,B):
    valC="Welcome to class C"

c1=C()
print(c1.valA)
print(c1.valB)
print(c1.valC)

#super() method = used to access methods of the parent class
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Bmw(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        self.type=type
        super().start()

car1=Bmw("M5", "electric")
print(car1.type)
