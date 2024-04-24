class Hotel:
    def __init__(self,name,capacity,state):
        self.name=name
        self.capacity=capacity
        self.state=state
    def __str__ (self):
         return f"{self.name} {self.capacity} {self.state}"
    
my_hotel=Hotel("rev", 456,"Akwa")
print(my_hotel)

class Hotel4:
    def __init__(self,name,capacity,state):
        self.name=name
        self.capacity=capacity
        self.state=state
    def __str__ (self):
         return f"{self.name} {self.capacity} {self.state}"
my_hotel4=Hotel4("rev4", 4564,"Akwa4")
print(my_hotel4)

class Hotel5:
    def __init__(self,name,capacity,state):
        self.name=name
        self.capacity=capacity
        self.state=state
    def __str__ (self):
         return f"{self.name} {self.capacity} {self.state}"
my_hotel5=Hotel("rev5", 4565,"Akwa5")
print(my_hotel5)

