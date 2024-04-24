
import random
import sys

while True:


   x=random.randint(0,9)

   print("guess the random number x")
   reply=int(input( "what is your guess number >>  \n"))
   if reply==x:
       print("correct!")
       break
   else:
       print(f"your guess is wrong, the rigth answer is {x}")
       print("would like to try again, \n 1.yes, \n2.no")
    
       response= input("choice  >> ")
   if response == 1:
               continue
            
   else:
        break
SystemExit



