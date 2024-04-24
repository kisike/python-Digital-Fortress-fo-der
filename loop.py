"""while loop"""
import sys
guest_number = 9
guest_limit = 3
while True:
    guest_count = 0
    while  guest_count < guest_limit:
       response = int(input("enter your guest\n >>  "))
       if response == guest_number:
           print(" woo! correct")
           break
       else:
            print("oops , try again ! \n >>")
       guest_count +=1
    if guest_count == guest_limit: 
        print ("you have reached your limit")
        print (" would you like to try again \n 1. yes \n 2. no")
        reply = int(input(">> "))
        if reply == 1: 
            continue #Restart the game  
        else:
             print ("thanks for trying 😊😊😊")
    sys.exit # Exit the program

         

        


