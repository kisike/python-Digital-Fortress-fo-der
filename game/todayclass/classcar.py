class car:
    def __init__(self,name,make, year,color,origin):
        self.name=name
        self.make=make
        self.year=year
        self.color=color
        self.origin=origin
    def __str__(self):
       return f"{self.name} {self.make} {self.year} {self.color} {self.origin}"
   # def my_description(self):
        #return f" m,y name {self.firstname} {self.lastname} i am {self.age} and i am from {self.origin}"
    
new_car=car("ojo", "ivm",2024, "grey" "Nig")
print (new_car)


class mybus(car):
    def __init__(self,name,make, year,color,origin, size, type):
        super().__init__(self,name,make, year,color,origin)

        self.size=size
        self.type=type
    def __str__(self):
        return f"{self.name} {self.make} {self.year} {self.color} {self.origin} {self.size} {self.type}"
        
x=mybus ("rty","20ty",2027, "white","nig","67ft","7uy")
print(x)
        

