#interger=range(2,7)
#for i in interger:
 #   for r in interger:
  #   print("scores of virtua game")
   #  print(f"teamA {i} * teamB  {r}")

while True:
    guess_number=6
    guess_count=0
    guess_limit=3

    while guess_count < guess_limit:
       print ("guess the rigth number")
    response=input("enter you guess >>  ")
    guess_count +=1
    if response==guess_number:
        print("correct, win")
    else:
        continue
 
    

