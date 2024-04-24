x=20
def myname():
    tunde=10
    global x
    def mutunde ():
        y=15
        print(tunde+x+y)
    mutunde()
myname()

import tunde
tunde.mysum(90,45)
print(tunde)

x=tunde.employee["name"]
print(x)


import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%d"))
print(x.strftime("%D"))
print(x.strftime("%W"))
print(x.strftime("%w"))