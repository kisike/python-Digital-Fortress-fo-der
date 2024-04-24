#class person:
   # name="samsung"

#new_person= person()
#print(new_person.name)

class Person:
    def __init__(self,firstname, lastname,age,origin):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.origin=origin
    def __str__(self):
       return f"{self.firstname} {self.lastname} {self.age} {self.origin}"
    def my_description(self):
        return f" my name {self.firstname} {self.lastname} i am {self.age} and i am from {self.origin}"
    
new_person=Person("ojo", "john",23, "Ogun state")
print (new_person.my_description())
print(new_person)


class Mynew(Person):
    def __init__(self,firstname, lastname,age,origin, serial_number, color):
            super().__init__(firstname, lastname,age,origin,)

            self.serial_number=serial_number
            self.color=color
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.age} {self.origin} {self.serial_number} {self.color}"
        
x=Mynew("tunde","ojo",56,"ede",3452,"red")
print(x)



class Person():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
tunde= Person()
tunde2=iter(tunde)
print(next(tunde))

 


