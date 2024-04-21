class Car:
    def __init__ (self,name, brand):
        self.name=name
        self.brand=brand
    def tunde (self):
        return f"the name of my car is {self.name} and the brand is {self.brand}"
    
class Phone:
    def __init__ (self,name, brand):
        self.name=name
        self.brand=brand
    def tunde (self):
        return f"the name of my phone is {self.name} and the brand is {self.brand}"
class School:
    def __init__ (self,name, brand):
        self.name=name
        self.brand=brand
    def tunde (self):
        return f"the name of my shool is {self.name} and the class is {self.brand}"
My_car=Car("toyota", "mg5")
myphone=Phone("samsang","urt5")
myschool=School ("unijos", "jos")
for make in (My_car,myphone,myschool):
    print(make.tunde())