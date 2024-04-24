import sys

guest_number=8
guest_limit=3
while True:
    guest_count=0
    while guest_count< guest_limit:
        print(" guest the rigth number ")
        response=int(input("input the rigth number  >> "))
        if response==guest_number:
            print("correct, congratulations")
            break
        else:
            print("oops, try again")
            guest_count += 1
        if guest_count == guest_limit:
            print("you have reach your limit")
            print ("would you like to try again \n1.yes, \n2.no")
            reply=str(input("what is your reply    >>  "))
            if reply==1 or reply=="yes":
               continue #Restart the game
            #elif reply==2 or reply== "no":
            else: 
              sys.exit() #Exit the program
                