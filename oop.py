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
