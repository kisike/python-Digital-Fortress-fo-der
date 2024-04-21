'''while loop'''

print("0.off \n  1.on  n>>")
command=""

while command != "burn":
    command= input(" >>  ")
    print ("ok")
    if command.lower()=="off":
        print("the bulb is off💡❌")
    elif command.lower()=="on":
        print("the bulb is on 💡")
    else:
        print("burnt !!!")
        print ("done")

